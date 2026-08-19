"""Prep ship-skin PNGs for LAST STAND: key out fake checkerboard backgrounds, crop, normalize to a 300x216 frame.
Usage: python prep_skins.py <img_dir> [--sheet out.png]
"""
import sys, glob, os
from collections import deque
import numpy as np
from PIL import Image, ImageDraw

OUT_W, OUT_H = 300, 216      # same aspect as player.png (150x108), 4x authored
MARGIN = 6                   # px of transparent margin inside the frame

def is_checker(rgb):
    """boolean mask of pixels that look like the fake checkerboard: very light + neutral"""
    r, g, b = rgb[..., 0].astype(int), rgb[..., 1].astype(int), rgb[..., 2].astype(int)
    mn = np.minimum(np.minimum(r, g), b); mx = np.maximum(np.maximum(r, g), b)
    return (mn >= 236) & ((mx - mn) <= 8)

def flood_from_border(mask):
    """pixels of `mask` connected (4-neigh) to the image border"""
    h, w = mask.shape
    seen = np.zeros_like(mask, dtype=bool)
    q = deque()
    for x in range(w):
        for y in (0, h - 1):
            if mask[y, x] and not seen[y, x]: seen[y, x] = True; q.append((y, x))
    for y in range(h):
        for x in (0, w - 1):
            if mask[y, x] and not seen[y, x]: seen[y, x] = True; q.append((y, x))
    while q:
        y, x = q.popleft()
        for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
            if 0 <= ny < h and 0 <= nx < w and mask[ny, nx] and not seen[ny, nx]:
                seen[ny, nx] = True; q.append((ny, nx))
    return seen

def enclosed_checker_pockets(mask, rgb, border_bg):
    """remaining checker-colored components (not touching border) that contain BOTH checker tones -> background pockets"""
    h, w = mask.shape
    rest = mask & ~border_bg
    lum = rgb[..., 0].astype(int)
    seen = np.zeros_like(mask, dtype=bool)
    remove = np.zeros_like(mask, dtype=bool)
    ys, xs = np.nonzero(rest)
    for y0, x0 in zip(ys, xs):
        if seen[y0, x0]: continue
        comp = []
        q = deque([(y0, x0)]); seen[y0, x0] = True
        while q:
            y, x = q.popleft(); comp.append((y, x))
            for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
                if 0 <= ny < h and 0 <= nx < w and rest[ny, nx] and not seen[ny, nx]:
                    seen[ny, nx] = True; q.append((ny, nx))
        if len(comp) < 150: continue
        cy = np.array([c[0] for c in comp]); cx = np.array([c[1] for c in comp])
        l = lum[cy, cx]
        white = np.mean(l >= 251); grey = np.mean(l <= 249)
        if white > 0.12 and grey > 0.12:      # two-tone => checkerboard pocket
            remove[cy, cx] = True
    return remove

def process(path):
    im = Image.open(path)
    has_alpha = im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info)
    im = im.convert('RGBA')
    a = np.array(im)
    rgb = a[..., :3]
    keyed = False
    if not (has_alpha and a[0, 0, 3] == 0 and a[0, -1, 3] == 0):
        mask = is_checker(rgb)
        bg = flood_from_border(mask)
        bg |= enclosed_checker_pockets(mask, rgb, bg)
        alpha = a[..., 3].copy(); alpha[bg] = 0
        # soften 1px fringe: pixels touching background that are still very light get partial alpha
        light = is_checker(rgb) | ((rgb.min(axis=2) >= 225) & ((rgb.max(axis=2).astype(int) - rgb.min(axis=2)) <= 12))
        edge = np.zeros_like(bg)
        edge[1:, :] |= bg[:-1, :]; edge[:-1, :] |= bg[1:, :]; edge[:, 1:] |= bg[:, :-1]; edge[:, :-1] |= bg[:, 1:]
        fr = edge & ~bg & light
        alpha[fr] = 90
        a[..., 3] = alpha
        keyed = True
    # crop to content
    ys, xs = np.nonzero(a[..., 3] > 8)
    if len(ys) == 0: raise RuntimeError('empty after keying: ' + path)
    y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
    crop = Image.fromarray(a[y0:y1, x0:x1])
    # fit into frame, preserving aspect
    bw, bh = OUT_W - 2 * MARGIN, OUT_H - 2 * MARGIN
    s = min(bw / crop.width, bh / crop.height)
    nw, nh = max(1, round(crop.width * s)), max(1, round(crop.height * s))
    crop = crop.resize((nw, nh), Image.LANCZOS)
    out = Image.new('RGBA', (OUT_W, OUT_H), (0, 0, 0, 0))
    out.paste(crop, ((OUT_W - nw) // 2, (OUT_H - nh) // 2), crop)
    out.save(path, optimize=True)
    return keyed, (x1 - x0, y1 - y0)

def main():
    d = sys.argv[1]
    sheet = None
    if '--sheet' in sys.argv: sheet = sys.argv[sys.argv.index('--sheet') + 1]
    files = sorted(glob.glob(os.path.join(d, 'skin_*.png')))
    tiles = []
    for f in files:
        keyed, bbox = process(f)
        print(os.path.basename(f), 'keyed' if keyed else 'alpha-ok', 'bbox', bbox, flush=True)
        tiles.append((os.path.basename(f), Image.open(f).convert('RGBA')))
    if sheet:
        cols = 4; rows = (len(tiles) + cols - 1) // cols
        S = Image.new('RGBA', (cols * (OUT_W + 10), rows * (OUT_H + 26)), (20, 28, 44, 255))
        dr = ImageDraw.Draw(S)
        for i, (name, t) in enumerate(tiles):
            x, y = (i % cols) * (OUT_W + 10), (i // cols) * (OUT_H + 26)
            dr.rectangle([x, y, x + OUT_W, y + OUT_H], outline=(60, 80, 120, 255))
            S.paste(t, (x, y), t); dr.text((x + 4, y + OUT_H + 6), name, fill=(220, 230, 245, 255))
        S.save(sheet)

if __name__ == '__main__':
    main()

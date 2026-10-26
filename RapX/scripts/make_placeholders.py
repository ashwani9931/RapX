"""Generate placeholder PNGs for the landing page using only the standard library.

Run from the repo root:
    python scripts/make_placeholders.py

Writes:
    static/img/model.png      400x520, dark red -> black gradient with a dark
                              silhouette and a red/orange rim light
    static/img/avatar-1.png   48x48 flat grey
    static/img/avatar-2.png
    static/img/avatar-3.png
Replace model.png with the real photo at the same path when available.
"""

from __future__ import annotations

import math
import struct
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMG_DIR = ROOT / "static" / "img"


def _chunk(tag: bytes, data: bytes) -> bytes:
    crc = zlib.crc32(tag + data) & 0xFFFFFFFF
    return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", crc)


def write_png(path: Path, width: int, height: int, pixel) -> None:
    """Write an 8-bit RGB PNG. `pixel(x, y)` returns an (r, g, b) tuple."""
    rows = bytearray()
    for y in range(height):
        rows.append(0)  # filter type: none
        for x in range(width):
            r, g, b = pixel(x, y)
            rows += bytes((_clamp(r), _clamp(g), _clamp(b)))
    ihdr = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    png = (
        b"\x89PNG\r\n\x1a\n"
        + _chunk(b"IHDR", ihdr)
        + _chunk(b"IDAT", zlib.compress(bytes(rows), 9))
        + _chunk(b"IEND", b"")
    )
    path.write_bytes(png)


def _clamp(v: float) -> int:
    return max(0, min(255, int(round(v))))


def _lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t


def model_pixel_factory(width: int, height: int):
    """Dark red->black vertical gradient with a head-and-shoulders silhouette.

    The silhouette is near-black; a thin red/orange rim light hugs its edge so
    the shape reads as a backlit figure, similar to the reference photo.
    """
    cx = width / 2
    head_cy, head_r = height * 0.17, width * 0.11
    neck_top, neck_half = head_cy + head_r * 0.8, width * 0.055
    shoulder_y = height * 0.36
    torso_half_top, torso_half_bot = width * 0.40, width * 0.30

    def inside(x: float, y: float) -> float:
        """Signed distance-ish: >0 inside the figure, <0 outside (in px)."""
        d_head = head_r - math.hypot(x - cx, y - head_cy)

        d_neck = -1e9
        if neck_top <= y <= shoulder_y:
            d_neck = neck_half - abs(x - cx)

        d_torso = -1e9
        if y >= shoulder_y:
            t = min(1.0, (y - shoulder_y) / (height - shoulder_y))
            half = _lerp(torso_half_top, torso_half_bot, t)
            # Rounded shoulders: shrink width near the top of the torso.
            shoulder_round = min(1.0, (y - shoulder_y) / (width * 0.12))
            half = _lerp(torso_half_top * 0.55, half, math.sqrt(shoulder_round))
            d_torso = half - abs(x - cx)

        return max(d_head, d_neck, d_torso)

    def pixel(x: int, y: int):
        t = y / (height - 1)
        # Background: dark red at top fading to black at the bottom, slightly
        # brighter toward the horizontal centre.
        centre = 1 - min(1.0, abs(x - cx) / cx)
        bg_r = _lerp(78, 0, t) * (0.55 + 0.45 * centre)
        bg_g = _lerp(10, 0, t) * (0.55 + 0.45 * centre)
        bg_b = _lerp(12, 0, t) * (0.55 + 0.45 * centre)

        d = inside(x, y)
        if d <= 0:
            return bg_r, bg_g, bg_b

        # Inside the silhouette: near-black body with a rim light that is
        # strongest on the edge and fades over ~14px inward.
        rim = max(0.0, 1 - d / 14.0)
        rim = rim * rim
        # Rim is warmer (orange) on the upper body, redder lower down.
        warm = 1 - t
        rim_r = _lerp(200, 255, warm)
        rim_g = _lerp(30, 110, warm)
        rim_b = _lerp(20, 30, warm)
        body = 8 + 6 * (1 - t)
        return (
            _lerp(body, rim_r, rim),
            _lerp(body * 0.8, rim_g, rim),
            _lerp(body * 0.9, rim_b, rim),
        )

    return pixel


def main() -> None:
    IMG_DIR.mkdir(parents=True, exist_ok=True)

    write_png(IMG_DIR / "model.png", 400, 520, model_pixel_factory(400, 520))

    greys = (0x6E, 0x80, 0x5A)
    for i, g in enumerate(greys, start=1):
        write_png(IMG_DIR / f"avatar-{i}.png", 48, 48, lambda x, y, g=g: (g, g, g + 6))

    for name in ("model.png", "avatar-1.png", "avatar-2.png", "avatar-3.png"):
        print(f"wrote {IMG_DIR / name}")


if __name__ == "__main__":
    main()

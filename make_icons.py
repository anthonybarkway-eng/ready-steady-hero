"""Draw the app icon (a traffic light on a sky) as PNGs, with no image libraries needed."""
import math
import pathlib
import struct
import zlib

ROOT = pathlib.Path(__file__).resolve().parent


def png_bytes(w, h, pixel):
    raw = bytearray()
    for y in range(h):
        raw.append(0)
        for x in range(w):
            raw.extend(pixel(x, y))

    def chunk(tag, data):
        return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)

    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(bytes(raw), 9)) + chunk(b"IEND", b""))


def lerp(a, b, t):
    return tuple(int(round(a[i] + (b[i] - a[i]) * t)) for i in range(3))


def icon(size):
    s = size
    sky_top, sky_bottom = (0x8F, 0xD8, 0xFF), (0xEC, 0xF9, 0xFF)
    grass = (0x6E, 0xC8, 0x4A)
    body = (0x2B, 0x2D, 0x42)
    lamps = [(0xE6, 0x39, 0x46), (0xFF, 0xB7, 0x03), (0x2D, 0xC6, 0x53)]
    # traffic light body: rounded rectangle centred, lamps stacked inside
    bw, bh, r = 0.46 * s, 0.80 * s, 0.11 * s
    bx0, by0 = (s - bw) / 2, (s - bh) / 2
    lamp_r = 0.105 * s
    lamp_cx = s / 2
    lamp_cy = [by0 + bh * f for f in (0.22, 0.5, 0.78)]
    ss = 3  # supersampling

    def inside_rrect(x, y):
        cx = min(max(x, bx0 + r), bx0 + bw - r)
        cy = min(max(y, by0 + r), by0 + bh - r)
        return (x - cx) ** 2 + (y - cy) ** 2 <= r * r

    def sample(x, y):
        for cy, col in zip(lamp_cy, lamps):
            if (x - lamp_cx) ** 2 + (y - cy) ** 2 <= lamp_r * lamp_r:
                return col
        if inside_rrect(x, y):
            return body
        if y > 0.86 * s:
            return grass
        return lerp(sky_top, sky_bottom, y / (0.86 * s))

    def pixel(px, py):
        acc = [0, 0, 0]
        for i in range(ss):
            for j in range(ss):
                c = sample(px + (i + 0.5) / ss, py + (j + 0.5) / ss)
                acc[0] += c[0]; acc[1] += c[1]; acc[2] += c[2]
        n = ss * ss
        return (acc[0] // n, acc[1] // n, acc[2] // n)

    return png_bytes(s, s, pixel)


for size in (180, 192, 512):
    out = ROOT / f"icon-{size}.png"
    out.write_bytes(icon(size))
    print("wrote", out.name, out.stat().st_size, "bytes")

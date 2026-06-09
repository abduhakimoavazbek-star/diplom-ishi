# -*- coding: utf-8 -*-
"""
Toza Python (faqat stdlib) PNG chizish kutubxonasi.
Hech qanday tashqi paketga bog'liq emas (matplotlib/PIL kerak emas).
Chizish primitivlari: piksel, chiziq, to'rtburchak, doira, matn (bitmap shrift).
"""
import struct
import zlib
import math


class Canvas:
    def __init__(self, w, h, bg=(255, 255, 255)):
        self.w = w
        self.h = h
        # RGB buffer, har piksel 3 bayt
        self.buf = bytearray(bg * (w * h))

    def _idx(self, x, y):
        return (y * self.w + x) * 3

    def px(self, x, y, color):
        x = int(round(x))
        y = int(round(y))
        if 0 <= x < self.w and 0 <= y < self.h:
            i = self._idx(x, y)
            self.buf[i] = color[0]
            self.buf[i + 1] = color[1]
            self.buf[i + 2] = color[2]

    def line(self, x0, y0, x1, y1, color=(0, 0, 0), width=1):
        x0, y0, x1, y1 = int(round(x0)), int(round(y0)), int(round(x1)), int(round(y1))
        dx = abs(x1 - x0)
        dy = -abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx + dy
        r = width // 2
        while True:
            if width <= 1:
                self.px(x0, y0, color)
            else:
                for ox in range(-r, r + 1):
                    for oy in range(-r, r + 1):
                        self.px(x0 + ox, y0 + oy, color)
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 >= dy:
                err += dy
                x0 += sx
            if e2 <= dx:
                err += dx
                y0 += sy

    def rect(self, x0, y0, x1, y1, color=(0, 0, 0), width=1):
        self.line(x0, y0, x1, y0, color, width)
        self.line(x1, y0, x1, y1, color, width)
        self.line(x1, y1, x0, y1, color, width)
        self.line(x0, y1, x0, y0, color, width)

    def fill_rect(self, x0, y0, x1, y1, color):
        x0, x1 = sorted((int(round(x0)), int(round(x1))))
        y0, y1 = sorted((int(round(y0)), int(round(y1))))
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1):
                self.px(x, y, color)

    def circle(self, cx, cy, r, color=(0, 0, 0), width=1):
        steps = max(24, int(2 * math.pi * r))
        prev = None
        for i in range(steps + 1):
            a = 2 * math.pi * i / steps
            x = cx + r * math.cos(a)
            y = cy + r * math.sin(a)
            if prev is not None:
                self.line(prev[0], prev[1], x, y, color, width)
            prev = (x, y)

    def fill_circle(self, cx, cy, r, color):
        for y in range(int(cy - r), int(cy + r) + 1):
            for x in range(int(cx - r), int(cx + r) + 1):
                if (x - cx) ** 2 + (y - cy) ** 2 <= r * r:
                    self.px(x, y, color)

    def polyline(self, pts, color=(0, 0, 0), width=1):
        for i in range(len(pts) - 1):
            self.line(pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1], color, width)

    def arrow(self, x0, y0, x1, y1, color=(0, 0, 0), width=2, head=7):
        self.line(x0, y0, x1, y1, color, width)
        ang = math.atan2(y1 - y0, x1 - x0)
        for da in (math.radians(150), math.radians(-150)):
            hx = x1 + head * math.cos(ang + da)
            hy = y1 + head * math.sin(ang + da)
            self.line(x1, y1, hx, hy, color, width)

    def text(self, x, y, s, color=(0, 0, 0), scale=2, spacing=1):
        """Matnni chap-tepa burchakdan chizadi. Faqat katta harf/raqam/belgi."""
        cx = int(x)
        s = s.upper()
        for ch in s:
            glyph = FONT.get(ch, FONT.get('?'))
            for ry, row in enumerate(glyph):
                for rxi, bit in enumerate(row):
                    if bit == '#':
                        self.fill_rect(cx + rxi * scale, y + ry * scale,
                                       cx + rxi * scale + scale - 1,
                                       y + ry * scale + scale - 1, color)
            cx += (GLYPH_W + spacing) * scale

    def text_center(self, cx, y, s, color=(0, 0, 0), scale=2, spacing=1):
        w = self.text_width(s, scale, spacing)
        self.text(int(cx - w / 2), y, s, color, scale, spacing)

    @staticmethod
    def text_width(s, scale=2, spacing=1):
        return len(s) * (GLYPH_W + spacing) * scale

    def save(self, path):
        raw = bytearray()
        stride = self.w * 3
        for y in range(self.h):
            raw.append(0)  # filter type 0
            raw.extend(self.buf[y * stride:(y + 1) * stride])
        compressed = zlib.compress(bytes(raw), 9)

        def chunk(typ, data):
            c = struct.pack(">I", len(data)) + typ + data
            crc = zlib.crc32(typ + data) & 0xffffffff
            return c + struct.pack(">I", crc)

        sig = b"\x89PNG\r\n\x1a\n"
        ihdr = struct.pack(">IIBBBBB", self.w, self.h, 8, 2, 0, 0, 0)
        with open(path, "wb") as f:
            f.write(sig)
            f.write(chunk(b"IHDR", ihdr))
            f.write(chunk(b"IDAT", compressed))
            f.write(chunk(b"IEND", b""))


# ----- 5x7 bitmap shrift (8 qator balandlik konteyner, kenglik 5) -----
GLYPH_W = 5

FONT = {
    ' ': ["     ", "     ", "     ", "     ", "     ", "     ", "     "],
    'A': [" ### ", "#   #", "#   #", "#####", "#   #", "#   #", "#   #"],
    'B': ["#### ", "#   #", "#   #", "#### ", "#   #", "#   #", "#### "],
    'C': [" ### ", "#   #", "#    ", "#    ", "#    ", "#   #", " ### "],
    'D': ["#### ", "#   #", "#   #", "#   #", "#   #", "#   #", "#### "],
    'E': ["#####", "#    ", "#    ", "#### ", "#    ", "#    ", "#####"],
    'F': ["#####", "#    ", "#    ", "#### ", "#    ", "#    ", "#    "],
    'G': [" ### ", "#   #", "#    ", "# ###", "#   #", "#   #", " ### "],
    'H': ["#   #", "#   #", "#   #", "#####", "#   #", "#   #", "#   #"],
    'I': ["#####", "  #  ", "  #  ", "  #  ", "  #  ", "  #  ", "#####"],
    'J': ["  ###", "   # ", "   # ", "   # ", "#  # ", "#  # ", " ##  "],
    'K': ["#   #", "#  # ", "# #  ", "##   ", "# #  ", "#  # ", "#   #"],
    'L': ["#    ", "#    ", "#    ", "#    ", "#    ", "#    ", "#####"],
    'M': ["#   #", "## ##", "# # #", "# # #", "#   #", "#   #", "#   #"],
    'N': ["#   #", "##  #", "# # #", "# # #", "#  ##", "#   #", "#   #"],
    'O': [" ### ", "#   #", "#   #", "#   #", "#   #", "#   #", " ### "],
    'P': ["#### ", "#   #", "#   #", "#### ", "#    ", "#    ", "#    "],
    'Q': [" ### ", "#   #", "#   #", "#   #", "# # #", "#  # ", " ## #"],
    'R': ["#### ", "#   #", "#   #", "#### ", "# #  ", "#  # ", "#   #"],
    'S': [" ####", "#    ", "#    ", " ### ", "    #", "    #", "#### "],
    'T': ["#####", "  #  ", "  #  ", "  #  ", "  #  ", "  #  ", "  #  "],
    'U': ["#   #", "#   #", "#   #", "#   #", "#   #", "#   #", " ### "],
    'V': ["#   #", "#   #", "#   #", "#   #", "#   #", " # # ", "  #  "],
    'W': ["#   #", "#   #", "#   #", "# # #", "# # #", "## ##", "#   #"],
    'X': ["#   #", "#   #", " # # ", "  #  ", " # # ", "#   #", "#   #"],
    'Y': ["#   #", "#   #", " # # ", "  #  ", "  #  ", "  #  ", "  #  "],
    'Z': ["#####", "    #", "   # ", "  #  ", " #   ", "#    ", "#####"],
    '0': [" ### ", "#   #", "#  ##", "# # #", "##  #", "#   #", " ### "],
    '1': ["  #  ", " ##  ", "  #  ", "  #  ", "  #  ", "  #  ", " ### "],
    '2': [" ### ", "#   #", "    #", "   # ", "  #  ", " #   ", "#####"],
    '3': ["#####", "   # ", "  #  ", "   # ", "    #", "#   #", " ### "],
    '4': ["   # ", "  ## ", " # # ", "#  # ", "#####", "   # ", "   # "],
    '5': ["#####", "#    ", "#### ", "    #", "    #", "#   #", " ### "],
    '6': ["  ## ", " #   ", "#    ", "#### ", "#   #", "#   #", " ### "],
    '7': ["#####", "    #", "   # ", "  #  ", " #   ", " #   ", " #   "],
    '8': [" ### ", "#   #", "#   #", " ### ", "#   #", "#   #", " ### "],
    '9': [" ### ", "#   #", "#   #", " ####", "    #", "   # ", " ##  "],
    '.': ["     ", "     ", "     ", "     ", "     ", " ##  ", " ##  "],
    ',': ["     ", "     ", "     ", "     ", " ##  ", " ##  ", "#    "],
    '-': ["     ", "     ", "     ", "#####", "     ", "     ", "     "],
    '+': ["     ", "  #  ", "  #  ", "#####", "  #  ", "  #  ", "     "],
    ':': ["     ", " ##  ", " ##  ", "     ", " ##  ", " ##  ", "     "],
    '/': ["    #", "    #", "   # ", "  #  ", " #   ", "#    ", "#    "],
    '(': ["   # ", "  #  ", " #   ", " #   ", " #   ", "  #  ", "   # "],
    ')': [" #   ", "  #  ", "   # ", "   # ", "   # ", "  #  ", " #   "],
    '%': ["##  #", "##  #", "   # ", "  #  ", " #   ", "#  ##", "#  ##"],
    '=': ["     ", "     ", "#####", "     ", "#####", "     ", "     "],
    "'": [" ##  ", " ##  ", " #   ", "     ", "     ", "     ", "     "],
    '?': [" ### ", "#   #", "   # ", "  #  ", "  #  ", "     ", "  #  "],
    '#': [" # # ", " # # ", "#####", " # # ", "#####", " # # ", " # # "],
    'x': ["     ", "     ", "#   #", " # # ", "  #  ", " # # ", "#   #"],
    'X2': [],
}

# kichik harflar uchun katta harf bilan almashtirish (text() upper qiladi)

if __name__ == "__main__":
    # Shriftni tekshirish: ASCII-dump
    test = "ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789 .-+:/()%='"
    for ch in test:
        if ch == ' ':
            continue
        g = FONT.get(ch)
        print(f"--- '{ch}' ---")
        for row in g:
            print(row.replace(' ', '.'))

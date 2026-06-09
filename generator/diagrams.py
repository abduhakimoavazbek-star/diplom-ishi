# -*- coding: utf-8 -*-
"""Diplom ishi uchun chizmalar va grafiklarni yaratish (PNG)."""
import os
import math
from gfx import Canvas

OUT = os.path.join(os.path.dirname(__file__), "..", "img")
os.makedirs(OUT, exist_ok=True)

BLACK = (0, 0, 0)
BLUE = (20, 40, 140)
RED = (190, 30, 30)
GREEN = (30, 120, 50)
GRAY = (120, 120, 120)
LGRAY = (210, 210, 210)
ORANGE = (220, 130, 20)


def box(c, x0, y0, x1, y1, label, fill=None, tcolor=BLACK, scale=2, lw=2):
    if fill:
        c.fill_rect(x0, y0, x1, y1, fill)
    c.rect(x0, y0, x1, y1, BLACK, lw)
    lines = label.split("\n")
    total_h = len(lines) * (8 * scale)
    yy = (y0 + y1) // 2 - total_h // 2
    for ln in lines:
        c.text_center((x0 + x1) // 2, yy, ln, tcolor, scale)
        yy += 8 * scale


# ---------- 1.1 Tormoz tizimi umumiy sxemasi ----------
def fig_brake_system():
    c = Canvas(900, 620)
    c.text_center(450, 12, "1.1-RASM. NEXIA-3 TORMOZ TIZIMI UMUMIY SXEMASI", BLACK, 2)
    # Pedal
    box(c, 60, 70, 180, 120, "TORMOZ\nPEDALI", fill=LGRAY)
    # Vacuum booster
    box(c, 230, 60, 380, 130, "VAKUUM\nKUCHAYTIRGICH", fill=(225, 235, 250))
    # Master cylinder
    box(c, 430, 60, 600, 130, "BOSH TORMOZ\nSILINDRI", fill=(225, 235, 250))
    # Reservoir
    box(c, 460, 10, 570, 55, "REZERVUAR\nDOT-4", fill=(235, 245, 235), scale=2)
    c.line(515, 55, 515, 60, BLACK, 2)
    # ABS modulator
    box(c, 380, 280, 540, 350, "ABS\nGIDROBLOK", fill=(250, 240, 225))
    # connections
    c.arrow(180, 95, 230, 95, BLACK, 2)
    c.arrow(380, 95, 430, 95, BLACK, 2)
    c.line(515, 130, 515, 200, BLUE, 2)
    c.line(515, 200, 460, 200, BLUE, 2)
    c.arrow(460, 200, 460, 280, BLUE, 2)
    # to four wheels
    # front-left disc
    def wheel(cx, cy, kind, name):
        c.circle(cx, cy, 38, BLACK, 2)
        if kind == "disc":
            c.fill_circle(cx, cy, 22, (200, 210, 220))
            c.circle(cx, cy, 22, BLACK, 1)
            c.fill_rect(cx - 8, cy - 30, cx + 8, cy - 18, (120, 120, 120))  # caliper
        else:
            c.circle(cx, cy, 24, BLACK, 1)
            c.fill_circle(cx, cy, 6, (160, 160, 160))
        c.text_center(cx, cy + 44, name, BLACK, 2)
    wheel(170, 300, "disc", "OLD CHAP\nDISK")
    wheel(170, 470, "disc", "OLD O'NG\nDISK")
    wheel(740, 300, "drum", "ORQA CHAP\nBARABAN")
    wheel(740, 470, "drum", "ORQA O'NG\nBARABAN")
    # lines ABS -> wheels (diagonal split)
    c.arrow(380, 300, 215, 300, RED, 2)      # front-left
    c.arrow(540, 320, 700, 470, RED, 2)      # rear-right (diagonal contour I)
    c.arrow(380, 330, 210, 470, BLUE, 2)     # front-right
    c.arrow(540, 300, 702, 300, BLUE, 2)     # rear-left (diagonal contour II)
    c.text(560, 250, "DIAGONAL IKKI KONTUR", RED, 2)
    # legend
    c.text(60, 560, "1-PEDAL  2-KUCHAYTIRGICH  3-BOSH SILINDR  4-ABS  5-DISK MEXANIZM  6-BARABAN MEXANIZM", BLACK, 2)
    c.save(os.path.join(OUT, "fig_brake_system.png"))


# ---------- 1.2 Disk tormoz mexanizmi (kesim) ----------
def fig_disc_caliper():
    c = Canvas(820, 540)
    c.text_center(410, 12, "1.2-RASM. OLD DISK TORMOZ MEXANIZMI TUZILISHI", BLACK, 2)
    cx, cy = 360, 290
    # rotor (ventilated disc) - two plates with vanes
    c.fill_rect(cx - 18, cy - 170, cx + 18, cy + 170, (205, 210, 220))
    c.rect(cx - 18, cy - 170, cx + 18, cy + 170, BLACK, 2)
    # vanes
    for yy in range(cy - 160, cy + 160, 22):
        c.line(cx - 16, yy, cx + 16, yy, GRAY, 1)
    c.text_center(cx, cy + 178, "TORMOZ DISKI (ROTOR)", BLACK, 2)
    # pads
    c.fill_rect(cx - 60, cy - 70, cx - 22, cy + 70, (150, 90, 60))
    c.fill_rect(cx + 22, cy - 70, cx + 60, cy + 70, (150, 90, 60))
    c.text(cx - 200, cy - 60, "KOLODKA", BLACK, 2)
    c.line(cx - 95, cy - 50, cx - 60, cy - 40, BLACK, 1)
    # caliper body
    c.rect(cx - 150, cy - 95, cx - 60, cy + 95, BLACK, 2)
    c.rect(cx + 60, cy - 95, cx + 150, cy + 95, BLACK, 2)
    c.line(cx - 150, cy - 95, cx + 150, cy - 95, BLACK, 2)
    c.line(cx - 150, cy + 95, cx + 150, cy + 95, BLACK, 2)
    # piston
    c.fill_rect(cx - 130, cy - 35, cx - 95, cy + 35, (235, 225, 180))
    c.rect(cx - 130, cy - 35, cx - 95, cy + 35, BLACK, 1)
    c.text_center(cx - 112, cy + 110, "PORSHEN", BLACK, 2)
    c.text_center(cx + 105, cy + 110, "SUPORT", BLACK, 2)
    # hydraulic inlet
    c.line(cx - 150, cy, cx - 200, cy, BLUE, 3)
    c.arrow(cx - 200, cy, cx - 150, cy, BLUE, 3)
    c.text(cx - 320, cy - 16, "GIDRAVLIK\nBOSIM", BLUE, 2)
    c.text(cx - 320, cy + 0, "", BLUE, 2)
    # dimensions
    c.line(cx + 200, cy - 170, cx + 200, cy + 170, BLACK, 1)
    c.line(cx + 190, cy - 170, cx + 210, cy - 170, BLACK, 1)
    c.line(cx + 190, cy + 170, cx + 210, cy + 170, BLACK, 1)
    c.text(cx + 215, cy - 10, "D=256", BLACK, 2)
    c.text(cx + 215, cy + 14, "MM", BLACK, 2)
    c.save(os.path.join(OUT, "fig_disc_caliper.png"))


# ---------- 1.3 Gidravlik sxema ----------
def fig_hydraulic():
    c = Canvas(900, 560)
    c.text_center(450, 12, "1.3-RASM. GIDRAVLIK TORMOZ YURITMASI PRINSIPIAL SXEMASI", BLACK, 2)
    box(c, 60, 60, 180, 120, "PEDAL", fill=LGRAY)
    box(c, 220, 50, 360, 130, "VAKUUM\nKUCHAYTIRGICH", fill=(225, 235, 250))
    box(c, 400, 50, 540, 130, "BOSH\nSILINDR", fill=(225, 235, 250))
    box(c, 420, 0, 520, 45, "BACHOK", fill=(235, 245, 235))
    c.line(470, 45, 470, 50, BLACK, 2)
    c.arrow(180, 90, 220, 90, BLACK, 2)
    c.arrow(360, 90, 400, 90, BLACK, 2)
    # main line down
    c.line(540, 90, 620, 90, BLUE, 3)
    c.line(620, 90, 620, 470, BLUE, 3)
    box(c, 560, 230, 700, 300, "ABS\nMODULATOR", fill=(250, 240, 225))
    c.line(620, 230, 620, 90, BLUE, 3)
    # branches to cylinders
    ys = [170, 250 + 90, 420]
    # front cylinders
    def cyl(x, y, name):
        c.rect(x, y - 22, x + 70, y + 22, BLACK, 2)
        c.fill_rect(x + 2, y - 18, x + 30, y + 18, (235, 225, 180))
        c.text(x + 80, y - 8, name, BLACK, 2)
    c.line(620, 150, 800, 150, BLUE, 3); cyl(800, 150, "OLD CHAP")
    c.line(620, 360, 800, 360, BLUE, 3); cyl(800, 360, "ORQA O'NG")
    c.line(620, 470, 200, 470, BLUE, 3); cyl(130, 470, "OLD O'NG")
    c.line(360, 470, 360, 410, BLUE, 3); cyl(300, 410, "ORQA CHAP")
    # pressure label
    c.text(640, 110, "P=8-12 MPA", RED, 2)
    c.text(60, 520, "PASKAL QONUNI: BOSIM BARCHA SILINDRLARGA TENG UZATILADI", BLACK, 2)
    c.save(os.path.join(OUT, "fig_hydraulic.png"))


# ---------- 3.1 Texnologik jarayon blok-sxemasi ----------
def fig_process_flow():
    c = Canvas(760, 900)
    c.text_center(380, 12, "3.1-RASM. KAPITAL TA'MIRLASH TEXNOLOGIK JARAYONI BLOK-SXEMASI", BLACK, 2)
    steps = [
        ("QABUL QILISH VA DIAGNOSTIKA", (235, 245, 235)),
        ("DEMONTAJ", (225, 235, 250)),
        ("YUVISH VA TOZALASH", (225, 235, 250)),
        ("DEFEKTOVKA (O'LCHASH/NAZORAT)", (250, 240, 225)),
    ]
    y = 50
    cx = 380
    bw = 360
    prev_y = None
    for txt, col in steps:
        box(c, cx - bw // 2, y, cx + bw // 2, y + 50, txt, fill=col)
        if prev_y is not None:
            c.arrow(cx, prev_y, cx, y, BLACK, 2)
        prev_y = y + 50
        y += 95
    # decision diamond
    dy = y
    cyc = dy + 45
    pts = [(cx, dy), (cx + 130, cyc), (cx, dy + 90), (cx - 130, cyc)]
    c.polyline(pts + [pts[0]], BLACK, 2)
    c.text_center(cx, cyc - 16, "YAROQLIMI?", BLACK, 2)
    c.arrow(cx, prev_y, cx, dy, BLACK, 2)
    # branch yes -> assembly ; no -> restore/replace
    box(c, cx + 180, dy + 18, cx + 360, dy + 72, "TIKLASH /\nALMASHTIRISH", fill=(250, 230, 230))
    c.arrow(cx + 130, cyc, cx + 180, cyc, RED, 2)
    c.text(cx + 135, cyc - 22, "YO'Q", RED, 2)
    c.line(cx + 360, dy + 45, cx + 420, dy + 45, BLACK, 2)
    c.line(cx + 420, dy + 45, cx + 420, dy + 200, BLACK, 2)
    y2 = dy + 130
    c.text(cx + 20, cyc + 6, "HA", GREEN, 2)
    c.arrow(cx, dy + 90, cx, y2, GREEN, 2)
    rest = [
        ("YIG'ISH VA MONTAJ", (225, 235, 250)),
        ("SOZLASH VA HAVOSIZLANTIRISH", (225, 235, 250)),
        ("SINOV (STEND + ZICHLIK)", (250, 240, 225)),
        ("QABUL AKTI VA KAFOLAT", (235, 245, 235)),
    ]
    prev_y = y2
    yy = y2
    first = True
    for txt, col in rest:
        box(c, cx - bw // 2, yy, cx + bw // 2, yy + 50, txt, fill=col)
        if not first:
            c.arrow(cx, prev_y, cx, yy, BLACK, 2)
        first = False
        prev_y = yy + 50
        yy += 95
    # connect restore back into assembly input
    c.line(cx + 420, dy + 200, cx + bw // 2 + 5, y2 + 25, BLACK, 2)
    c.arrow(cx + bw // 2 + 5, y2 + 25, cx + bw // 2, y2 + 25, BLACK, 2)
    c.save(os.path.join(OUT, "fig_process_flow.png"))


# ---------- 3.5 Disk detali chizmasi (o'lchamlar bilan) ----------
def fig_disc_drawing():
    c = Canvas(760, 560)
    c.text_center(380, 12, "3.5-RASM. TORMOZ DISKI DETAL CHIZMASI (NEXIA-3 OLD)", BLACK, 2)
    cx, cy = 300, 300
    c.circle(cx, cy, 180, BLACK, 2)        # outer
    c.circle(cx, cy, 95, BLACK, 2)         # hat outer
    c.circle(cx, cy, 30, BLACK, 2)         # center bore
    # bolt holes
    for i in range(4):
        a = math.radians(45 + i * 90)
        bx = cx + 60 * math.cos(a)
        by = cy + 60 * math.sin(a)
        c.circle(bx, by, 9, BLACK, 1)
    # friction ring hatch
    for r in (120, 150, 170):
        c.circle(cx, cy, r, LGRAY, 1)
    # dimension lines
    c.line(cx - 180, cy + 210, cx + 180, cy + 210, BLACK, 1)
    c.line(cx - 180, cy + 200, cx - 180, cy + 220, BLACK, 1)
    c.line(cx + 180, cy + 200, cx + 180, cy + 220, BLACK, 1)
    c.text_center(cx, cy + 224, "D=256 MM", BLACK, 2)
    c.line(cx - 30, cy - 210, cx + 30, cy - 210, BLACK, 1)
    c.text_center(cx, cy - 232, "d=60 MM", BLACK, 2)
    # technical requirements box
    bx0 = 540
    c.rect(bx0, 120, 748, 470, BLACK, 2)
    c.text(bx0 + 8, 130, "TEXNIK TALABLAR:", BLACK, 2)
    reqs = [
        "1. MATERIAL:",
        "   CHO'YAN GG-20",
        "2. QALINLIK 24 MM",
        "   (MIN 22 MM)",
        "3. RUN-OUT",
        "   <= 0.05 MM",
        "4. SIRT Ra<=1.6",
        "5. QATTIQLIK",
        "   HB 180-220",
    ]
    yy = 158
    for r in reqs:
        c.text(bx0 + 8, yy, r, BLACK, 2)
        yy += 22
    c.text_center(cx, cy, "+", BLACK, 2)
    c.save(os.path.join(OUT, "fig_disc_drawing.png"))


# ---------- 4.x grafik: Tormozlash kuchi - bosim ----------
def chart_axes(c, ox, oy, w, h, xmax, ymax, xlabel, ylabel, title):
    c.text_center(ox + w // 2, 10, title, BLACK, 2)
    c.line(ox, oy, ox, oy - h, BLACK, 2)       # y axis
    c.line(ox, oy, ox + w, oy, BLACK, 2)       # x axis
    # gridlines x
    for i in range(1, 6):
        x = ox + w * i / 5
        c.line(x, oy, x, oy - h, LGRAY, 1)
        c.text_center(x, oy + 8, str(round(xmax * i / 5, 1)), BLACK, 2)
    for i in range(1, 6):
        yv = oy - h * i / 5
        c.line(ox, yv, ox + w, yv, LGRAY, 1)
        c.text(ox - 52, yv - 7, str(round(ymax * i / 5, 1)), BLACK, 2)
    c.text(ox + w // 2 - 40, oy + 30, xlabel, BLACK, 2)
    c.text(ox - 40, oy - h - 22, ylabel, BLACK, 2)


def chart_force_pressure():
    c = Canvas(720, 520)
    ox, oy, w, h = 90, 440, 560, 360
    xmax, ymax = 12.0, 8.0  # P (MPa), F (kN) - g'ildirakdagi tutash kuch (2 kolodka)
    chart_axes(c, ox, oy, w, h, xmax, ymax,
               "BOSIM P, MPA", "KUCH F, KN",
               "4.1-RASM. TORMOZLASH KUCHINING BOSIMGA BOG'LIQLIGI")
    # F = 2*mu * P * A * Reff/rd  (2 kolodka). A=1.81e-3 m2, mu=0.4, Reff=0.10, rd=0.28
    mu, A, Reff, rd = 0.4, 1.8096e-3, 0.10, 0.28
    pts = []
    for i in range(0, 121):
        P = xmax * i / 120  # MPa
        F = 2 * mu * (P * 1e6) * A * Reff / rd / 1000.0  # kN
        x = ox + w * P / xmax
        y = oy - h * F / ymax
        pts.append((x, y))
    c.polyline(pts, RED, 2)
    # working point P=8 MPa
    Pw = 8.0
    Fw = 2 * mu * (Pw * 1e6) * A * Reff / rd / 1000.0
    xw = ox + w * Pw / xmax
    yw = oy - h * Fw / ymax
    c.fill_circle(xw, yw, 4, BLUE)
    c.line(xw, oy, xw, yw, BLUE, 1)
    c.line(ox, yw, xw, yw, BLUE, 1)
    c.text(xw + 6, yw - 24, "ISH NUQTASI", BLUE, 2)
    c.text(xw + 6, yw - 4, "P=8 F=" + str(round(Fw, 1)), BLUE, 2)
    c.save(os.path.join(OUT, "chart_force_pressure.png"))


def chart_temperature():
    c = Canvas(720, 520)
    ox, oy, w, h = 90, 440, 560, 360
    xmax, ymax = 10.0, 400.0  # tormozlashlar soni, harorat C
    chart_axes(c, ox, oy, w, h, xmax, ymax,
               "KETMA-KET TORMOZLASH SONI", "HARORAT, C",
               "4.2-RASM. DISK HARORATINING ORTISHI (60-0 KM/SOAT)")
    pts = []
    T = 35.0
    for n in range(0, 11):
        x = ox + w * n / xmax
        y = oy - h * min(T, ymax) / ymax
        pts.append((x, y))
        T = 35 + 320 * (1 - math.exp(-n / 3.0))  # to'yinish egri chizig'i
    c.polyline(pts, ORANGE, 2)
    for p in pts:
        c.fill_circle(p[0], p[1], 3, RED)
    # critical line at 300 C
    yc = oy - h * 300 / ymax
    c.line(ox, yc, ox + w, yc, RED, 1)
    c.text(ox + 8, yc - 22, "KRITIK 300 C - FEDING XAVFI", RED, 2)
    c.save(os.path.join(OUT, "chart_temperature.png"))


def chart_cost():
    c = Canvas(720, 520)
    ox, oy, w, h = 110, 430, 540, 340
    c.text_center(ox + w // 2, 10, "7.1-RASM. XARAJATLAR TAQQOSLASH (MING SO'M)", BLACK, 2)
    c.line(ox, oy, ox, oy - h, BLACK, 2)
    c.line(ox, oy, ox + w, oy, BLACK, 2)
    ymax = 1500.0
    for i in range(1, 6):
        yv = oy - h * i / 5
        c.line(ox, yv, ox + w, yv, LGRAY, 1)
        c.text(ox - 60, yv - 7, str(int(ymax * i / 5)), BLACK, 2)
    data = [("KAPITAL\nTA'MIRLASH", 637, GREEN), ("YANGI QISM\nXARIDI", 1190, RED)]
    bw = 120
    gap = 140
    x = ox + 80
    for name, val, col in data:
        y = oy - h * val / ymax
        c.fill_rect(x, y, x + bw, oy, col)
        c.rect(x, y, x + bw, oy, BLACK, 1)
        c.text_center(x + bw // 2, y - 24, str(val), BLACK, 2)
        for i, ln in enumerate(name.split("\n")):
            c.text_center(x + bw // 2, oy + 10 + i * 18, ln, BLACK, 2)
        x += bw + gap
    c.text(ox + 60, oy - h - 0, "TEJAMKORLIK: 46%", BLUE, 2)
    c.save(os.path.join(OUT, "chart_cost.png"))


if __name__ == "__main__":
    fig_brake_system()
    fig_disc_caliper()
    fig_hydraulic()
    fig_process_flow()
    fig_disc_drawing()
    chart_force_pressure()
    chart_temperature()
    chart_cost()
    print("Barcha chizmalar yaratildi:")
    for f in sorted(os.listdir(OUT)):
        print("  ", f, os.path.getsize(os.path.join(OUT, f)), "bayt")

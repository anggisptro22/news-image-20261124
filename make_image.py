#!/usr/bin/env python3
# Draws entry.png: 1024x1024 news infographic for make.fun bounty news-image-20261124.
# All content drawn programmatically (rectangles, lines, text). No external images.
import os
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (16, 18, 26)
PAPER = (28, 31, 42)
CARD = (36, 40, 54)
FG = (240, 240, 235)
DIM = (170, 175, 185)
FONTS = "/usr/share/fonts/truetype/dejavu/"

def F(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)

f_mast = F("DejaVuSans-Bold.ttf", 52)
f_sub = F("DejaVuSans.ttf", 26)
f_tag = F("DejaVuSans-Bold.ttf", 20)
f_head = F("DejaVuSans-Bold.ttf", 29)
f_body = F("DejaVuSans.ttf", 21)

STORIES = [
    ("UKRAINE", (74, 144, 226), "Zelenskiy asks West for $125bn for 2027",
     "Sea drones hit Russian ships off Libya, Gulf of Finland"),
    ("MIDEAST", (230, 126, 34), "Houthis strike Riyadh's tallest tower",
     "11 wounded; Saudi-backed forces press Yemen offensive"),
    ("TECH", (155, 89, 182), "Nvidia reinstates Jensen Huang as CEO",
     "Board reversal days after exit, after Trump intervention"),
    ("AFRICA", (46, 204, 113), "Gavi to buy 1.5m Ebola vaccine doses",
     "New Bundibugyo shot for the big Congo outbreak"),
    ("CLIMATE", (241, 196, 15), "EU push to fix UN climate summits",
     "After COP31 in Türkiye collapses without a deal"),
    ("ASIA", (231, 76, 60), "China unveils new space station crew",
     "First foreign astronaut — a Pakistani — to fly"),
]

def wrap(d, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= maxw:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)
# top rule + masthead
d.rectangle([0, 0, W, 6], fill=(200, 60, 50))
d.text((W // 2, 74), "TUESDAY, 24 NOVEMBER 2026", font=f_mast, fill=FG, anchor="mm")
d.text((W // 2, 122), "THE WORLD IN ONE DAY  ·  SIX STORIES THAT MATTERED", font=f_sub, fill=DIM, anchor="mm")
d.line([40, 158, W - 40, 158], fill=(80, 85, 100), width=2)

top = 178
ch = 120  # card height
gap = 9
for i, (tag, color, head, body) in enumerate(STORIES):
    y = top + i * (ch + gap)
    d.rounded_rectangle([40, y, W - 40, y + ch], radius=10, fill=CARD)
    d.rectangle([40, y, 48, y + ch], fill=color)
    tw = d.textlength(tag, font=f_tag)
    d.rounded_rectangle([68, y + 16, 68 + tw + 24, y + 46], radius=6, fill=color)
    d.text((80, y + 31), tag, font=f_tag, fill=(20, 20, 24), anchor="lm")
    hl = wrap(d, head, f_head, W - 200)
    for j, ln in enumerate(hl):
        d.text((68, y + 60 + j * 33), ln, font=f_head, fill=FG)
    bl = wrap(d, body, f_body, W - 200)
    d.text((68, y + 60 + len(hl) * 33 + 3), bl[0], font=f_body, fill=DIM)

d.line([40, H - 34, W - 40, H - 34], fill=(80, 85, 100), width=2)
d.text((W // 2, H - 18), "make.fun · news-image-20261124 · all facts reported 24 Nov 2026", font=F("DejaVuSans.ttf", 18), fill=DIM, anchor="mm")

img.save("entry.png", optimize=True)
print("saved", os.path.getsize("entry.png"), "bytes")

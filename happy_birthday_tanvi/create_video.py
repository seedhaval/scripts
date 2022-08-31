from PIL import Image, ImageEnhance
import glob
import random
from moviepy.editor import *

car_lst_lr = list(glob.glob('car_img/lr/*.*'))
car_lst_ud = list(glob.glob('car_img/ud/*.*'))
cnv_width = 1600
cnv_height = 900
img_px = 150

l, r, u, d = "left right up down".split()


class Car:
    def __init__(self, ix, iy, dr, static, lftdx, topdx):
        self.left = ix
        self.top = iy
        self.dr = dr
        self.lftdx = lftdx
        self.topdx = topdx
        if dr in (l,r):
            self.fl = random.choice(car_lst_lr)
        else:
            self.fl = random.choice(car_lst_ud)
        self.img = Image.open(self.fl)
        self.base_img = self.img.copy()
        self.speed = random.choice((15, 38))
        self.static = static

    def shift(self, fid):
        if fid < 5:
            return
        elif self.static and 25 < fid < 55:
            sz = int(img_px - ((img_px - 40) / 30) * (fid - 25))
            self.left -= self.lftdx
            self.top -= self.topdx
            self.img = self.base_img.resize((sz, sz))
            self.img = ImageEnhance.Brightness(self.img).enhance(1+((fid-25)*.02))
        elif self.static:
            return
        elif self.dr == d:
            self.top += self.speed
        elif self.dr == u:
            self.top -= self.speed
        elif self.dr == l:
            self.left -= self.speed
        elif self.dr == r:
            self.left += self.speed


class Letter:
    def __init__(self, irow, icol, strtpos, width, ltr):
        self.irow = irow
        self.icol = icol
        self.ltr = ltr
        self.strtpos = strtpos
        self.width = width
        print(self.width)
        self.car_ar = []
        self.load_cars()

    def load_cars(self):
        for ir, row in enumerate(self.ltr):
            for ic, cell in enumerate(row):
                if cell == "|":
                    dr = random.choice((u, d))
                    static = True
                elif cell == "-":
                    dr = random.choice((l, r))
                    static = True
                else:
                    dr = random.choice((l, r, u, d))
                    static = False
                left = (cnv_width - (self.width * img_px)) // 2 + (ic * img_px)
                top = (cnv_height - (5 * img_px)) // 2 + (ir * img_px)
                tgtlft = 50 + (strtpos + ic) * 40
                tgttop = 50 + (250 * self.irow) + (ir * 40)
                lftdx = (left - tgtlft) / 30
                topdx = (top - tgttop) / 30
                self.car_ar.append(Car(left, top, dr, static, lftdx, topdx))

    def shift(self, fid):
        for car in self.car_ar:
            car.shift(fid)

    def add_img(self, bg):
        for car in self.car_ar:
            bg.paste(car.img, (int(car.left), int(car.top)), car.img)


def draw_img(ltr_ar, fid):
    bg = Image.new('RGB', (1600, 900), (255, 255, 255))
    for i, ltr in enumerate(ltr_ar):
        ltr_strt = (i * 45)
        if ltr_strt < fid:
            ltr.shift(fid - ltr_strt)
            ltr.add_img(bg)
    bg.save('out_frames/out_%03d.png' % fid)


def get_text_map():
    ar = []
    i = 1
    with open('text_map.csv') as f:
        for ln in [x.strip().rstrip(',') for x in f.readlines() if x.strip().strip(',')]:
            pts = [[x.split(',')] for x in (ln + ',').split(',x,')[:-1]]
            if i % 5 == 1:
                curpts = pts
            else:
                for j, v in enumerate(pts):
                    curpts[j].extend(v)
            if i % 5 == 0:
                i = 0
                ar.append(curpts)
            i += 1
    return ar


ar = []
txt_map = get_text_map()
for irow, ln in enumerate(txt_map):
    strtpos = 0
    for icol, ltr in enumerate(ln):
        width = len(ltr[0])
        ar.append(Letter(irow, icol, strtpos, width, ltr))
        strtpos += width + 1

for fid in range(900):
    print(fid)
    draw_img(ar, fid)

clip = ImageSequenceClip(sorted(glob.glob('out_frames/*.*')), fps=20)
clip.write_videofile('out.mp4')

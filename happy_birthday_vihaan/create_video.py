from PIL import Image
import glob
import random
from moviepy.editor import *

car_lst = list(glob.glob('car_img/*.*'))

l,r,u,d = "left right up down".split()

class Car:
    def __init__(self,ix,iy,dr,static):
        self.left = 80 + (ix*40)
        self.top = 70 + (iy*40)
        self.ix = ix
        self.iy = iy
        self.dr = dr
        self.fl = random.choice(car_lst)
        self.img = Image.open(self.fl)
        if dr == d:
            self.img = self.img.transpose(Image.ROTATE_90)
        elif dr == r:
            self.img = self.img.transpose(Image.ROTATE_180)
            self.img = self.img.transpose(Image.FLIP_TOP_BOTTOM)
        elif dr == u:
            self.img = self.img.transpose(Image.ROTATE_270)
        self.start = random.choice((5,40))
        self.speed = random.choice((8,18))
        self.static = static

    def shift(self, fid):
        if self.static or fid < self.start:
            return
        elif self.dr == d:
            self.top += self.speed
        elif self.dr == u:
            self.top -= self.speed
        elif self.dr == l:
            self.left -= self.speed
        elif self.dr == r:
            self.left += self.speed

def draw_img(car_ar,fid):
    bg = Image.new('RGB',(1600,900),(255,255,255))
    for car in car_ar:
        car.shift(fid)
        bg.paste(car.img,(car.left,car.top),car.img)
    bg.save('out_frames/out_%03d.png' % fid)

def get_text_map():
    with open('text_map.csv') as f:
        return [x.strip().split(',') for x in f.readlines() if x.strip()]

txt_map = get_text_map()
car_ar = []
for ir, row in enumerate(txt_map):
    for ic, cell in enumerate(row):
        if cell == "|":
            dr = random.choice((u,d))
            static = True
        elif cell == "-":
            dr = random.choice((l,r))
            static = True
        else:
            dr = random.choice((l,r,u,d))
            static = False
        car_ar.append(Car(ic,ir,dr,static))

for fid in range(300):
    print(fid)
    draw_img(car_ar,fid)

clip = ImageSequenceClip(sorted(glob.glob('out_frames/*.*')),fps=10)
clip.write_videofile('out.mp4')
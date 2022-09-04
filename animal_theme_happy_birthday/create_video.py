from PIL import Image, ImageDraw, ImageOps, ImageFont
import glob
import random
from moviepy.editor import *
import math

person_name = 'Abcdef'


def rotate_point(x, y, degrees, shftx, shfty):
    angle = math.radians(degrees)
    qx = (math.cos(angle) * x) - (math.sin(angle) * y)
    qy = (math.sin(angle) * x) + (math.cos(angle) * y)
    return qx + shftx, shfty - qy


class Wheel:
    def __init__(self):
        self.inner_radius = 40
        self.outer_radius = 50
        self.image_length = (self.outer_radius * 2) + 10
        self.wheel_color = (255, 255, 0)
        self.wheel_width = self.outer_radius - self.inner_radius
        self.spoke_width = 10
        self.angle = random.randint(0, 360)
        self.img = None
        self.recreate_image()
        self.speed = 6

    def recreate_image(self):
        self.img = Image.new('RGBA', (self.image_length, self.image_length))
        draw = ImageDraw.Draw(self.img)
        draw.ellipse((5, 5, self.image_length - 5, self.image_length - 5), fill=self.wheel_color,
                     outline=self.wheel_color)
        mask_img = Image.new('L', (self.image_length, self.image_length), 0)
        mask_draw = ImageDraw.Draw(mask_img)
        delta = 5 + self.wheel_width
        mask_draw.ellipse((5, 5, self.image_length - 5, self.image_length - 5), fill=255)
        mask_draw.ellipse((delta, delta, self.image_length - delta, self.image_length - delta), fill=0)

        x1, y1 = rotate_point(-self.inner_radius, 0, self.angle, self.image_length / 2, self.image_length / 2)
        x2, y2 = rotate_point(self.inner_radius, 0, self.angle, self.image_length / 2, self.image_length / 2)
        mask_draw.line((x1, y1, x2, y2), fill=255, width=self.spoke_width)
        x1, y1 = rotate_point(-self.inner_radius, 0, self.angle + 90, self.image_length / 2, self.image_length / 2)
        x2, y2 = rotate_point(self.inner_radius, 0, self.angle + 90, self.image_length / 2, self.image_length / 2)
        mask_draw.line((x1, y1, x2, y2), fill=255, width=self.spoke_width)
        self.img.putalpha(mask_img)

    def shift(self):
        self.angle = (self.angle - self.speed) % 360
        self.recreate_image()


class Engine:
    def __init__(self, left, top):
        self.width = 470
        self.height = 600
        self.engine = Image.open('engine.png')
        self.engine_height, self.engine_width = self.engine.size
        self.whl1 = Wheel()
        self.whl2 = Wheel()
        self.left = left
        self.top = top
        self.speed = 10
        self.img = None
        self.recreate_image()

    def recreate_image(self):
        self.img = Image.new('RGBA', (self.width, self.height))
        self.img.paste(self.engine, (0, self.height - (self.engine_height - 45)), self.engine)
        self.img.paste(self.whl1.img, (50, self.height - 110), self.whl1.img)
        self.img.paste(self.whl2.img, (self.engine_width - 60, self.height - 110), self.whl2.img)

    def shift(self):
        self.left += self.speed
        self.whl1.shift()
        self.whl2.shift()
        self.recreate_image()


class Trolley:
    def __init__(self, left, top, color, animal):
        self.width = 800
        self.height = 600
        self.trolley_height = 150
        self.trolley_width = 700
        self.connector_width = self.width - self.trolley_width
        self.trolley_color = color
        self.whl1 = Wheel()
        self.whl2 = Wheel()
        self.left = left
        self.top = top
        self.speed = 10
        self.img = None
        self.animal_width = 400
        self.animal = Image.open('animals/%s.png' % animal)
        w, h = self.animal.size
        factor = 400 / w
        self.animal = self.animal.resize((int(w * factor), int(h * factor)))
        w, h = self.animal.size
        self.animal_top = self.height - (self.trolley_height + 5 + h)
        self.recreate_image()

    def recreate_image(self):
        self.img = Image.new('RGBA', (self.width, self.height))
        self.img.paste(self.animal, (0, self.animal_top), self.animal)
        draw = ImageDraw.Draw(self.img)
        draw.rectangle((0, self.height - self.trolley_height - 55, self.trolley_width, self.height - 55),
                       fill=self.trolley_color)
        self.img.paste(self.whl1.img, (50, self.height - 110), self.whl1.img)
        self.img.paste(self.whl2.img, (self.trolley_width - 160, self.height - 110), self.whl2.img)
        draw.rectangle((self.trolley_width, self.height - 90, self.width, self.height - 70), fill=(0, 0, 0))

    def shift(self):
        self.left += self.speed
        self.whl1.shift()
        self.whl2.shift()
        self.recreate_image()


class Gift:
    def __init__(self, color, gift, left, top):
        self.color = color
        self.left = left
        self.top = top
        self.gift = Image.open('gifts/%s.png' % gift)
        self.width = 400
        self.height = 600
        self.box_height = 150
        self.box_width = 200
        self.box_top = self.height - self.box_height
        self.angle = 0
        self.fid = 0
        self.img = None
        self.speed = 7
        self.zoom_factor = 10
        self.mode = 'move up'
        self.font = ImageFont.truetype(r'C:\Windows\Fonts\verdana.ttf', size=36)
        self.gift_top = None
        self.gift_img = None
        self.gift_img_top = None
        self.gift_img_left = None
        self.gift_width = 150

    def recreate_image(self):
        self.img = Image.new('RGBA', (self.width, self.height))
        if self.mode == 'pop out':
            gift_img = ImageOps.pad(self.gift, (150, 150))
            self.img.paste(gift_img, (25, self.gift_top), gift_img)
        draw = ImageDraw.Draw(self.img)
        draw.rectangle((0, self.box_top, self.box_width, self.box_top + self.box_height), fill=self.color)
        draw.text((100, self.box_top + 75), person_name, font=self.font, anchor="mm", fill=(0, 0, 0))
        x1, y1 = rotate_point(-200, 0, self.angle, 200, self.box_top)
        x2, y2 = (200, self.box_top)
        draw.line((x1, y1, x2, y2), fill=self.color, width=30)

    def shift(self):
        if self.mode == 'move up' and self.fid > 5:
            self.box_top -= self.speed
        elif self.mode == 'open box' and self.fid > 30:
            self.angle -= self.speed
            self.gift_top = self.box_top
        elif self.mode == 'pop out' and self.fid > 55:
            self.gift_top -= self.speed
        self.recreate_image()
        self.fid += 1
        if self.mode == 'move up' and self.fid > 25:
            self.mode = 'open box'
        elif self.mode == 'open box' and self.fid > 50:
            self.mode = 'pop out'

    def set_zoom(self):
        self.mode = 'Zoom In'
        self.recreate_image()
        self.gift_img_top = self.top + self.gift_top
        self.gift_img_left = self.left + 25
        self.fid = 1

    def zoom_img(self):
        if self.fid < 20:
            self.gift_img_top -= self.zoom_factor
            self.gift_img_left -= self.zoom_factor
            self.gift_width += self.zoom_factor
            self.gift_img = Image.new('RGBA', (self.gift_width, self.gift_width))
            gift_img = ImageOps.pad(self.gift, (self.gift_width, self.gift_width))
            self.gift_img.paste(gift_img, (0, 0), gift_img)
        self.fid += 1


def draw_train(bg, shift=False):
    if shift == True:
        engine.shift()
    if -800 <= engine.left <= 2200:
        bg.paste(engine.img, (engine.left, engine.top), engine.img)
    for t in t_ar:
        if shift == True:
            t.shift()
        if -800 <= t.left <= 2200:
            bg.paste(t.img, (t.left, t.top), t.img)


base_img = Image.open('base_img.jpg')
t_ar = []
gift_ar = []
clr_ar = [(255, 140, 0), (102, 205, 170), (123, 104, 238), (255, 105, 180), (176, 196, 222)]
animal_ar = ('elephant', 'duck', 'giraffe', 'penguin', 'panda')
gft_lst = ('teddy_bear', 'barbie', 'chocolate', 'cake', 'ball')
engine = Engine(-470, 250)
left = -470 - 800
for i in range(5):
    t_ar.append(Trolley(left, 250, clr_ar[i], animal_ar[i]))
    gift_ar.append(Gift(clr_ar[i], gft_lst[i], 725, 195))
    left -= 800

i = 0
cur_idx = 0
for j in range(600):
    print('processing frame ', i)
    if cur_idx < len(t_ar) and t_ar[cur_idx].left > 325:
        g = gift_ar[cur_idx]
        for k in range(95):
            print('processing frame ', i)
            g.shift()
            bg = base_img.copy()
            bg.paste(g.img, (g.left, g.top), g.img)
            draw_train(bg, False)
            bg.save('out_frames/img_%04d.png' % i)
            i += 1
        g.set_zoom()
        for k in range(30):
            print('processing frame ', i)
            g.zoom_img()
            bg = base_img.copy()
            bg.paste(g.img, (g.left, g.top), g.img)
            draw_train(bg, False)
            bg.paste(g.gift_img, (g.gift_img_left, g.gift_img_top), g.gift_img)
            bg.save('out_frames/img_%04d.png' % i)
            i += 1
        cur_idx += 1
    bg = base_img.copy()
    draw_train(bg, True)
    bg.save('out_frames/img_%04d.png' % i)
    i += 1

clip = ImageSequenceClip(sorted(glob.glob('out_frames/*.*')), fps=20)
clip.write_videofile('out.mp4')

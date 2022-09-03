from PIL import Image, ImageDraw
import glob
import random
from moviepy.editor import *
import math


def rotate_point(x, y, degrees, shftx, shfty):
    angle = math.radians(degrees)
    qx = (math.cos(angle) * x) - (math.sin(angle) * y)
    qy = (math.sin(angle) * x) + (math.cos(angle) * y)
    return qx + shftx, shfty - qy


class Wheel:
    def __init__(self):
        self.inner_radius = 80
        self.outer_radius = 100
        self.image_length = (self.outer_radius * 2) + 10
        self.wheel_color = (255, 255, 0)
        self.wheel_width = self.outer_radius - self.inner_radius
        self.spoke_width = 10
        self.angle = random.randint(0, 360)
        self.img = None
        self.recreate_image()
        self.speed = 5

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
        x1, y1 = rotate_point(-self.inner_radius, 0, self.angle+90, self.image_length / 2, self.image_length / 2)
        x2, y2 = rotate_point(self.inner_radius, 0, self.angle+90, self.image_length / 2, self.image_length / 2)
        mask_draw.line((x1, y1, x2, y2), fill=255, width=self.spoke_width)
        self.img.putalpha(mask_img)

    def shift(self):
        self.angle = ( self.angle + self.speed ) % 360

whl = Wheel()
for i in range(300):
    bg = Image.new('RGB', (1600, 900), (255, 255, 255))
    whl.shift()
    bg.paste(whl.img, (300, 300), whl.img)
    bg.save('out_frames/img_%03d.png' % i)

clip = ImageSequenceClip(sorted(glob.glob('out_frames/*.*')), fps=20)
clip.write_videofile('out.mp4')

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
        x1, y1 = rotate_point(-self.inner_radius, 0, self.angle+90, self.image_length / 2, self.image_length / 2)
        x2, y2 = rotate_point(self.inner_radius, 0, self.angle+90, self.image_length / 2, self.image_length / 2)
        mask_draw.line((x1, y1, x2, y2), fill=255, width=self.spoke_width)
        self.img.putalpha(mask_img)

    def shift(self):
        self.angle = ( self.angle - self.speed ) % 360
        self.recreate_image()

class Engine:
    def __init__(self,left,top):
        self.width=470
        self.height=600
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
        self.img = Image.new('RGBA',(self.width,self.height))
        self.img.paste(self.engine,(0,self.height - (self.engine_height - 45)),self.engine)
        self.img.paste(self.whl1.img,(50,self.height-110),self.whl1.img)
        self.img.paste(self.whl2.img,(self.engine_width-60,self.height-110),self.whl2.img)

    def shift(self):
        self.left += self.speed
        self.whl1.shift()
        self.whl2.shift()
        self.recreate_image()

class Trolley:
    def __init__(self,left,top,color,animal):
        self.width=800
        self.height=600
        self.trolley_height=150
        self.trolley_width=700
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
        w,h = self.animal.size
        factor = 400/w
        self.animal = self.animal.resize((int(w*factor),int(h*factor)))
        w,h = self.animal.size
        self.animal_top = self.height - (self.trolley_height + 5 + h)
        self.recreate_image()

    def recreate_image(self):
        self.img = Image.new('RGBA',(self.width,self.height))
        self.img.paste(self.animal,(0,self.animal_top),self.animal)
        draw = ImageDraw.Draw(self.img)
        draw.rectangle((0,self.height-self.trolley_height-55,self.trolley_width,self.height-55),fill=self.trolley_color)
        self.img.paste(self.whl1.img,(50,self.height-110),self.whl1.img)
        self.img.paste(self.whl2.img,(self.trolley_width-160,self.height-110),self.whl2.img)
        draw.rectangle((self.trolley_width,self.height-90,self.width,self.height-70),fill=(0,0,0))

    def shift(self):
        self.left += self.speed
        self.whl1.shift()
        self.whl2.shift()
        self.recreate_image()

t_ar = []
clr_ar = [(255,140,0),(102,205,170),(123,104,238),(255,105,180),(176,196,222)]
animal_ar = ('elephant','duck','giraffe','penguin','panda')
engine=Engine(-470,250)
left = -470 - 800
for i in range(5):
    t_ar.append(Trolley(left,250,clr_ar[i],animal_ar[i]))
    left -= 800

for i in range(500):
    print('processing frame ',i)
    bg = Image.open('base_img.jpg')
    engine.shift()
    bg.paste(engine.img, (engine.left, engine.top), engine.img)
    for t in t_ar:
        t.shift()
        bg.paste(t.img, (t.left, t.top), t.img)
    bg.save('out_frames/img_%03d.png' % i)

clip = ImageSequenceClip(sorted(glob.glob('out_frames/*.*')), fps=20)
clip.write_videofile('out.mp4')

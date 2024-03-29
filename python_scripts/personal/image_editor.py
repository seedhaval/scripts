import random
from tkinter import *
from tkinter import filedialog
from typing import List
from PIL import Image, ImageTk, ImageEnhance
from math import sqrt
from math import atan2, degrees
from pathlib import Path
import os

if os.name == 'nt':
    w = 500
    h = 700
    base_fldr = [
        r"D:\Documents\Python create puzzles\2_digit_addition\images",
        r"D:\Documents\Python create "
        r"puzzles\draw_beads_on_abacus_for_2_digit_number\worksheet_images"
    ]
    cnvw = w - 20
    cnvh = h - 100
else:
    w = 1050
    h = 1950
    base_fldr = [
        "../tmp/img1",
        "../tmp/img2",
    ]
    cnvw = w - 40
    cnvh = h - 100

actions = ["move", "rotate", "scale", "contrast", "brightness", "flip H",
           "flip V", "random", "crop", "swap", "add frame", "animate",
           "reset animation"]

img = {}
pt_ar = []
img_ar = []
curi = 0
delay = 500
cnv_img = None


def angle_between(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    deg1 = (360 + degrees(atan2(x1 - x2, y1 - y2))) % 360
    deg2 = (360 + degrees(atan2(x3 - x2, y3 - y2))) % 360
    return deg2 - deg1 if deg1 <= deg2 else 360 - (deg1 - deg2)


def get_distance(p1: List[int], p2: List[int]):
    x1, y1 = p1
    x2, y2 = p2
    return sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))


def refresh_canvas():
    global cnv_img
    base_img = Image.new('RGBA', (cnvw, cnvh), (255, 255, 255, 255))
    for k in sorted(img.keys()):
        imgnew = img[k]['refobj'].copy().convert('RGBA')
        if len(img[k]['crop']) > 0:
            imgnew = imgnew.crop(tuple(img[k]['crop']))
        imgw = int(imgnew.size[0] * img[k]['scale'])
        imgh = int(imgnew.size[1] * img[k]['scale'])
        imgnew = imgnew.resize((imgw, imgh))
        if img[k]['fliph'] == True:
            imgnew = imgnew.transpose(Image.FLIP_LEFT_RIGHT)
        if img[k]['flipv'] == True:
            imgnew = imgnew.transpose(Image.FLIP_TOP_BOTTOM)
        imgnew = ImageEnhance.Brightness(imgnew).enhance(img[k]['brightness'])
        imgnew = ImageEnhance.Contrast(imgnew).enhance(img[k]['contrast'])
        imgnew = imgnew.rotate(img[k]['rotate'], expand=True)
        base_img.paste(imgnew, (img[k]['left'], img[k]['top']), imgnew)
    cnv_img = ImageTk.PhotoImage(base_img.convert("RGB"))
    cnv.set_image(cnv_img)


def load_img(imgfl):
    key = int(layer.get()) - 1
    img[key] = {'refobj': Image.open(imgfl), 'contrast': 1.0, 'brightness':
        1.0, 'rotate': 0, 'top': 1, 'left': 1, 'fliph': False, 'flipv':
                    False, "crop": []}
    img[key]['width'], img[key]['height'] = img[key]['refobj'].size
    rx = cnvw * 1.00 / img[key]['width']
    ry = cnvh * 1.00 / img[key]['height']
    img[key]['scale'] = min(rx, ry)
    refresh_canvas()


def selectFile(*args, **kwargs):
    fldr = base_fldr[int(layer.get()) - 1]
    fl = filedialog.askopenfilename(initialdir=fldr)
    if fl:
        load_img(fl)


def pos(elm, pos_ar: List[int]):
    row, col, rowspan, colspan = pos_ar
    elm.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, padx=5,
             pady=5)


class MyLabel:
    def __init__(self, prnt, text: str, width: int, height: int,
                 pos_ar: List[int]):
        self.prnt = prnt
        self.var: StringVar = StringVar()
        self.elm = Label(self.prnt, textvariable=self.var)
        self.var.set(text)
        self.elm.config(width=width)
        self.elm.config(height=height)
        pos(self.elm, pos_ar)

    def set(self, text):
        self.var.set(text)

    def set_font_size(self, sz: int):
        self.elm.config(font=("Roboto", sz))


class MyButton:
    def __init__(self, prnt, text: str, cb, pos_ar: List[int]):
        self.prnt = prnt
        self.elm = Button(self.prnt, text=text, command=cb)
        pos(self.elm, pos_ar)


class MyDropDown:
    def __init__(self, prnt, ar: List[str], pos_ar: List[int]):
        self.prnt = prnt
        self.var = StringVar()
        self.var.set(ar[0])
        self.elm = OptionMenu(self.prnt, self.var, *ar)
        pos(self.elm, pos_ar)

    def get(self):
        return self.var.get()

    def set(self, val: str):
        self.var.set(val)


class MyCanvas:
    def __init__(self, prnt, width: int, height: int, pos_ar: List[int]):
        self.prnt = prnt
        self.height = height
        self.width = width
        self.elm: Canvas = Canvas(prnt, height=height, width=width)
        self.imgtk = None
        pos(self.elm, pos_ar)
        self.cb = None

    def set_callback(self, cb):
        self.cb = cb
        self.elm.bind('<Button-1>', self.cb)

    def set_image(self, imgtk):
        self.imgtk = imgtk
        self.elm.create_image(self.width, self.height, image=imgtk, anchor=SE)


class MyFrame:
    def __init__(self, prnt, title: str, width: int, height: int,
                 pos_ar: List[int]):
        self.elm: LabelFrame = LabelFrame(prnt, text=title)
        self.elm.config(width=width)
        self.elm.config(height=height)
        self.elm.grid_propagate(False)
        pos(self.elm, pos_ar)
        self.children = {}

    def add_label(self, nm: str, text: str, width: int, height: int,
                  pos_ar: List[int]) -> MyLabel:
        self.children[nm]: MyLabel = MyLabel(self.elm, text, width, height,
                                             pos_ar)
        return self.children[nm]

    def add_dropdown(self, nm: str, ar: List[str],
                     pos_ar: List[int]) -> MyDropDown:
        self.children[nm]: MyDropDown = MyDropDown(self.elm, ar, pos_ar)
        return self.children[nm]

    def add_button(self, nm: str, text: str, cb, pos_ar: List[int]) -> MyButton:
        self.children[nm]: MyButton = MyButton(self.elm, text, cb, pos_ar)
        return self.children[nm]

    def add_canvas(self, nm: str, width: int, height: int,
                   pos_ar: List[int]) -> MyCanvas:
        self.children[nm]: MyCanvas = MyCanvas(self.elm, width, height, pos_ar)
        return self.children[nm]


def add_frame(self, title: str, width: int, height: int,
              pos_ar: List[int]):
    self.children['title'] = MyFrame(self.elm, title, width, height, pos_ar)
    return self.children['title']


class MyApp:
    def __init__(self, title: str, width: int, height: int):
        self.top = Tk()
        self.top.title(title)
        self.top.grid_propagate(False)
        self.top.geometry(f'{width}x{height}+10+10')
        self.children = {}

    def add_frame(self, title: str, width: int, height: int,
                  pos_ar: list[int]) -> MyFrame:
        self.children['title'] = MyFrame(self.top, title, width, height, pos_ar)
        return self.children['title']

    def show(self):
        self.top.mainloop()


def handle_click(event):
    global pt_ar
    pt_ar.append([event.x, event.y])
    key = int(layer.get()) - 1
    if action.get() == "move" and len(pt_ar) == 2:
        img[key]['left'] += pt_ar[1][0] - pt_ar[0][0]
        img[key]['top'] += pt_ar[1][1] - pt_ar[0][1]
        pt_ar = []
        refresh_canvas()
    elif action.get() == "scale" and len(pt_ar) == 3:
        s = get_distance(pt_ar[0], pt_ar[2]) / get_distance(pt_ar[0], pt_ar[1])
        img[key]['scale'] *= s
        pt_ar = []
        refresh_canvas()
    elif action.get() == "brightness" and len(pt_ar) == 3:
        s = get_distance(pt_ar[0], pt_ar[2]) / get_distance(pt_ar[0], pt_ar[1])
        img[key]['brightness'] *= s
        pt_ar = []
        refresh_canvas()
    elif action.get() == "contrast" and len(pt_ar) == 3:
        s = get_distance(pt_ar[0], pt_ar[2]) / get_distance(pt_ar[0], pt_ar[1])
        img[key]['contrast'] *= s
        pt_ar = []
        refresh_canvas()
    elif action.get() == 'flip H':
        img[key]['fliph'] = not img[key]['fliph']
        pt_ar = []
        refresh_canvas()
    elif action.get() == 'flip V':
        img[key]['flipv'] = not img[key]['flipv']
        pt_ar = []
        refresh_canvas()
    elif action.get() == "rotate" and len(pt_ar) == 3:
        s = angle_between(*pt_ar)
        img[key]['rotate'] = (img[key]['rotate'] + s)
        pt_ar = []
        refresh_canvas()
    elif action.get() == "random":
        load_img(random.choice(list(Path(base_fldr[1]).glob('*.*'))))
        pt_ar = []
    elif action.get() == "swap":
        img[0], img[1] = img[1], img[0]
        refresh_canvas()
        pt_ar = []
    elif action.get() == "crop" and len(pt_ar) == 2:
        x1, y1 = pt_ar[0]
        x2, y2 = pt_ar[1]
        x1, x2 = [x - img[key]['left'] for x in (x1, x2)]
        y1, y2 = [y - img[key]['top'] for y in (y1, y2)]
        x1, y1, x2, y2 = [int(x * 1.0 / img[key]['scale']) for x in (x1, y1,
                                                                     x2, y2)]
        img[key]['crop'] = [x1, y1, x2, y2]
        refresh_canvas()
        pt_ar = []
    elif action.get() == "add frame":
        img_ar.append(cnv_img)
        pt_ar = []
    elif action.get() == "animate":
        pt_ar = []
        curi = -1
        animate()
    elif action.get() == "reset animation":
        pt_ar = []
        img_ar.clear()


def animate():
    global curi
    if len(img_ar) > 0:
        curi = (curi + 1) % (len(img_ar))
        cnv.set_image(img_ar[curi])
        app.top.after(delay, animate)


app = MyApp("Image Editor", w, h)
frm: MyFrame = app.add_frame("Image Editor", w - 10, h - 10,
                             [1, 1, 1, 1])
layer: MyDropDown = frm.add_dropdown("layer", '1 2 3 4'.split(),
                                     [1, 1, 1, 1])
selfile: MyButton = frm.add_button("selfile", "...", selectFile,
                                   [1, 2, 1, 1])
action: MyDropDown = frm.add_dropdown("action", actions, [1, 3, 1, 1])
cnv: MyCanvas = frm.add_canvas("cnv", cnvw, cnvh, [2, 1, 1, 3])
cnv.set_callback(handle_click)
app.show()

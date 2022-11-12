import tkinter as tk
import core
import os
import pathlib
import random

if os.name == 'nt':
    w = 500
    h = 700
    base_fldr = r"D:\Documents\Python create puzzles\2_digit_addition\images"
    cnvw = w - 40
    cnvh = int(h * 0.6)
else:
    w = 1050
    h = 1950
    base_fldr = "../tmp/img/"
    cnvw = w - 40
    cnvh = int(h * 0.6)


def handle_click(x: int, y: int):
    if not gd.cur_sec.point_exists(x,y):
        return
    act.lblltxt.set(gd.cur_act.event)
    act.lblverb.elm['text'] = gd.cur_act.verb


def refresh_file(*args, **kwargs):
    fl = random.choice(list(pathlib.Path(base_fldr).glob('*.*')))
    gd.file = pathlib.Path(fl).name
    photo.load_file(str(fl))
    gd.get_one_due_action()
    photo.update_sections([gd.cur_sec])


gd = core.GameData()
app = core.MyApp("Action Game", w, h)
frmFileSel: core.MyFrame = app.add_frame("Photo", w - 10, int(h * 0.1),
                                         [1, 1, 1, 1])
selfile: core.MyButton = frmFileSel.add_button("selfile", "...", refresh_file,
                                               [1, 1, 1, 1])
frmAction: core.MyFrame = app.add_frame("Action", w - 10, int(h * 0.2),
                                        [2, 1, 1, 1])
frmCnv: core.MyFrame = app.add_frame("Image", w - 10, int(h * 0.65),
                                     [3, 1, 1, 1])
cnv: core.MyCanvas = frmCnv.add_canvas("cnv", cnvw, cnvh, [1, 1, 1, 1])
photo = core.Photo(cnv, handle_click, cnvw, cnvh)
act = core.DoAction(gd, frmAction, refresh_file)
app.show()

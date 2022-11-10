import tkinter as tk
import core
import os
from tkinter import filedialog
import pathlib
import random

if os.name == 'nt':
    w = 500
    h = 700
    base_fldr = [r"D:\Documents\Python create puzzles\2_digit_addition\images"]
    cnvw = w - 40
    cnvh = int(h * 0.6)
else:
    w = 1050
    h = 1950
    base_fldr = random.choice(["../DCIM/Restored/","../tmp/img/"])
    cnvw = w - 40
    cnvh = int(h * 0.6)

def handle_click(x: int, y: int):
    if not gd.cur_sec.x1 < x < gd.cur_sec.x2:
        return
    if not gd.cur_sec.y1 < y < gd.cur_sec.y2:
        return
    a = gd.action_data.actions[gd.cur_act_idx]
    act.lblltxt.set(a.event)
    act.lblverb.elm['text'] = a.verb
    
    
def refresh_file():    
    gd.cur_act_idx, gd.cur_sec = gd.action_data.get_one_due(gd.section_data.get_s_dict(gd.file))
    photo.update_sections([gd.cur_sec])
    
    
    
def selectFile(*args, **kwargs):
    #fl = filedialog.askopenfilename(initialdir=base_fldr)
    fl = random.choice(list(pathlib.Path(base_fldr).glob('*.*')))
    if fl:
        gd.set_img_file(pathlib.Path(fl).name)
        photo.load_file(fl)
        refresh_file()
        
        
gd = core.GameData()
app = core.MyApp("Action Game", w, h)
frmFileSel: core.MyFrame = app.add_frame("Photo", w - 10, int(h * 0.1),
                             [1, 1, 1, 1])
selfile: core.MyButton = frmFileSel.add_button("selfile", "...", selectFile,
                                   [1, 1, 1, 1])
frmAction: core.MyFrame = app.add_frame("Action", w - 10, int(h * 0.2),
                             [2, 1, 1, 1])
frmCnv: core.MyFrame = app.add_frame("Image", w - 10, int(h * 0.65),
                             [3, 1, 1, 1])
cnv: core.MyCanvas = frmCnv.add_canvas("cnv", cnvw, cnvh, [1, 1, 1, 1])
photo = core.Photo(cnv, handle_click, cnvw, cnvh)
act = core.DoAction(gd,frmAction,refresh_file)
app.show()

import pathlib
import tkinter as tk
from tkinter import filedialog

import core
import os

if os.name == 'nt':
    w = 500
    h = 700
    base_fldr = r"D:\Documents\Python create puzzles\2_digit_addition\images"
    cnvw = w - 40
    cnvh = int(h * 0.6)
else:
    w = 1050
    h = 1950
    base_fldr = "../DCIM/Restored/",
    cnvw = w - 40
    cnvh = int(h * 0.6)


def selectFile(*args, **kwargs):
    fl = filedialog.askopenfilename(initialdir=base_fldr)
    if fl:
        gd.set_img_file(pathlib.Path(fl).name)
        photo.load_file(fl)
        photo.update_sections(gd.section_data.get_sections_for_file(gd.file))
        


def handle_click(x: int, y: int):
    global pt_ar
    pt_ar.append([x, y])
    if len(pt_ar) == 1:
        photo.update_sections(gd.section_data.get_sections_for_file(gd.file))
    elif len(pt_ar) == 2:
        section_ar = [x for x in photo.section_ar]
        x1,y1 = [str(x) for x in pt_ar[0]]
        x2, y2 = [str(x) for x in pt_ar[1]]
        section_ar.append(core.Section(['','','',x1,y1,x2,y2]))
        gd.cur_ar = [x for x in pt_ar]
        pt_ar = []
        photo.update_sections(section_ar)


pt_ar = []
gd = core.GameData()
app = core.MyApp("Edit Section", w, h)
frmFileSel: core.MyFrame = app.add_frame("Photo", w - 10, int(h * 0.1),
                                         [1, 1, 1, 1])
selfile: core.MyButton = frmFileSel.add_button("selfile", "...", selectFile,
                                               [1, 1, 1, 1])
frmSection: core.MyFrame = app.add_frame("Edit Section", w - 10, int(h * 0.2),
                                         [2, 1, 1, 1])
frmCnv: core.MyFrame = app.add_frame("Image", w - 10, int(h * 0.65),
                                     [3, 1, 1, 1])
cnv: core.MyCanvas = frmCnv.add_canvas("cnv", cnvw, cnvh, [1, 1, 1, 1])
photo = core.Photo(cnv, handle_click, cnvw, cnvh)
editsection = core.EditSection(frmSection, gd)
app.show()

import tkinter as tk
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
    base_fldr = "../tmp/img1",
    cnvw = w - 40
    cnvh = int(h * 0.6)

app = core.MyApp("Edit Section", w, h)
frmFileSel: core.MyFrame = app.add_frame("Photo", w - 10, int(h * 0.1),
                             [1, 1, 1, 1])
selfile: core.MyButton = frmFileSel.add_button("selfile", "...", None,
                                   [1, 1, 1, 1])
frmAction: core.MyFrame = app.add_frame("Edit Section", w - 10, int(h * 0.2),
                             [2, 1, 1, 1])
frmCnv: core.MyFrame = app.add_frame("Image", w - 10, int(h * 0.65),
                             [3, 1, 1, 1])
cnv: core.MyCanvas = frmCnv.add_canvas("cnv", cnvw, cnvh, [1, 1, 1, 1])
cnv.set_callback(None)
app.show()

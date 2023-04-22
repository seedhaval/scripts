import os
from tkinter import *
from PIL import Image, ImageTk
from textwrap import fill

w, h = (500, 700)
lw, lh = (40, 5)


# w,h = (1050,1950)


def next_cmd():
    typ, fl, tm, txt = scene_ar.pop()
    if typ == "b":
        fldr = bg_fldr
    elif typ == "h":
        fldr = hmn_fldr
    img1 = Image.open(f"{fldr}/{fl}.txt")
    itk = ImageTk.PhotoImage(img1)
    lblimg.configure(image=itk)
    lblimg.image = itk
    lbltxt.configure(text=fill(txt, width=lw))
    if len(scene_ar) > 0:
        top.after(int(tm) * 1000, next_cmd)
    else:
        top.after(int(tm) * 1000, exit)


schema_file = "D:/data/.schema"
with open(schema_file) as f:
    schema = f.read().strip()
with open(schema_file, 'w') as f:
    f.write('scheme')

bg_fldr = "D:/data/back"
hmn_fldr = f"D:/data/{schema}"
if not os.path.exists(hmn_fldr):
    exit()

scene_txt_file = "D:/data/scene.txt"

with open(scene_txt_file) as f:
    scene_ar = [x.strip().split(",") for x in f.readlines() if x.strip()][::-1]

top = Tk()
top.grid_propagate(False)
top.option_add("*font", "verdana 16")
top.geometry(f'{w}x{h}+10+10')
lblimg = Label(width=w, height=int(h * 0.75))
lblimg.place(x=1, y=1)
lbltxt = Label(width=lw, height=lh)
lbltxt.place(x=1, y=int(h * 0.75))
top.after(5000, next_cmd)
top.mainloop()

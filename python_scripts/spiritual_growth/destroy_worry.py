from tkinter import *
from PIL import Image, ImageDraw, ImageTk, ImageFont
import textwrap
import random

imgtk = None
img_size = (1100, 550)
mask_img = Image.new("L", img_size, 255)
mask_draw = ImageDraw.Draw(mask_img)
base_img = Image.new('RGBA', img_size, (255, 255, 255, 255))
base_draw = ImageDraw.Draw(base_img)


def pos(elm, pos_ar: list[int]):
    row, col, rowspan, colspan = pos_ar
    elm.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, padx=5, pady=5)


def show_img():
    global imgtk

    txtval = txt.get(1.0, "end-1c")
    font = ImageFont.truetype('arial', size=72)
    offset = 50
    for ln in textwrap.wrap(txtval, width=25):
        base_draw.text((100, offset), ln, fill="black", align="center", font=font)
        offset += font.getsize(ln)[1] + 20
    imgtk = ImageTk.PhotoImage(base_img)
    cnv.create_image(1100, 550, image=imgtk, anchor=SE)


def cut_circle(event):
    x, y = event.x, event.y
    global imgtk
    r = random.randint(20, 40)
    mask_draw.ellipse((x - r, y - r, x + r, y + r), fill=0)
    base_img.putalpha(mask_img)
    imgtk = ImageTk.PhotoImage(base_img)
    cnv.create_image(1100, 550, image=imgtk, anchor=SE)


top = Tk()
top.title("Destroy Worry")
top.geometry(f'1200x700+10+10')
lbl = Label(top, text="What are you worried about ?", font=("Arial", 18))
pos(lbl, [1, 1, 1, 1])
txt = Text(top, height=1, width=65, font=("Arial", 18))
pos(txt, [1, 2, 1, 1])
btn = Button(top, text="Start destroying worry", command=show_img, font=("Arial", 18))
pos(btn, [2, 1, 1, 2])
cnv = Canvas(top, width=1100, height=550)
cnv.bind("<Button-1>", cut_circle)
pos(cnv, [3, 1, 1, 2])

top.mainloop()

from __future__ import annotations
from tkinter import *


def pos(elm, pos_ar: list[int]):
    row, col, rowspan, colspan = pos_ar
    elm.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, padx=5, pady=5)


class MyFrame:
    def __init__(self, prnt, title: str, width: int, height: int, pos_ar: list[int]):
        self.elm: LabelFrame = LabelFrame(prnt, text=title)
        self.elm.config(width=width)
        self.elm.config(height=height)
        self.elm.grid_propagate(False)
        pos(self.elm, pos_ar)
        self.children = {}

    def add_label(self, nm: str, text: str, width: int, height: int, pos_ar: list[int]) -> MyLabel:
        self.children[nm]: MyLabel = MyLabel(self.elm, text, width, height, pos_ar)
        return self.children[nm]

    def add_button(self, nm: str, text: str, cb, pos_ar: list[int]) -> MyButton:
        self.children[nm]: MyButton = MyButton(self.elm, text, cb, pos_ar)
        return self.children[nm]


class MyLabel:
    def __init__(self, prnt, text: str, width: int, height: int, pos_ar: list[int]):
        self.prnt = prnt
        self.var: StringVar = StringVar()
        self.elm = Label(self.prnt, textvariable=self.var)
        self.var.set(text)
        self.elm.config(width=width)
        self.elm.config(height=height)
        pos(self.elm, pos_ar)

    def set(self, text):
        self.var.set(text)


class MyButton:
    def __init__(self, prnt, text: str, cb, pos_ar: list[int]):
        self.prnt = prnt
        self.elm = Button(self.prnt, text=text, command=cb)
        pos(self.elm, pos_ar)


class MyApp:
    def __init__(self, title: str, width: int, height: int):
        self.top = Tk()
        self.top.title(title)
        self.top.grid_propagate(False)
        self.top.geometry(f'{width}x{height}+10+10')
        self.children = {}

    def add_frame(self, title: str, width: int, height: int, pos_ar: list[int]) -> MyFrame:
        self.children['title'] = MyFrame(self.top, title, width, height, pos_ar)
        return self.children['title']

    def show(self):
        self.top.mainloop()

from tkinter import *
from typing import List


def dummy(*args, **kwargs):
    pass


def pos(elm, xy: List[int]):
    elm.place(x=xy[0], y=xy[1])


class MyButton:
    def __init__(self, prnt, text: str, cb, xy: List[int]):
        self.prnt = prnt
        self.elm = Button(self.prnt, text=text, command=cb)
        pos(self.elm, xy)


class MyLabel:
    def __init__(self, prnt, text: str, width: int, height: int, xy: List[int]):
        self.prnt = prnt
        self.var: StringVar = StringVar()
        self.elm = Label(self.prnt, textvariable=self.var)
        self.var.set(text)
        self.elm.config(width=width)
        self.elm.config(height=height)
        pos(self.elm, xy)

    def set(self, text):
        self.var.set(text)


class MyFrame:
    def __init__(self, prnt, title: str, width: int, height: int, xy: List[int]):
        self.elm: LabelFrame = LabelFrame(prnt, text=title)
        self.elm.config(width=width)
        self.elm.config(height=height)
        pos(self.elm, xy)
        self.children = {}

    def add_label(self, text: str, width: int, height: int, xy: List[int]) -> MyLabel:
        self.children[text]: MyLabel = MyLabel(self.elm, text, width, height, xy)
        return self.children[text]

    def add_button(self, text: str, cb, xy: List[int]) -> MyButton:
        self.children[text]: MyButton = MyButton(self.elm, text, cb, xy)
        return self.children[text]


class MyApp:
    def __init__(self, title: str, width: int, height: int):
        self.top = Tk()
        self.top.title(title)
        self.top.grid_propagate(False)
        self.top.geometry(f'{width}x{height}+10+10')
        self.children = {}

    def add_frame(self, title: str, width: int, height: int, xy: List[int]) -> MyFrame:
        self.children['title'] = MyFrame(self.top, title, width, height, xy)
        return self.children['title']

    def show(self):
        self.top.mainloop()

from __future__ import annotations
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from typing import List, Callable


def pos(elm, pos_ar: List[int]):
    row, col, rowspan, colspan = pos_ar
    elm.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, padx=5,
             pady=5)


class MyDropdown:
    def __init__(self, prnt, ar, width: int, height: int, pos_ar: List[int],
                 cb):
        self.prnt = prnt
        self.ar = ar
        self.var: StringVar = StringVar()
        self.elm = ttk.OptionMenu(self.prnt, self.var, ar[0], *ar, command=cb)
        self.elm.config(width=width)
        pos(self.elm, pos_ar)

    def load_list(self, ar):
        self.ar = ar
        self.elm.set_menu(None, *self.ar)
        self.set(ar[0])

    def set(self, text):
        self.var.set(text)

    def get(self):
        return self.var.get()


class MyListbox:
    def __init__(self, prnt, ar: List[str], width: int, height: int,
                 pos_ar: List[int]):
        self.prnt = prnt
        self.ar = ar
        self.var: StringVar = StringVar()
        self.elm = Listbox(self.prnt, listvariable=self.var, width=width,
                           height=height)
        pos(self.elm, pos_ar)
        self.load_list()

    def clear(self):
        self.elm.delete(0, END)

    def load_list(self):
        self.clear()
        for i, v in enumerate(self.ar):
            self.elm.insert(i + 1, v)

    def add_item(self, v: str):
        self.ar.extend([v])
        self.load_list()

    def set(self, text):
        self.var.set(text)

    def get(self):
        ar = [self.elm.get(i) for i in self.elm.curselection()]
        if len(ar) > 0:
            return ar[0]
        return None

    def get_active_index(self):
        ar = self.elm.curselection()
        if len(ar) > 0:
            return ar[0]
        return None


class MyLabel:
    def __init__(self, prnt, text: str, width: int, height: int,
                 pos_ar: List[int]):
        self.prnt = prnt
        self.var: StringVar = StringVar()
        self.elm = ttk.Label(self.prnt, textvariable=self.var)
        self.var.set(text)
        self.elm.config(width=width)
        # self.elm.config(height=height)
        pos(self.elm, pos_ar)

    def set(self, text):
        self.var.set(text)

    def set_font_size(self, sz: int):
        self.elm.config(font=("verdana", sz))


class MyButton:
    def __init__(self, prnt, text: str, cb, pos_ar: List[int]):
        self.prnt = prnt
        self.elm = Button(self.prnt, text=text, command=cb)
        pos(self.elm, pos_ar)


class MyText():
    def __init__(self, prnt, text: str, width: int, height: int,
                 pos_ar: List[int]):
        self.prnt = prnt
        self.elm = Text(self.prnt, width=width, height=height)
        self.set(text)
        pos(self.elm, pos_ar)

    def clear(self):
        self.elm.delete('1.0', END)

    def set(self, text):
        self.clear()
        self.elm.insert(END, text)

    def get(self):
        return self.elm.get('1.0', 'end -1c')


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

    def add_button(self, nm: str, text: str, cb, pos_ar: List[int]) -> MyButton:
        self.children[nm]: MyButton = MyButton(self.elm, text, cb, pos_ar)
        return self.children[nm]

    def add_text(self, nm: str, text: str, width: int, height: int,
                 pos_ar: List[int]) -> MyText:
        self.children[nm]: MyText = MyText(self.elm, text, width, height,
                                           pos_ar)
        return self.children[nm]

    def add_listbox(self, nm: str, ar: List[str], width: int, height: int,
                    pos_ar: List[int]) -> MyListbox:
        self.children[nm]: MyListbox = MyListbox(self.elm, ar, width, height,
                                                 pos_ar)
        return self.children[nm]

    def add_dropdown(self, nm: str, ar: List[str], width: int, height: int,
                     pos_ar: List[int], cb) -> MyDropdown:
        self.children[nm]: MyDropdown = MyDropdown(self.elm, ar, width, height,
                                                   pos_ar, cb)
        return self.children[nm]

    def add_frame(self, title: str, width: int, height: int,
                  pos_ar: List[int]) -> MyFrame:
        self.children[title] = MyFrame(self.elm, title, width, height, pos_ar)
        return self.children[title]

    def remove_border(self):
        self.elm.config(borderwidth=0)
        self.elm.config(highlightthickness=0)

class MyApp:
    def __init__(self, title: str, width: int, height: int):
        self.top = Tk()
        self.top.title(title)
        self.top.grid_propagate(False)
        tkFont.nametofont("TkDefaultFont").config(size=12)
        self.top.option_add("*font", "verdana 12")
        self.top.geometry(f'{width}x{height}+10+10')
        self.children = {}
        self.main_frame: MyFrame = self.add_main_frame()

    def add_frame(self, title: str, width: int, height: int,
                  pos_ar: list[int]) -> MyFrame:
        self.children[title] = MyFrame(self.top, title, width, height, pos_ar)
        return self.children[title]

    def clear_screen(self):
        if '--' in self.children:
            self.children['--'].elm.destroy()
        self.main_frame = self.add_main_frame()
        self.main_frame.remove_border()

    def add_main_frame(self):
        return self.add_frame("--", 790, 590, [1, 1, 1, 1])

    def show(self):
        self.top.mainloop()

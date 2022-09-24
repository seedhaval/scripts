from tkinter import *
from typing import List


def dummy(*args, **kwargs):
    pass


def pos(elm, xy: List[int]):
    elm.place(x=xy[0], y=xy[1])


class MyWidget:
    def __init__(self, elm, xy: List[int]):
        self.elm = elm
        self.default_bg = self.elm.cget('background')
        self.x, self.y = xy
        pos(self.elm, xy=xy)

    def move(self, x: int, y: int):
        self.x, self.y = x, y
        pos(self.elm, xy=[x, y])

    def bg(self, clr: str):
        self.elm.config(bg=clr)

    def reset_bg(self):
        self.elm.config(bg=self.default_bg)

    def hide(self):
        self.elm.place_forget()

    def show(self):
        pos(self.elm, xy=[self.x, self.y])


class MyButton(MyWidget):
    def __init__(self, prnt, text: str, cb, xy: List[int]):
        self.prnt = prnt
        self.elm = Button(self.prnt, text=text, command=cb)
        super().__init__(self.elm, xy)

    def set(self, text):
        self.elm['text'] = text


class MyDropdown(MyWidget):
    def __init__(self, prnt, options: List[str], text: str, xy: List[int]):
        self.prnt = prnt
        self.var: StringVar = StringVar()
        self.var.set(text)
        self.elm = OptionMenu(self.prnt, self.var, *options)
        super().__init__(self.elm, xy)

    def set(self, text):
        self.var.set(text)


class MyLabel(MyWidget):
    def __init__(self, prnt, text: str, width: int, height: int, xy: List[int]):
        self.prnt = prnt
        self.var: StringVar = StringVar()
        self.elm = Label(self.prnt, textvariable=self.var)
        self.var.set(text)
        self.elm.config(width=width)
        self.elm.config(height=height)
        super().__init__(self.elm, xy)

    def set(self, text):
        self.var.set(text)


class MyText(MyWidget):
    def __init__(self, prnt, text: str, width: int, height: int, xy: List[int]):
        self.prnt = prnt
        self.elm = Text(self.prnt, width=width, height=height)
        self.set(text)
        super().__init__(self.elm, xy)

    def clear(self):
        self.elm.delete('1.0', END)

    def set(self, text):
        self.clear()
        self.elm.insert(END, text)


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

    def add_text(self, text: str, width: int, height: int, xy: List[int]) -> MyText:
        self.children[text]: MyText = MyText(self.elm, text, width, height, xy)
        return self.children[text]

    def add_button(self, text: str, cb, xy: List[int]) -> MyButton:
        self.children[text]: MyButton = MyButton(self.elm, text, cb, xy)
        return self.children[text]

    def add_dropdown(self, options: List[str], text: str, xy: List[int]) -> MyDropdown:
        self.children[text]: MyDropdown = MyDropdown(self.elm, options, text, xy)
        return self.children[text]


class MyApp:
    def __init__(self, title: str, width: int, height: int):
        self.top = Tk()
        self.top.title(title)
        self.top.grid_propagate(False)
        self.top.geometry(f'{width}x{height}+10+10')
        self.top.option_add("*font", "verdana 28")
        self.children = {}

    def add_frame(self, title: str, width: int, height: int, xy: List[int]) -> MyFrame:
        self.children['title'] = MyFrame(self.top, title, width, height, xy)
        return self.children['title']

    def show(self):
        self.top.mainloop()


class Scene:
    def __init__(self, obj, pafter=0):
        self.obj = obj
        self.is_finished = False
        self.cur_step = 0
        self.pafter = pafter

    def set_move(self, tgt):
        self.tgt = tgt
        self.steps = 15
        self.delay_ms = 200
        self.init = self.init_move

    def init_move(self):
        self.strt = {k: (v.x, v.y) for k, v in self.obj.items()}
        self.delta = {}
        for k, v in self.tgt.items():
            dx = (self.tgt[k][0] - self.strt[k][0]) * 1.0 / self.steps
            dy = (self.tgt[k][1] - self.strt[k][1]) * 1.0 / self.steps
            self.delta[k] = (dx, dy)
        self.action = self.move

    def move(self):
        for k in self.tgt.keys():
            obj = self.obj[k]
            dx, dy = self.delta[k]
            obj.move(obj.x + dx, obj.y + dy)
        self.cur_step += 1
        if self.cur_step >= self.steps:
            self.is_finished = True

    def set_show_once(self, wdgt, text, dly):
        self.wdgt = wdgt
        self.text = text
        self.delay_ms = dly
        self.init = dummy
        self.action = self.show_once

    def show_once(self):
        if self.cur_step == 0:
            self.obj[self.wdgt].set(self.text)
            self.obj[self.wdgt].show()
        elif self.cur_step == 1:
            self.obj[self.wdgt].hide()
            self.is_finished = True
        self.cur_step += 1

    def set_flash(self, ar, clr, dly):
        self.ar = ar
        self.clr = clr
        self.delay_ms = dly
        self.action = self.flash
        self.init = dummy

    def flash(self):
        if self.cur_step in (0, 2):
            for w in self.ar:
                self.obj[w].bg(self.clr)
        else:
            for w in self.ar:
                self.obj[w].reset_bg()
        if self.cur_step > 2:
            self.is_finished = True
        self.cur_step += 1

    def set_change_text(self, ar, dly):
        self.ar = ar
        self.delay_ms = dly
        self.init = dummy
        self.action = self.change_text

    def change_text(self):
        w, v = self.ar[self.cur_step]
        self.obj[w].set(v)
        if self.cur_step >= len(self.ar) - 1:
            self.is_finished = True
        self.cur_step += 1

    def next_step(self):
        self.action()

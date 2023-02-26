from __future__ import annotations

import tkinter.font as tkFont
from collections import OrderedDict
from tkinter import *
from tkinter import ttk
from typing import List


def pos(elm, pos_ar: List[int]):
    row, col, rowspan, colspan = pos_ar
    elm.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, padx=5,
             pady=5)


class MyTreeView:
    def __init__(self, prnt, height: int, cols, pos_ar: List[int], cb):
        self.prnt = prnt
        self.elm = ttk.Treeview(self.prnt, selectmode='browse',
                                show=["headings"], height=height)
        self.cols = cols
        self.data = []
        self.elm["columns"] = [str(x + 1) for x in range(len(cols))]
        for i, cinfo in enumerate(cols):
            colnm, width, anchor = cinfo
            self.elm.column(str(i + 1), width=width, anchor=anchor)
            self.elm.heading(str(i + 1), text=colnm)
        self.elm.bind('<ButtonRelease-1>', cb)
        pos(self.elm, pos_ar)

    def clear(self):
        for item in self.elm.get_children():
            self.elm.delete(item)

    def load_data(self, ar):
        self.data = ar
        self.clear()
        for i, values in enumerate(ar):
            self.elm.insert("", 'end', values=values, text=f"{i}",
                            iid=f'Row{i}')

    def update_current_row(self, colid, colval):
        if self.cur_ir is not None:
            self.data[self.cur_ir][colid] = colval
            self.elm.item(self.cur_iid, values=self.data[self.cur_ir])

    def select_row(self, ir):
        self.elm.selection_set(f'Row{ir}')
        self.cur_ir = ir
        self.cur_iid = f"Row{self.cur_ir}"

    def select_focussed(self):
        self.focus = self.elm.focus()
        sel = self.elm.item(self.focus)
        if sel['text']:
            self.select_row(int(sel['text']))
        else:
            self.cur_ir = None
            self.cur_iid = None

    def get_sel_row_values(self):
        if self.cur_ir is not None:
            return self.data[self.cur_ir]
        return None

    def select_next_row(self):
        if self.cur_ir is not None and len(self.data) > self.cur_ir + 1:
            self.select_row(self.cur_ir + 1)


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

    def bind_return(self, cb):
        self.return_cb = cb
        self.elm.bind('<Return>', cb)

    def select_all(self):
        self.elm.tag_add(SEL, "1.0", END)
        self.elm.mark_set(INSERT, "1.0")
        self.elm.see(INSERT)

    def focus(self):
        self.elm.focus_set()

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

    def add_dropdown(self, nm: str, ar: List[str], width: int, height: int,
                     pos_ar: List[int], cb) -> MyDropdown:
        self.children[nm]: MyDropdown = MyDropdown(self.elm, ar, width, height,
                                                   pos_ar, cb)
        return self.children[nm]

    def add_treeview(self, nm: str, height: int, cols,
                     pos_ar: List[int], cb) -> MyTreeView:
        self.children[nm]: MyTreeView = MyTreeView(self.elm, height, cols,
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
        self.top.option_add("*font", ("", 12))
        self.top.geometry(f'{width}x{height}+10+10')
        self.children = {}
        self.main_frame: MyFrame = self.add_main_frame()
        self.menu = OrderedDict()
        self.xobj = []
        self.menubar: Menu

    def add_frame(self, title: str, width: int, height: int,
                  pos_ar: list[int]) -> MyFrame:
        self.children[title] = MyFrame(self.top, title, width, height, pos_ar)
        return self.children[title]

    def clear_screen(self):
        if '  ' in self.children:
            self.children['  '].elm.destroy()
        self.main_frame = self.add_main_frame()
        self.main_frame.remove_border()

    def add_main_frame(self):
        return self.add_frame("  ", 790, 590, [1, 1, 1, 1])

    def add_menu(self, menu_ar):
        self.menubar = Menu(self.top)
        self.top.config(menu=self.menubar)

        for menu, submenu, cmd in menu_ar:
            if menu not in self.menu:
                mobj = Menu(self.menubar, tearoff=False)
                self.menu[menu] = mobj
            else:
                mobj = self.menu[menu]
            mobj.add_command(label=submenu, command=cmd)
            self.xobj.append(mobj)

        for k, v in self.menu.items():
            self.menubar.add_cascade(label=k, menu=v)

    def show(self):
        self.top.mainloop()

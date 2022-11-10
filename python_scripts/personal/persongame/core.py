from tkinter import *
from typing import List, Callable
from datetime import datetime, date
import csv


def pos(elm, pos_ar: List[int]):
    row, col, rowspan, colspan = pos_ar
    elm.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, padx=5,
             pady=5)


class MyLabel:
    def __init__(self, prnt, text: str, width: int, height: int,
                 pos_ar: List[int]):
        self.prnt = prnt
        self.var: StringVar = StringVar()
        self.elm = Label(self.prnt, textvariable=self.var)
        self.var.set(text)
        self.elm.config(width=width)
        self.elm.config(height=height)
        pos(self.elm, pos_ar)

    def set(self, text):
        self.var.set(text)

    def set_font_size(self, sz: int):
        self.elm.config(font=("Roboto", sz))


class MyButton:
    def __init__(self, prnt, text: str, cb, pos_ar: List[int]):
        self.prnt = prnt
        self.elm = Button(self.prnt, text=text, command=cb)
        pos(self.elm, pos_ar)


class MyCanvas:
    def __init__(self, prnt, width: int, height: int, pos_ar: List[int]):
        self.prnt = prnt
        self.height = height
        self.width = width
        self.elm: Canvas = Canvas(prnt, height=height, width=width)
        self.imgtk = None
        pos(self.elm, pos_ar)
        self.cb = None

    def set_callback(self, cb):
        self.cb = cb
        self.elm.bind('<Button-1>', self.cb)

    def set_image(self, imgtk):
        self.imgtk = imgtk
        self.elm.create_image(self.width, self.height, image=imgtk, anchor=SE)


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

    def add_canvas(self, nm: str, width: int, height: int,
                   pos_ar: List[int]) -> MyCanvas:
        self.children[nm]: MyCanvas = MyCanvas(self.elm, width, height, pos_ar)
        return self.children[nm]


def add_frame(self, title: str, width: int, height: int,
              pos_ar: List[int]):
    self.children['title'] = MyFrame(self.elm, title, width, height, pos_ar)
    return self.children['title']


class MyApp:
    def __init__(self, title: str, width: int, height: int):
        self.top = Tk()
        self.top.title(title)
        self.top.grid_propagate(False)
        self.top.geometry(f'{width}x{height}+10+10')
        self.children = {}

    def add_frame(self, title: str, width: int, height: int,
                  pos_ar: list[int]) -> MyFrame:
        self.children['title'] = MyFrame(self.top, title, width, height, pos_ar)
        return self.children['title']

    def show(self):
        self.top.mainloop()


class Action:
    def __init__(self, ar: List[str]):
        self.person: str = ar[0]
        self.section: str = ar[1]
        self.event: str = ar[2]
        self.duetime: date = datetime.strptime(ar[3], "%Y-%m-%d %H:%M:%S")
        self.cooling_days: float = float(ar[4])
        self.verb: str = ar[5]
        self.action_minutes: int = int(ar[6])
        self.wait_text: str = ar[7]

    def get_busy_text(self):
        return self.wait_text.replace("$x", self.person)


class ActionData:
    def __init__(self):
        self.actions: List[Action] = []
        self.load()

    def load(self):
        with open("Action - Action.csv") as f:
            csv_reader = csv.reader(f)
            next(csv_reader, None)
            for row in csv_reader:
                self.actions.append(Action(row))


class Section:
    def __init__(self, ar: List[str]):
        self.file: str = ar[0]
        self.person: str = ar[1]
        self.section: str = ar[2]
        self.x1: int = int(ar[3])
        self.y1: int = int(ar[4])
        self.x2: int = int(ar[5])
        self.y2: int = int(ar[6])


class SectionData:
    def __init__(self):
        self.sections: List[Section] = []
        self.load()

    def load(self):
        with open("Action - Section.csv") as f:
            csv_reader = csv.reader(f)
            next(csv_reader, None)
            for row in csv_reader:
                self.sections.append(Section(row))


class GameData:
    def __init__(self):
        self.action_data: ActionData = ActionData()
        self.section_data: SectionData = SectionData()


class Photo:
    def __init__(self, cnv: MyCanvas, file: str, cb: Callable):
        self.cnv = cnv
        self.file = file
        self.cb = cb

    def show_all_sections(self):
        pass

    def show_overdue_sections(self):
        pass

    def handle_click(self, event):
        pass
        person: str = ""
        section: str = ""
        self.cb(person, section)


class EditSection:
    def __init__(self, frame: MyFrame, gd: GameData):
        self.frame = frame
        self.gd = gd

    def delete_section(self):
        pass

    def load_section(self, person: str, section: str):
        pass


class DoAction:
    def __init__(self, gd: GameData):
        self.gd = gd
        self.action = None

    def show(self, action: Action):
        pass

    def show_busy(self):
        pass

    def perform_action(self):
        pass

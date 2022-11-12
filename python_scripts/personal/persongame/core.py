from tkinter import *
from typing import List, Callable, Dict
from datetime import datetime, date, timedelta
from PIL import Image, ImageTk, ImageDraw
import csv
import random


def pos(elm, pos_ar: List[int]):
    row, col, rowspan, colspan = pos_ar
    elm.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, padx=5,
             pady=5)


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

    def add_text(self, nm: str, text: str, width: int, height: int,
                 pos_ar: List[int]) -> MyText:
        self.children[nm]: MyText = MyText(self.elm, text, width, height,
                                           pos_ar)
        return self.children[nm]


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


class CSV:
    def __init__(self, fl: str, header: bool, headertxt: str):
        self.fl = fl
        self.header = header
        self.headertxt = headertxt

    def get_shuffled_records(self):
        out = []
        with open(self.fl) as f:
            csv_reader = csv.reader(f)
            if self.header == True:
                next(csv_reader, None)
            for row in csv_reader:
                out.append(row)
        random.shuffle(out)
        return out

    def write(self, data: List):
        with open(self.fl, "w") as f:
            f.write(self.headertxt + '\n')
            for row in data:
                f.write(','.join([str(x) for x in row]) + '\n')


class Action:
    def __init__(self, ar: List[str], idx: int):
        self.person: str = ar[0].strip()
        self.section: str = ar[1].strip()
        self.event: str = ar[2]
        self.duetimetxt = ar[3]
        self.duetime: date = datetime.strptime(ar[3], "%Y-%m-%d %H:%M:%S")
        self.cooling_days: float = float(ar[4])
        self.verb: str = ar[5]
        self.idx: int = idx
        if self.duetime > datetime.now():
            self.is_due = False
        else:
            self.is_due = True

    def get_row_ar(self):
        return [self.person, self.section, self.event, self.duetimetxt,
                self.cooling_days, self.verb]

    def do(self):
        self.duetime = datetime.now() + timedelta(days=self.cooling_days)
        self.duetimetxt = self.duetime.strftime("%Y-%m-%d %H:%M:%S")
        self.is_due = False


class ActionData:
    def __init__(self):
        self.actions: Dict[int, Action] = {}
        self.fl = "Action - Action.csv"
        self.header = "person,section,event,due,cool,verb"
        self.csv = CSV(self.fl, True, self.header)
        self.load()

    def get_sorted_data(self):
        return sorted(self.actions.values(), key=lambda x: (
            x.verb, x.event, x.person, x.section))

    def load(self) -> None:
        self.actions = {i: Action(x, i) for i, x in
                        enumerate(self.csv.get_shuffled_records())}

    def get_due(self) -> List[Action]:
        return [x for x in self.actions.values() if x.is_due]

    def save(self) -> None:
        self.csv.write([x.get_row_ar() for x in self.get_sorted_data()])


class Section:
    def __init__(self, ar: List[str], idx: int):
        self.file: str = ar[0]
        self.person: str = ar[1].strip()
        self.section: str = ar[2].strip()
        self.x1: int = int(ar[3])
        self.y1: int = int(ar[4])
        self.x2: int = int(ar[5])
        self.y2: int = int(ar[6])
        self.minx, self.maxx = sorted((self.x1, self.x2))
        self.miny, self.maxy = sorted((self.y1, self.y2))
        self.idx = idx

    def get_bbox(self):
        return [(self.x1, self.y1), (self.x2, self.y2)]

    def point_exists(self, x: int, y: int):
        if not self.minx <= x <= self.maxx:
            return False
        if not self.miny <= y <= self.maxy:
            return False
        return True

    def get_row_ar(self):
        return [self.file, self.person, self.section, self.x1, self.y1,
                self.x2, self.y2]


class SectionData:
    def __init__(self):
        self.sections: Dict[int, Section] = {}
        self.fl = "Action - Section.csv"
        self.header = "file,person,section,x1,y1,x2,y2"
        self.csv = CSV(self.fl, True, self.header)
        self.load()

    def load(self) -> None:
        self.sections = {i: Section(x, i) for i, x in
                         enumerate(self.csv.get_shuffled_records())}

    def get_sections_for_file(self, file: str) -> List[Section]:
        return ([x for x in self.sections.values() if x.file == file])

    def save(self):
        self.csv.write([x.get_row_ar() for x in self.sections.values()])


class GameData:
    def __init__(self):
        self.action_data: ActionData = ActionData()
        self.section_data: SectionData = SectionData()
        self.file = None
        self.cur_ar = []
        self.cur_act: Action = None
        self.cur_sec: Section = None

    def get_one_due_action(self):
        ref_set = {(x.person, x.section): x for x in
                   self.section_data.get_sections_for_file(self.file)}
        self.cur_act = [x for x in self.action_data.get_due() if
                        (x.person, x.section) in ref_set][0]
        self.cur_sec = ref_set[(self.cur_act.person, self.cur_act.section)]


class Photo:
    def __init__(self, cnv: MyCanvas, cb: Callable, cnvw: int, cnvh: int):
        self.cnv = cnv
        self.cb = cb
        self.section_ar = []
        self.file = None
        self.file_img = None
        self.pil_img = None
        self.tk_img = None
        self.cnvw, self.cnvh = (cnvw, cnvh)
        self.scale = 1.0
        self.cnv.set_callback(self.handle_click)

    def load_file(self, file: str):
        self.file = file
        img = Image.open(file)
        imgw, imgh = img.size
        rx = self.cnvw * 1.00 / imgw
        ry = self.cnvh * 1.00 / imgh
        self.scale = min(rx, ry)
        n_imgw = int(imgw * self.scale)
        n_imgh = int(imgh * self.scale)
        self.file_img = img.resize((n_imgw, n_imgh))
        self.load_image()

    def load_image(self):
        self.pil_img = Image.new('RGBA', (self.cnvw, self.cnvh), (0, 0, 0, 255))
        self.pil_img.paste(self.file_img, (1, 1),
                           self.file_img.copy().convert('RGBA'))
        draw = ImageDraw.Draw(self.pil_img)
        for s in self.section_ar:
            x1, y1 = [x * self.scale for x in s.get_bbox()[0]]
            x2, y2 = [x * self.scale for x in s.get_bbox()[1]]
            draw.rectangle(((x1, y1), (x2, y2)), outline=(150, 0, 0), width=5)
        self.tk_img = ImageTk.PhotoImage(self.pil_img.convert("RGB"))
        self.cnv.set_image(self.tk_img)

    def update_sections(self, section_ar):
        self.section_ar = section_ar
        self.load_image()

    def handle_click(self, event):
        x, y = [event.x, event.y]
        self.cb(int(x / self.scale), int(y / self.scale))


class EditSection:
    def __init__(self, frame: MyFrame, gd: GameData):
        self.frame = frame
        self.gd = gd
        self.lbl_person: MyLabel = self.frame.add_label("person", "Person",
                                                        20, 1, [1, 1, 1, 1])
        self.txt_person: MyText = self.frame.add_text("personnm", "", 20, 1,
                                                      [1, 2, 1, 1])
        self.lbl_section: MyLabel = self.frame.add_label("section", "Section",
                                                         20, 1, [2, 1, 1, 1])
        self.txt_section: MyText = self.frame.add_text("sectionnm", "", 20, 1,
                                                       [2, 2, 1, 1])
        self.btn_add: MyButton = self.frame.add_button("add", "Add",
                                                       self.add_section,
                                                       [3, 1, 1, 1])

    def add_section(self):
        file = self.gd.file
        person = self.txt_person.get()
        section = self.txt_section.get()
        x1, y1 = [str(x) for x in self.gd.cur_ar[0]]
        x2, y2 = [str(x) for x in self.gd.cur_ar[1]]
        sid = max(self.gd.section_data.sections.keys()) + 1
        self.gd.section_data.sections[sid] = Section([file, person, section,
                                                      x1, y1, x2, y2], sid)
        self.gd.section_data.save()


class DoAction:
    def __init__(self, gd: GameData, frame, cb):
        self.gd = gd
        self.cb = cb
        self.action = None
        self.lblltxt = frame.add_label("txt", "", 40, 3, [1, 1, 1, 1])
        self.lblverb = frame.add_button("btn", "", self.perform_action,
                                        [2, 1, 1, 1])

    def perform_action(self):
        self.gd.cur_act.do()
        self.lblltxt.set("")
        self.lblverb.elm['text'] = ''
        self.gd.action_data.save()
        self.cb()

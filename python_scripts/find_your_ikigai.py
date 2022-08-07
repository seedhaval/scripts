import tkhelper
from typing import List, Dict
import json
import os

s1 = "What you love"
s2 = "What you are good at"
s3 = "What the world needs"
s4 = "What you can be paid for"

obj = {}
cursel = {}


def load_data() -> Dict[str, List[str]]:
    if os.path.exists('ikigai.json'):
        with open('ikigai.json') as f:
            return json.load(f)
    return {s1: [], s2: [], s3: [], s4: []}


def update_txt():
    pass


def delete_txt():
    pass


def refresh_clue():
    pass


class EditableListBox:
    def __init__(self, prnt: tkhelper.MyFrame, lbl: str, pos_ar: List[int]):
        self.nm = lbl
        self.cvr = prnt.add_frame("", width=320, height=190, pos_ar=pos_ar)
        self.lbl = self.cvr.add_label(lbl + "_lbl", lbl, width=25, height=2, pos_ar=[1, 1, 1, 1])
        self.btn = self.cvr.add_button(lbl + "_add", "+", cb=lambda: add(self), pos_ar=[1, 2, 1, 1])
        self.lb = self.cvr.add_listbox(lbl + "_list", [], lambda x: handle_listbox_select(self), width=30, height=6,
                                       pos_ar=[2, 1, 1, 2])


class ClueListBox:
    def __init__(self, prnt: tkhelper.MyFrame, lbl: str, pos_ar: List[int]):
        self.cvr = prnt.add_frame("", width=320, height=190, pos_ar=pos_ar)
        self.lbl = self.cvr.add_label(lbl + "_lbl", lbl, width=25, height=2, pos_ar=[1, 1, 1, 1])
        self.btn = self.cvr.add_button(lbl + "_add", "⟳", cb=refresh_clue, pos_ar=[1, 2, 1, 1])
        self.lb = self.cvr.add_listbox(lbl + "_list", [], clear_txt, width=30, height=6,
                                       pos_ar=[2, 1, 1, 2])


def clear_txt():
    pass


def handle_listbox_select(cntnr: EditableListBox):
    curIdx = cntnr.lb.get_active_index()
    if not curIdx:
        return
    cntnr.lb.get()


def add(cntnr: EditableListBox):
    cntnr.lb.add_item('new entry')

def load_ui():
    main_fr = app.add_frame("", 1000, 730, [1, 1, 1, 3])
    main_fr.add_label("lbl1", "Find Your Ikigai", 30, 1, [1, 1, 1, 3])
    top_fr = main_fr.add_frame("", 990, 60, [2, 1, 1, 1])
    obj['txt'] = top_fr.add_text("txt1", "", 87, 1, [1, 1, 1, 1])
    top_fr.add_button("update", "✓", update_txt, [1, 2, 1, 1])
    top_fr.add_button("delete", "🗑", delete_txt, [1, 3, 1, 1])
    cnt_fr = main_fr.add_frame("", 990, 600, [3, 1, 1, 1])
    obj[s1] = EditableListBox(cnt_fr, s1, [1, 2, 1, 1])
    obj[s2] = EditableListBox(cnt_fr, s2, [2, 1, 1, 1])
    obj[s3] = EditableListBox(cnt_fr, s3, [2, 3, 1, 1])
    obj[s4] = EditableListBox(cnt_fr, s4, [3, 2, 1, 1])
    obj['clue'] = ClueListBox(cnt_fr, "Clues", [2, 2, 1, 1])


app = tkhelper.MyApp("Find your Ikigai", 1010, 740)
data = load_data()
load_ui()
app.show()

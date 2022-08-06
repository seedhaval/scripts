import tkhelper
from typing import List


def update_txt():
    pass


def delete_txt():
    pass


class EditableListBox:
    def __init__(self, prnt: tkhelper.MyFrame, lbl: str, pos_ar: List[int]):
        self.nm = lbl
        self.cvr = prnt.add_frame("", width=320, height=190, pos_ar=pos_ar)
        self.lbl = self.cvr.add_label(lbl + "_lbl", lbl, width=25, height=2, pos_ar=[1, 1, 1, 1])
        self.btn = self.cvr.add_button(lbl + "_add", "+", cb=lambda: add(self), pos_ar=[1, 2, 1, 1])
        self.lb = self.cvr.add_listbox(lbl + "_list", [], width=30, height=6, pos_ar=[2, 1, 1, 2])


class ReadOnlyListBox:
    def __init__(self, prnt: tkhelper.MyFrame, lbl: str, pos_ar: List[int]):
        self.cvr = prnt.add_frame("", width=320, height=190, pos_ar=pos_ar)
        self.lbl = self.cvr.add_label(lbl + "_lbl", lbl, width=30, height=2, pos_ar=[1, 1, 1, 1])
        self.lb = self.cvr.add_listbox(lbl + "_list", [], width=30, height=6,
                                       pos_ar=[2, 1, 1, 2])


def add(cntnr: EditableListBox):
    print(cntnr.nm)


def load_ui():
    main_fr = app.add_frame("", 1000, 730, [1, 1, 1, 3])
    main_fr.add_label("lbl1", "Find Your Ikigai", 30, 1, [1, 1, 1, 3])
    top_fr = main_fr.add_frame("", 990, 60, [2, 1, 1, 1])
    top_fr.add_text("txt1", "", 87, 1, [1, 1, 1, 1])
    top_fr.add_button("update", "✓", update_txt, [1, 2, 1, 1])
    top_fr.add_button("delete", "🗑", delete_txt, [1, 3, 1, 1])
    cnt_fr = main_fr.add_frame("", 990, 600, [3, 1, 1, 1])
    what_you_love = EditableListBox(cnt_fr, "What you love", [1, 2, 1, 1])
    what_you_are_good_at = EditableListBox(cnt_fr, "What you are good at", [2, 1, 1, 1])
    what_the_world_needs = EditableListBox(cnt_fr, "What the world needs", [2, 3, 1, 1])
    what_you_can_be_paid_for = EditableListBox(cnt_fr, "What you can be paid for", [3, 2, 1, 1])
    clue = ReadOnlyListBox(cnt_fr, "Clues", [2, 2, 1, 1])


app = tkhelper.MyApp("Find your Ikigai", 1010, 740)
load_ui()
app.show()

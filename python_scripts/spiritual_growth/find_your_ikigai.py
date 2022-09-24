import collections

import tkhelper
from typing import List, Dict
import json
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

s1 = "What you love"
s2 = "What you are\ngood at"
s3 = "What the world\nneeds"
s4 = "What you can\nbe paid for"

stop_words = set(stopwords.words('english'))
obj = {}
cursel = {}
ps = PorterStemmer()


class EditableListBox:
    def __init__(self, prnt: tkhelper.MyFrame, lbl: str, ar: List[str], pos_ar: List[int]):
        self.nm = lbl
        self.cvr = prnt.add_frame("", width=320, height=190, pos_ar=pos_ar)
        self.lbl = self.cvr.add_label(lbl + "_lbl", lbl, width=18, height=2, pos_ar=[1, 1, 1, 1])
        self.btn = self.cvr.add_button(lbl + "_add", "+", cb=lambda: add(self), pos_ar=[1, 2, 1, 1])
        self.btn = self.cvr.add_button(lbl + "_edit", "✎", cb=lambda: edit_txt(self), pos_ar=[1, 3, 1, 1])
        self.btn = self.cvr.add_button(lbl + "_del", "🗑", cb=lambda: delete_txt(self), pos_ar=[1, 4, 1, 1])
        self.lb = self.cvr.add_listbox(lbl + "_list", ar, width=30, height=6,
                                       pos_ar=[2, 1, 1, 4])


class ClueListBox:
    def __init__(self, prnt: tkhelper.MyFrame, lbl: str, pos_ar: List[int]):
        self.cvr = prnt.add_frame("", width=320, height=190, pos_ar=pos_ar)
        self.lbl = self.cvr.add_label(lbl + "_lbl", lbl, width=25, height=2, pos_ar=[1, 1, 1, 1])
        self.btn = self.cvr.add_button(lbl + "_add", "⟳", cb=refresh_clue, pos_ar=[1, 2, 1, 1])
        self.lb = self.cvr.add_listbox(lbl + "_list", [], width=30, height=6,
                                       pos_ar=[2, 1, 1, 2])


def load_data() -> Dict[str, List[str]]:
    if os.path.exists('ikigai.json'):
        with open('ikigai.json') as f:
            return json.load(f)
    return {s1: [], s2: [], s3: [], s4: []}


def update_txt():
    obj[cursel['nm']].lb.ar[cursel['idx']] = obj['txt'].get()
    obj[cursel['nm']].lb.load_list()
    save()


def refresh_clue():
    ar = []
    for s in (s1, s2, s3, s4):
        snt = '. '.join(obj[s].lb.ar)
        tokens = word_tokenize(snt)
        ar.extend(set([ps.stem(w) for w in tokens if not w.lower() in stop_words and len(w) > 2]))
    obj['clue'].lb.ar = [x[0] for x in collections.Counter(ar).most_common(4)]
    obj['clue'].lb.load_list()


def save():
    d = {}
    for k in (s1, s2, s3, s4):
        d[k] = obj[k].lb.ar
    with open('ikigai.json', 'w') as f:
        f.write(json.dumps(d))


def edit_txt(cntnr: EditableListBox):
    global cursel
    curIdx = cntnr.lb.get_active_index()
    if curIdx is None:
        return
    cursel = {'nm': cntnr.nm, 'idx': curIdx}
    obj['txt'].set(cntnr.lb.get())


def delete_txt(cntnr: EditableListBox):
    curIdx = cntnr.lb.get_active_index()
    if curIdx is not None:
        del cntnr.lb.ar[curIdx]
        cntnr.lb.load_list()
    save()


def add(cntnr: EditableListBox):
    cntnr.lb.add_item('new entry')


def load_ui():
    main_fr = app.add_frame("", 1000, 730, [1, 1, 1, 3])
    main_fr.add_label("lbl1", "Find Your Ikigai", 30, 1, [1, 1, 1, 3])
    top_fr = main_fr.add_frame("", 990, 60, [2, 1, 1, 1])
    obj['txt'] = top_fr.add_text("txt1", "", 92, 1, [1, 1, 1, 1])
    top_fr.add_button("update", "✓", update_txt, [1, 2, 1, 1])
    cnt_fr = main_fr.add_frame("", 990, 600, [3, 1, 1, 1])
    obj[s1] = EditableListBox(cnt_fr, s1, data[s1], [1, 2, 1, 1])
    obj[s2] = EditableListBox(cnt_fr, s2, data[s2], [2, 1, 1, 1])
    obj[s3] = EditableListBox(cnt_fr, s3, data[s3], [2, 3, 1, 1])
    obj[s4] = EditableListBox(cnt_fr, s4, data[s4], [3, 2, 1, 1])
    obj['clue'] = ClueListBox(cnt_fr, "Clues", [2, 2, 1, 1])


app = tkhelper.MyApp("Find your Ikigai", 1010, 740)
data = load_data()
load_ui()
app.show()

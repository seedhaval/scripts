import tkhelper

obj = {}

shlok = "कर्मण्येवाधिकारस्ते मा फलेषु कदाचन ।"


def save():
    with open('action.txt', 'a') as f:
        f.write(f"I am {obj['txt1'].get()} because it is my duty to {obj['txt3'].get()}\n")


def load_ui():
    fr = app.add_frame("", width=600, height=60, pos_ar=[1, 1, 1, 1])
    lbl = fr.add_label("shlok", shlok, width=32, height=1, pos_ar=[1, 1, 1, 1])
    lbl.set_font_size(20)
    fr2 = app.add_frame("", width=600, height=230, pos_ar=[2, 1, 1, 1])
    fr2.add_label("lbl1", "I am doing this ...", width=25, height=1, pos_ar=[1, 1, 1, 3])
    obj['txt1'] = fr2.add_text("txt1", "", width=25, height=2, pos_ar=[2, 1, 1, 3])
    fr2.add_label("lbl2", "So that i can get this ...", width=25, height=1, pos_ar=[3, 1, 1, 1])
    fr2.add_label("lbl3", "Because it is my duty to ...", width=25, height=1, pos_ar=[3, 3, 1, 1])
    obj['txt2'] = fr2.add_text("txt2", "", width=25, height=3, pos_ar=[4, 1, 1, 1])
    fr2.add_label("lbl4", "➜\n\n", width=4, height=3, pos_ar=[4, 2, 3, 1])
    obj['txt3'] = fr2.add_text("txt3", "", width=25, height=3, pos_ar=[4, 3, 1, 1])
    fr2.add_button("btn1", "Save", save, [5, 1, 1, 3])


app = tkhelper.MyApp("Abandon Attachment to Fruits of Action", width=610, height=330)
load_ui()
app.show()

from tkinter import messagebox

from lib import db
from lib.uihelper import MyApp

d = {}


def save_data(*args, **kwargs):
    ar = []
    for i, row in enumerate(d['treeview'].data):
        if row[2] != "":
            ar.append(
                f"({d['marks_list'][i][0]},{d['marks_list'][i][3]},{row[2]})")
    db.delete_marks_for_div_exam(d['marks_list'][0][3], d['ddDivision'].get())
    db.bulk_insert_marks(ar)
    messagebox.showinfo("Done !!", "Done !!")


def clear_marks_info(*args, **kwargs):
    d['treeview'].clear()
    d['marks_list'] = []
    d['lblTotal'].set("Total marks = N/A")
    d['txtNewMarks'].clear()


def refresh_table():
    out = []
    for i, minfo in enumerate(d['marks_list']):
        marks = "" if minfo[4] == -999 else str(int(minfo[4]))
        out.append([minfo[1], minfo[2], marks])
    d['treeview'].load_data(out)


def show_student_marks(*args, **kwargs):
    get_student_marks()
    refresh_table()
    d['lblTotal'].set(f"Total marks = {d['marks_list'][0][5]}")


def get_student_marks():
    d['marks_list'] = db.get_student_marks_for_exam(
        d['ddSubject'].get(), d['ddExamCtgy'].get(),
        d['ddExamSubCtgy'].get(), d['ddDivision'].get())
    return d['marks_list']


def handle_subject_change(subject):
    exam_ctgy_list = db.get_exam_categories(d['ddSubject'].get())
    d['ddExamCtgy'].load_list(exam_ctgy_list)
    handle_exam_category_change(d['ddExamCtgy'].get())
    clear_marks_info()


def handle_exam_category_change(exam_category):
    exam_sub_ctgy_list = db.get_exam_sub_categories(d['ddSubject'].get(),
                                                    d['ddExamCtgy'].get())
    d['ddExamSubCtgy'].load_list(exam_sub_ctgy_list)
    clear_marks_info()


def refresh_text_marks():
    row = d['treeview'].get_sel_row_values()
    if row:
        d['txtNewMarks'].set(row[2])
    d['txtNewMarks'].select_all()


def handle_student_select(*args, **kwargs):
    d['treeview'].select_focussed()
    refresh_text_marks()


def handle_marks_enter_key_press(*args, **kwargs):
    d['treeview'].update_current_row(2, d['txtNewMarks'].get())
    d['treeview'].select_next_row()
    refresh_text_marks()
    return "break"


def show_ui(app: MyApp):
    d['app'] = app
    app.clear_screen()
    frm_details = app.main_frame.add_frame("Details", 780, 160, [1, 1, 1, 1])

    frm_details.add_label("Subject", "Subject", 18, 1, [1, 1, 1, 1])

    d['ddSubject'] = frm_details.add_dropdown("ddSubject",
                                              db.get_subject_list(),
                                              25, 1, [1, 2, 1, 1],
                                              handle_subject_change)
    frm_details.add_label("Exam Category", "Exam Category", 18, 1, [2, 1, 1, 1])
    d['ddExamCtgy'] = frm_details.add_dropdown("ddExamCtgy",
                                               db.get_exam_categories(
                                                   d['ddSubject'].get()),
                                               25, 1, [2, 2, 1, 1],
                                               handle_exam_category_change)
    frm_details.add_label("Exam Sub Category", "Exam Sub Category", 18, 1,
                          [3, 1, 1, 1])
    d['ddExamSubCtgy'] = frm_details.add_dropdown("ddExamSubCtgy",
                                                  db.get_exam_sub_categories(
                                                      d['ddSubject'].get(),
                                                      d['ddExamCtgy'].get()),
                                                  25, 1, [3, 2, 1, 1],
                                                  clear_marks_info)
    frm_details.add_label("Division", "Division", 15, 1, [1, 3, 1, 1])
    d['ddDivision'] = frm_details.add_dropdown("ddDivision",
                                               db.get_division_list(),
                                               2, 1, [1, 4, 1, 1],
                                               clear_marks_info)
    frm_details.add_button("btnShowStudents", "Show", show_student_marks,
                           [2, 3, 1, 2])
    d['frm_marks'] = d['app'].main_frame.add_frame("Marks", 780, 380,
                                                   [2, 1, 1, 1])

    cols = (("Roll No", 60, "c"), ("Name", 250, "sw"), ("Marks", 60, "se"))
    d['treeview'] = d['frm_marks'].add_treeview("tview", 16, cols, [1, 1, 3, 1],
                                                handle_student_select)
    d['lblTotal'] = d['frm_marks'].add_label("lblTotal", "Total marks = N/A",
                                             18, 1, [1, 2, 1, 1])
    lblMarksNew = d['frm_marks'].add_label("lblMarksNew", "Enter new marks",
                                           18, 1, [2, 2, 1, 1])
    d['txtNewMarks'] = d['frm_marks'].add_text("txtNewMarks", "", 5, 1,
                                               [2, 3, 1, 1])
    d['txtNewMarks'].bind_return(handle_marks_enter_key_press)
    d['frm_marks'].add_button("btnSaveStudents", "Save", save_data,
                              [3, 2, 1, 1])

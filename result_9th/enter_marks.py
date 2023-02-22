from uihelper import MyApp, MyDropdown
from codehelper import fetch_sqlite_rows
from math import ceil

d = {}
d['page_length'] = 8


def clear_marks_info(*args, **kwargs):
    clear_marks_frame()
    d['marks_textbox_ar'] = []
    d['marks_list'] = []
    d['ddPageNo'].load_list(['1'])


def load_page(pageno):
    clear_marks_frame()
    start = (int(pageno) - 1) * d['page_length']
    end = start + d['page_length']
    d['marks_textbox_ar'] = []
    for i, row in enumerate(d['marks_list'][start:end]):
        d['frm_marks'].add_label(f"lblnm{i}", row[1], 25, 1, [i + 1, 1, 1, 1])
        if row[3] == -999:
            txtMarks = ""
        else:
            txtMarks = str(int(row[3]))
        txtbox = d['frm_marks'].add_text(f"txtbox{i}", txtMarks, 5, 1,
                                         [i + 1, 2, 1, 1])


def clear_marks_frame():
    if 'frm_marks' in d:
        d['frm_marks'].elm.destroy()
    d['frm_marks'] = d['app'].main_frame.add_frame("Marks", 780, 300,
                                                   [3, 1, 1, 1])


def refresh_page_count():
    page_ar = [x + 1 for x in
               range(ceil(len(d['marks_list']) / d['page_length']))]
    d['ddPageNo'].load_list(page_ar)


def show_student_marks(*args, **kwargs):
    get_student_marks()
    refresh_page_count()
    load_page(1)


def get_student_marks():
    qry = f"select a.student_id, a.student_name, b.exam_id, " \
          f"coalesce(b.marks,-999) " \
          f"from student_info a " \
          f"left outer join student_marks b " \
          f"on a.student_id = b.student_id " \
          f"left outer join exam_details c " \
          f"on b.exam_id = c.exam_id " \
          f"where c.subject = '{d['ddSubject'].get()}' " \
          f"and c.exam_category = '{d['ddExamCtgy'].get()}' " \
          f"and c.exam_sub_category = '{d['ddExamSubCtgy'].get()}' " \
          f"and a.division = '{d['ddDivision'].get()}'"
    d['marks_list'] = [tuple(x) for x in fetch_sqlite_rows(qry)]
    return d['marks_list']


def get_subject_list():
    return sorted([x[0] for x in fetch_sqlite_rows(
        "select subject from exam_details group by 1 ;")])


def handle_subject_change(subject):
    exam_ctgy_list = get_exam_category_list()
    d['ddExamCtgy'].load_list(exam_ctgy_list)
    handle_exam_category_change(d['ddExamCtgy'].get())
    clear_marks_info()


def get_exam_category_list():
    return [x[0] for x in fetch_sqlite_rows(
        f"select exam_category from exam_details where subject = '"
        f"{d['ddSubject'].get()}' group by 1 order by exam_id;")]


def handle_exam_category_change(exam_category):
    exam_sub_ctgy_list = get_exam_sub_category_list()
    d['ddExamSubCtgy'].load_list(exam_sub_ctgy_list)
    clear_marks_info()


def get_exam_sub_category_list():
    return [x[0] for x in fetch_sqlite_rows(
        f"select exam_sub_category from exam_details where subject = '"
        f"{d['ddSubject'].get()}' and exam_category = '"
        f"{d['ddExamCtgy'].get()}' "
        f"group by 1 order by exam_id;")]


def get_division_list():
    return sorted([x[0] for x in fetch_sqlite_rows(
        "select division from student_info group by 1 order by student_id;")])


def show_ui(app: MyApp):
    d['app'] = app
    app.clear_screen()
    frm_details = app.main_frame.add_frame("Details", 780, 160, [1, 1, 1, 1])

    frm_details.add_label("Subject", "Subject", 18, 1, [1, 1, 1, 1])

    d['ddSubject'] = frm_details.add_dropdown("ddSubject", get_subject_list(),
                                              25, 1, [1, 2, 1, 1],
                                              handle_subject_change)
    frm_details.add_label("Exam Category", "Exam Category", 18, 1, [2, 1, 1, 1])
    d['ddExamCtgy'] = frm_details.add_dropdown("ddExamCtgy",
                                               get_exam_category_list(),
                                               25, 1, [2, 2, 1, 1],
                                               handle_exam_category_change)
    frm_details.add_label("Exam Sub Category", "Exam Sub Category", 18, 1,
                          [3, 1, 1, 1])
    d['ddExamSubCtgy'] = frm_details.add_dropdown("ddExamSubCtgy",
                                                  get_exam_sub_category_list(),
                                                  25, 1, [3, 2, 1, 1],
                                                  clear_marks_info)
    frm_details.add_label("Division", "Division", 15, 1, [1, 3, 1, 1])
    d['ddDivision'] = frm_details.add_dropdown("ddDivision",
                                               get_division_list(),
                                               2, 1, [1, 4, 1, 1],
                                               clear_marks_info)
    frm_details.add_button("btnShowStudents", "Show", show_student_marks,
                           [2, 3, 1, 2])
    frm_navigate = app.main_frame.add_frame("Navigate", 780, 70, [2, 1, 1, 2])
    frm_navigate.add_label("Page", "Page", 6, 1, [1, 1, 1, 1])
    d['ddPageNo'] = frm_navigate.add_dropdown("ddPageNo", ["1"], 3, 1,
                                              [1, 2, 1, 1], load_page)
    frm_navigate.add_button("btnSaveStudents", "Save", lambda: None,
                            [1, 3, 1, 2])
    clear_marks_frame()

from uihelper import MyApp, MyDropdown
from codehelper import fetch_sqlite_rows

d = {}


def get_subject_list():
    return sorted([x[0] for x in fetch_sqlite_rows(
        "select subject from exam_details group by 1 ;")])


def handle_subject_change(subject):
    exam_ctgy_list = get_exam_category_list()
    d['ddExamCtgy'].load_list(exam_ctgy_list)
    handle_exam_category_change(d['ddExamCtgy'].get())


def get_exam_category_list():
    return [x[0] for x in fetch_sqlite_rows(
        f"select exam_category from exam_details where subject = '"
        f"{d['ddSubject'].get()}' group by 1 order by exam_id;")]


def handle_exam_category_change(exam_category):
    exam_sub_ctgy_list = get_exam_sub_category_list()
    d['ddExamSubCtgy'].load_list(exam_sub_ctgy_list)


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
                                                  lambda x: None)
    frm_details.add_label("Division", "Division", 15, 1, [1, 3, 1, 1])
    d['ddDivision'] = frm_details.add_dropdown("ddDivision",
                                                  get_division_list(),
                                                  2, 1, [1, 4, 1, 1],
                                                  lambda x: None)
    frm_details.add_button("btnShowStudents", "Show", lambda: None,
                           [2, 3, 1, 2])
    frm_details.add_button("btnSaveStudents", "Save", lambda: None,
                           [3, 3, 1, 2])

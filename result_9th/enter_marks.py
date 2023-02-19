from uihelper import MyApp
from codehelper import fetch_sqlite_rows


def get_subject_list():
    return sorted([x[0] for x in fetch_sqlite_rows(
        "select subject from exam_details group by 1 ;")])


def show_ui(app: MyApp):
    app.clear_screen()
    frm_details = app.main_frame.add_frame("Details", 780, 205, [1, 1, 1, 1])
    frm_details.add_label("Subject", "Subject", 18, 1, [1, 1, 1, 1])
    frm_details.add_label("Exam Category", "Exam Category", 18, 1, [2, 1, 1, 1])
    frm_details.add_label("Exam Sub Category", "Exam Sub Category", 18, 1,
                          [3, 1, 1, 1])
    frm_details.add_label("Division", "Division", 18, 1, [4, 1, 1, 1])
    frm_dtl_btn = frm_details.add_frame("--", 770, 55, [5, 1, 1, 2])
    frm_dtl_btn.add_button("btnShowStudents", "Show Students", lambda: None,
                           [1, 1, 1, 1])

    print(get_subject_list())

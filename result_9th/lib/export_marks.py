from lib import sql_template
from lib.codehelper import fetch_sqlite_rows
from lib.uihelper import MyApp

d = {}


def get_subject_list():
    qry = sql_template.get_subject_list
    return sorted([x[0] for x in fetch_sqlite_rows(qry, ())])


def get_division_list():
    qry = sql_template.get_division_list
    return sorted([x[0] for x in fetch_sqlite_rows(qry, ())])


def show_ui(app: MyApp):
    d['app'] = app
    app.clear_screen()
    frm_select = app.main_frame.add_frame("Select", 500, 160, [1, 1, 1, 1])
    frm_select.add_label("Subject", "Subject", 18, 1, [1, 1, 1, 1])
    d['ddSubject'] = frm_select.add_dropdown("ddSubject", get_subject_list(),
                                             25, 1, [1, 2, 1, 1], lambda x: 1)
    frm_select.add_label("Division", "Division", 18, 1, [2, 1, 1, 1])
    d['ddDivision'] = frm_select.add_dropdown("ddDivision", get_division_list(),
                                              25, 1, [2, 2, 1, 1], lambda x: 1)
    frm_select.add_button("btnExport", "Export", lambda: 1, [3, 2, 1, 2])

from lib.codehelper import backup_database, data_path, sqlite_exec_query
from lib import excelhelper, sql_template
from tkinter import messagebox
from lib.uihelper import MyApp
import random

d = {}


def do_update():
    backup_database(False)
    data = excelhelper.read_all_rows(
        f"{data_path}\\result_reference_data.xlsx", "student_info")
    qry = sql_template.student_info_delete
    sqlite_exec_query(qry, ())
    ar = []
    for row in data[1:]:
        ar.append(f"({row[0]},'{row[1]}',{row[2]},'{row[3]}')")
    qry = "insert into student_info values " + ",\n".join(ar)
    sqlite_exec_query(qry, ())


def update():
    do_update()
    messagebox.showinfo("Done !!", "Done !!")


def do_new_year():
    if not d['txtCode'].get() == d['val']:
        return
    d['txtCode'].set("")
    do_update()
    qry = sql_template.student_marks_delete
    sqlite_exec_query(qry, ())
    messagebox.showinfo("Done !!", "Done !!")


def new_year(app: MyApp):
    d['app'] = app
    app.clear_screen()
    d['val'] = str(random.randint(1111, 9999))
    frm_select = app.main_frame.add_frame("Confirm", 500, 140, [1, 1, 1, 1])
    frm_select.add_label("info", "This action will delete all marks. Enter "
                                 "code " + d['val'] + " to confirm", 50, 1,
                         [1, 1, 1, 1])
    d['txtCode'] = frm_select.add_text("txtCode", "", 5, 1, [2, 1, 1, 1])
    frm_select.add_button("btnConfirm", "Confirm", do_new_year, [3, 1, 1, 1])

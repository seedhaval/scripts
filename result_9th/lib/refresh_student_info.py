from lib.codehelper import backup_database, data_path, sqlite_exec_query
from lib import excelhelper, sql_template, db
from tkinter import messagebox
from lib.uihelper import MyApp
import random

d = {}


def do_update():
    backup_database(False)
    data = excelhelper.read_all_rows(
        f"{data_path}\\result_reference_data.xlsx", "student_info")
    db.student_info_delete()
    ar = []
    for row in data[1:]:
        ar.append(f"({row[0]},'{row[1]}',{row[2]},'{row[3]}','{row[4]}')")
    db.bulk_insert_student_info(ar)


def update():
    do_update()
    messagebox.showinfo("Done !!", "Done !!")


def do_new_year():
    if not d['txtCode'].get() == d['val']:
        return
    d['txtCode'].set("")
    do_update()
    db.student_marks_delete()
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


def update_reg():
    backup_database(False)
    db.create_reg_info_if_not_exists()
    data = excelhelper.read_all_rows(
        f"{data_path}\\result_reference_data.xlsx", "reg_info")
    db.reg_info_delete()
    ar = []
    for row in data[1:]:
        ar.append(f"({row[0]},{row[1].replace('ID:','')},{row[2]})")
    db.bulk_insert_reg_info(ar)

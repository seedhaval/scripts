import json
import os
import random
import re
import string
from collections import defaultdict
from tkinter import filedialog
from tkinter import messagebox

import openpyxl
from openpyxl.utils import get_column_letter

from lib import excelhelper
from lib import sql_template
from lib.codehelper import fetch_sqlite_rows, output_path, data_path, \
    sqlite_exec_query
from lib.excelhelper import Cell
from lib.uihelper import MyApp

d = {}


def load_data():
    qry = sql_template.get_students_in_div
    args = [d['ddDivision'].get()]
    d['studentMap'] = [tuple(x) for x in fetch_sqlite_rows(qry, args)]
    qry = sql_template.get_exam_info_for_subject
    args = [d['ddSubject'].get()]
    data = [tuple(x) for x in fetch_sqlite_rows(qry, args)]
    d['examMap'] = {x[0]: (x[1], x[2]) for x in data}
    qry = sql_template.get_marks_for_subject
    args = [d['ddSubject'].get()]
    data = [tuple(x) for x in fetch_sqlite_rows(qry, args)]
    md = defaultdict(dict)
    for examid, sid, marks in data:
        md[sid][str(examid)] = marks
    d['marksMap'] = md


def get_subject_list():
    qry = sql_template.get_subject_list
    return sorted([x[0] for x in fetch_sqlite_rows(qry, ())])


def get_division_list():
    qry = sql_template.get_division_list
    return sorted([x[0] for x in fetch_sqlite_rows(qry, ())])


def get_output_file_path():
    filenm = f"{d['ddDivision'].get()}_{d['ddSubject'].get()}"
    p = re.compile("[" + re.escape(string.punctuation) + " ]+")
    filenm = p.sub("_", filenm) + "_bulk_template.xlsx"
    return f"{output_path}\\{filenm}"


def load_config():
    with open(f"{data_path}\config.json", encoding='utf8') as f:
        return json.load(f)


def add_excel_base_columns(wb):
    sht = wb.active
    Cell(7, 1, sht).set("sid")
    Cell(7, 2, sht).set("हजेरी क्रमांक").wrap()
    sht.cell(7, 3).value = "विद्यार्थ्याचे नाव"
    sht.cell(9, 3).value = "ठेवलेले गुण"
    sht.column_dimensions["A"].width = 8
    sht.column_dimensions["B"].width = 8
    sht.column_dimensions["C"].width = 30
    sht.row_dimensions[7].height = 120
    for row in range(7, 10):
        for col in range(1, 4):
            Cell(row, col, sht).border()


def add_excel_header(wb: openpyxl.Workbook, cfg):
    sht = wb.active
    sht.cell(2, 2).value = cfg['school name']
    sht.cell(4, 2).value = "विषय"
    sht.cell(4, 3).value = d['ddSubject'].get()
    sht.cell(5, 2).value = "तुकडी"
    sht.cell(5, 3).value = d['ddDivision'].get()


def add_excel_student_info(wb):
    sht = wb.active
    for i, v in enumerate(d['studentMap']):
        sid, roll, nm = v
        Cell(10 + i, 1, sht).set(sid).border()
        Cell(10 + i, 2, sht).set(roll).border()
        Cell(10 + i, 3, sht).set(nm).wrap().border()


def excel_format_mark_cells(wb):
    sht = wb.active
    for r in range(len(d['studentMap'])):
        for c in range(len(d['examMap'])):
            Cell(10 + r, 4 + c, sht).border().unprotect()


def add_excel_exam_info(wb):
    sht = wb.active
    for i, examid in enumerate(sorted(d['examMap'].keys())):
        nm = d['examMap'][examid][0]
        total = d['examMap'][examid][1]
        Cell(7, 4 + i, sht).set(nm).border().verticalwrap()
        Cell(8, 4 + i, sht).set(examid).border()
        Cell(9, 4 + i, sht).set(total).border()
        sht.column_dimensions[get_column_letter(4 + i)].width = 6


def add_excel_marks(wb):
    sht = wb.active
    for ir, student in enumerate(d['studentMap']):
        for ic, examid in enumerate(sorted(d['examMap'].keys())):
            if student[0] in d['marksMap'] \
                    and str(examid) in d['marksMap'][student[0]]:
                Cell(10 + ir, 4 + ic, sht).set(
                    d['marksMap'][student[0]][str(examid)])


def populate_excel(wb, cfg):
    add_excel_header(wb, cfg)
    add_excel_base_columns(wb)
    load_data()
    add_excel_student_info(wb)
    add_excel_exam_info(wb)
    excel_format_mark_cells(wb)
    add_excel_marks(wb)


def protect_sheet(wb):
    sht = wb.active
    sht.protection.password = str(random.randint(10000, 99999))


def export_data():
    filepath = get_output_file_path()
    cfg = load_config()
    wb = openpyxl.Workbook()
    populate_excel(wb, cfg)
    protect_sheet(wb)
    wb.save(filepath)
    wb.close()
    os.startfile(filepath)


def import_data():
    file = filedialog.askopenfilename(initialdir=output_path)
    if not file:
        return
    data = excelhelper.read_all_rows(file, False)
    subject = data[3][2]
    division = data[4][2]
    examids = data[7][3:]
    studentids = [x[0] for x in data[9:]]
    if subject != d['ddSubject'].get() or division != d['ddDivision'].get():
        messagebox.showerror("Invalid file", "Invalid file")
        return
    out = []
    for ir, row in enumerate(data[9:]):
        for ic, col in enumerate(row[3:]):
            if str(col).strip() not in ('None', ''):
                out.append(f"({studentids[ir]}, {examids[ic]}, {col})")
    qry = sql_template.delete_marks_for_div_subject
    args = [d['ddSubject'].get(), d['ddDivision'].get()]
    sqlite_exec_query(qry, args)
    qry = "insert into student_marks values " + ",\n".join(out)
    sqlite_exec_query(qry, ())
    messagebox.showinfo("Done !!", "Done !!")


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
    frm_select.add_button("btnGenTemplate", "Generate Template", export_data,
                          [3, 1, 1, 1])
    frm_select.add_button("btnImport", "Import", import_data,
                          [3, 2, 1, 1])

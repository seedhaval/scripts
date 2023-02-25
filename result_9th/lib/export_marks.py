import json
import os
import re
import string

import openpyxl
from openpyxl.utils import get_column_letter
from collections import defaultdict

from lib import sql_template
from lib.codehelper import fetch_sqlite_rows, tm_sfx, output_path, data_path
from lib.excelhelper import Cell
from lib.uihelper import MyApp
from lib.calculatedmarks import calculate

d = {}


def calculate_marks():
    cols = [x['id'] for x in d['colInfo'] if x['type'] == 'calculated']
    for k, v in d['marksMap'].items():
        calculate(v, 'subset', cols)


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
    get_column_info()
    calculate_marks()


def get_subject_list():
    qry = sql_template.get_subject_list
    return sorted([x[0] for x in fetch_sqlite_rows(qry, ())])


def get_division_list():
    qry = sql_template.get_division_list
    return sorted([x[0] for x in fetch_sqlite_rows(qry, ())])


def get_output_file_path():
    filenm = f"{d['ddDivision'].get()}_{d['ddSubject'].get()}_{tm_sfx()}"
    p = re.compile("[" + re.escape(string.punctuation) + " ]+")
    filenm = p.sub("_", filenm) + ".xlsx"
    return f"{output_path}\\{filenm}"


def load_config():
    with open(f"{data_path}\config.json", encoding='utf8') as f:
        return json.load(f)


def add_excel_base_columns(wb):
    sht = wb.active
    Cell(7, 1, sht).set("अ. नं.")
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
        Cell(10 + i, 1, sht).set(i + 1).border()
        Cell(10 + i, 2, sht).set(roll).border()
        Cell(10 + i, 3, sht).set(nm).wrap().border()


def excel_format_mark_cells(wb):
    sht = wb.active
    for r in range(len(d['studentMap'])):
        for c in range(len(d['colInfo'])):
            Cell(10 + r, 4 + c, sht).border().color(d['colInfo'][c]['color'])


def add_excel_exam_info(wb):
    sht = wb.active
    for i, examcol in enumerate(d['colInfo']):
        if 'nm' in examcol:
            nm = examcol['nm']
            total = examcol['total']
        else:
            nm = d['examMap'][int(examcol['id'])][0]
            total = d['examMap'][int(examcol['id'])][1]
        alias = examcol.get('alias', '')
        clr = examcol['color']
        Cell(7, 4 + i, sht).set(nm).border().verticalwrap().color(clr)
        Cell(8, 4 + i, sht).set(alias).border().color(clr)
        Cell(9, 4 + i, sht).set(total).border().color(clr)
        sht.column_dimensions[get_column_letter(4 + i)].width = 6


def get_column_info():
    with open(data_path + "\export_columns.csv", encoding='utf8') as f:
        data = [x.strip().split(",") for x in f.readlines() if x.strip()]
    col_data = [x for x in data if x[0] == d['ddSubject'].get()][0]
    col_info = []
    for col in col_data[1:]:
        curd = {}
        ar = col.split(":")
        if col[0] in '123456789':
            curd['type'] = 'exam id'
            curd['id'] = ar[0]
            curd['color'] = '000000'
        else:
            curd['type'] = 'calculated'
            curd['id'] = ar[0]
            curd['total'] = int(ar[1])
            curd['nm'] = ar[2]
            curd['color'] = '0000FF'

        if curd['type'] == 'exam id' and len(ar) > 1:
            curd['alias'] = ar[1]
        if curd['type'] == 'calculated' and len(ar) > 3:
            curd['alias'] = ar[3]

        col_info.append(curd)

    d['colInfo'] = col_info


def add_excel_marks(wb):
    sht = wb.active
    for ir, student in enumerate(d['studentMap']):
        for ic, exam in enumerate(d['colInfo']):
            if student[0] in d['marksMap'] \
                    and exam['id'] in d['marksMap'][student[0]]:
                Cell(10+ir,4+ic,sht).set(d['marksMap'][student[0]][exam['id']])


def populate_excel(wb, cfg):
    add_excel_header(wb, cfg)
    add_excel_base_columns(wb)
    load_data()
    add_excel_student_info(wb)
    add_excel_exam_info(wb)
    excel_format_mark_cells(wb)
    add_excel_marks(wb)


def export_data():
    filepath = get_output_file_path()
    cfg = load_config()
    wb = openpyxl.Workbook()
    populate_excel(wb, cfg)
    wb.save(filepath)
    os.startfile(filepath)


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
    frm_select.add_button("btnExport", "Export", export_data, [3, 2, 1, 2])

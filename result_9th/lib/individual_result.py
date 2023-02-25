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


def set_column_widths(wb: openpyxl.Workbook):
    sht = wb.active
    col_widths = [4, 7, 29, 7, 11, 14]
    for i, v in enumerate(col_widths):
        sht.column_dimensions[get_column_letter(1 + i)].width = v


def draw_excel_template(wb, cfg, ir):
    sht = wb.active
    Cell(ir, 2, sht).set(cfg['iso text 1']).border().center()
    Cell(ir + 1, 2, sht).set(cfg['iso text 2']).border().center()
    Cell(ir + 2, 2, sht).set(cfg['school info 1']).border().center()
    Cell(ir + 3, 2, sht).set(cfg['school name']).border().center()
    Cell(ir + 4, 2, sht).set(cfg['year text']).border().center()
    sht.merge_cells(f"B{ir}:F{ir}")
    sht.merge_cells(f"B{ir + 1}:F{ir + 1}")
    sht.merge_cells(f"B{ir + 2}:F{ir + 2}")
    sht.merge_cells(f"B{ir + 3}:F{ir + 3}")
    sht.merge_cells(f"B{ir + 4}:F{ir + 4}")
    Cell(ir + 5, 2, sht).set("हजेरी नं.").border().center()
    Cell(ir + 5, 3, sht).border().center()
    Cell(ir + 5, 4, sht).set("इयत्ता ९ वी").border().center()
    Cell(ir + 5, 6, sht).border().center()
    sht.merge_cells(f"D{ir + 5}:E{ir + 5}")
    Cell(ir + 6, 2, sht).border()
    Cell(ir + 6, 3, sht).set("विद्यार्थ्याचे नाव").border()
    Cell(ir + 6, 4, sht).border().center()
    sht.merge_cells(f"D{ir + 6}:F{ir + 6}")
    for i, val in enumerate(
            ["", "विषय", "माध्यम", "ठेवलेले गुण", "मिळालेले गुण"]):
        Cell(ir + 7, 2 + i, sht).set(val).border().center()
    for i, val in enumerate(["मराठी", "हिंदी/संस्कृत", "इंग्रजी", "एकुण",
                             "गणित", "विज्ञान आणि तंत्रज्ञान", "एकुण",
                             "समाजशास्त्र/टेकनिकल(V2/V3)",
                             "आरोग्य व शा.शिक्षण", "स्व विकास व कला रसास्वाद",
                             "स्काऊट गाईड/NCC/RSP", "एकुण", "शेकडा गुण",
                             "शेरा"]):
        Cell(ir + i + 8, 3, sht).set(val).center().border()
    for i, val in enumerate(["भाषा विभाग", "", "", "", "गणित विज्ञान विभाग ",
                             "", "", "", "", "", "", "", "", ""]):
        Cell(ir + i + 8, 2, sht).set(val).center().border().wrap()
    for i, val in enumerate(
            ["मराठी ", "मराठी ", "मराठी ", "", "मराठी ", "मराठी ", "", "मराठी ",
             "मराठी ", "मराठी ", "मराठी ", "", " "]):
        Cell(ir + i + 8, 4, sht).set(val).center().border()
    for i, val in enumerate(
            [100, 100, 100, 300, 100, 100, 200, 100, "", "", "",
             600, ""]):
        Cell(ir + i + 8, 5, sht).set(val).center().border()
    for i in range(13):
        Cell(ir + i + 8, 6, sht).center().border()
    Cell(ir + 21, 4, sht).center().border()
    sht.merge_cells(f"B{ir + 8}:B{ir + 11}")
    sht.merge_cells(f"B{ir + 12}:B{ir + 14}")
    sht.merge_cells(f"D{ir + 21}:F{ir + 21}")


def draw_excel_populate_marks(wb, ir, student):
    sid, roll, nm = student
    sht = wb.active
    Cell(ir + 5, 3, sht).set(roll)
    Cell(ir + 5, 6, sht).set("तुकडी - " + d['ddDivision'].get())
    Cell(ir + 6, 4, sht).set(nm)
    if sid in d['marksMap'] and 'mar.6' in d['marksMap'][sid]:
        Cell(ir + 8, 6, sht).set(d['marksMap'][sid]['mar.6'])
    if sid in d['marksMap'] and 'mat.16' in d['marksMap'][sid]:
        Cell(ir + 12, 6, sht).set(d['marksMap'][sid]['mat.16'])


def calculate_marks():
    for k, v in d['marksMap'].items():
        calculate(v, 'all', ())


def load_data():
    qry = sql_template.get_students_in_div
    args = [d['ddDivision'].get()]
    d['studentMap'] = [tuple(x) for x in fetch_sqlite_rows(qry, args)]
    qry = sql_template.get_marks_for_all_subjects
    data = [tuple(x) for x in fetch_sqlite_rows(qry, args)]
    md = defaultdict(dict)
    for examid, sid, marks in data:
        md[sid][str(examid)] = marks
    d['marksMap'] = md
    calculate_marks()


def get_division_list():
    qry = sql_template.get_division_list
    return sorted([x[0] for x in fetch_sqlite_rows(qry, ())])


def get_output_file_path():
    filenm = f"{d['ddDivision'].get()}_individual_result_{tm_sfx()}.xlsx"
    return f"{output_path}\\{filenm}"


def load_config():
    with open(f"{data_path}\config.json", encoding='utf8') as f:
        return json.load(f)


def add_excel_result(wb, cfg):
    for i, student in enumerate(d['studentMap']):
        ir = (i * 27) + 1
        draw_excel_template(wb, cfg, ir)
        draw_excel_populate_marks(wb, ir, student)


def populate_excel(wb, cfg):
    load_data()
    set_column_widths(wb)
    add_excel_result(wb, cfg)


def generate_result():
    filepath = get_output_file_path()
    cfg = load_config()
    wb = openpyxl.Workbook()
    populate_excel(wb, cfg)
    wb.save(filepath)
    wb.close()
    os.startfile(filepath)


def show_ui(app: MyApp):
    d['app'] = app
    app.clear_screen()
    frm_select = app.main_frame.add_frame("Select", 250, 120, [1, 1, 1, 1])
    frm_select.add_label("Division", "Division", 12, 1, [1, 1, 1, 1])
    d['ddDivision'] = frm_select.add_dropdown("ddDivision", get_division_list(),
                                              5, 1, [1, 2, 1, 1], lambda x: 1)
    frm_select.add_button("btnGen", "Generate", generate_result, [2, 2, 1, 2])

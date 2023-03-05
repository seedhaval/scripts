import openpyxl

from lib import db
from lib.calculatedmarks import calculate
from lib.codehelper import data_path, get_safe_output_xls_path
from lib.excelhelper import Cell, load_template, save_close_and_start, \
    apply_template, apply_column_widths
from lib.uihelper import MyApp

d = {}


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
    d['studentMap'] = db.get_student_map(d['ddDivision'].get())
    d['marksMap'] = db.get_marks_map_for_all_subjects(d['ddDivision'].get())
    d['tmplt'] = load_template(data_path + "\\template.xlsx", "reportcard",
                               2, 2, 7, 33)
    calculate_marks()


def get_output_file_path():
    return get_safe_output_xls_path(f"{d['ddDivision'].get()}_report_card"
                                    , True)


def add_excel_result(wb):
    sht = wb.active
    for i, student in enumerate(d['studentMap']):
        ir = (i * 37) + 1
        apply_template(sht, d['tmplt'], 2, ir)
        # draw_excel_populate_marks(wb, ir, student)


def populate_excel(wb):
    sht = wb.active
    load_data()
    apply_column_widths(sht, 2, d['tmplt']['widths'])
    add_excel_result(wb)


def generate_result():
    filepath = get_output_file_path()
    wb = openpyxl.Workbook()
    populate_excel(wb)
    save_close_and_start(wb, filepath)


def show_ui(app: MyApp):
    d['app'] = app
    app.clear_screen()
    frm_select = app.main_frame.add_frame("Select", 250, 120, [1, 1, 1, 1])
    frm_select.add_label("Division", "Division", 12, 1, [1, 1, 1, 1])
    d['ddDivision'] = frm_select.add_dropdown("ddDivision",
                                              db.get_division_list(),
                                              5, 1, [1, 2, 1, 1], lambda x: 1)
    frm_select.add_button("btnGen", "Generate", generate_result, [2, 2, 1, 2])

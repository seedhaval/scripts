import openpyxl

from lib import db
from lib.calculatedmarks import calculate
from lib.codehelper import data_path, get_safe_output_xls_path
from lib.excelhelper import Cell, load_template, save_close_and_start, \
    apply_template, apply_column_widths, add_page_break
from lib.uihelper import MyApp

d = {}


def draw_excel_populate_marks(wb, ir, student):
    sid, roll, nm = student
    md = d['marksMap'][sid]
    sht = wb.active
    Cell(ir + 6, 3, sht).set(roll)
    Cell(ir + 6, 6, sht).set("तुकडी - " + d['ddDivision'].get())
    Cell(ir + 7, 4, sht).set(nm)
    Cell(ir + 9, 6, sht).set(md['fin.mar.r1'])
    Cell(ir + 10, 6, sht).set(md['fin.hin.r1'])
    Cell(ir + 11, 6, sht).set(md['fin.eng.r1'])
    Cell(ir + 12, 6, sht).set(md['fin.grp.l1'])
    Cell(ir + 13, 6, sht).set(md['fin.mat.r1'])
    Cell(ir + 14, 6, sht).set(md['fin.sci.r1'])
    Cell(ir + 15, 6, sht).set(md['fin.grp.l2'])
    Cell(ir + 16, 6, sht).set(md['fin.smj.r1'])
    Cell(ir + 17, 6, sht).set(md['fin.aro.l1'])
    Cell(ir + 18, 6, sht).set(md['fin.jals.l1'])
    Cell(ir + 19, 6, sht).set(md['fin.ncc.l1'])
    Cell(ir + 20, 6, sht).set(md['fin.total.l1'])
    Cell(ir + 21, 6, sht).set(md['fin.100.l1'])
    Cell(ir + 22, 4, sht).set(md['final.pass.status'])



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
        draw_excel_populate_marks(wb, ir, student)
        add_page_break(sht, ir + 35)


def populate_excel(wb):
    sht = wb.active
    load_data()
    apply_column_widths(sht, 1, [5, 10, 20, 12, 11, 12, 12])
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

import openpyxl

from lib import db
from lib.calculatedmarks import calculate
from lib.codehelper import data_path, get_safe_output_xls_path
from lib.excelhelper import Cell, load_template, save_close_and_start, \
    apply_template, apply_column_widths, add_page_break
from lib.uihelper import MyApp

d = {}


def draw_excel_populate_marks(wb, ir, student, left):
    sid, roll, nm = student
    md = d['marksMap'][sid]
    sht = wb.active
    Cell(ir + 4, left + 1, sht).set(roll)
    Cell(ir + 4, left + 4, sht).set("तुकडी - " + d['ddDivision'].get())
    Cell(ir + 5, left + 2, sht).set(nm)
    Cell(ir + 7, left + 4, sht).set(md['fin.mar.r1'])
    Cell(ir + 8, left + 4, sht).set(md['fin.hin.r1'])
    Cell(ir + 9, left + 4, sht).set(md['fin.eng.r1'])
    Cell(ir + 10, left + 4, sht).set(md['fin.grp.l1'])
    Cell(ir + 11, left + 4, sht).set(md['fin.mat.r1'])
    Cell(ir + 12, left + 4, sht).set(md['fin.sci.r1'])
    Cell(ir + 13, left + 4, sht).set(md['fin.grp.l2'])
    Cell(ir + 14, left + 4, sht).set(md['fin.smj.r1'])
    Cell(ir + 15, left + 4, sht).set(md['fin.aro.l1'])
    Cell(ir + 16, left + 4, sht).set(md['fin.jals.l1'])
    Cell(ir + 17, left + 4, sht).set(md['fin.ncc.l1'])
    Cell(ir + 18, left + 4, sht).set(md['fin.total.l1'])
    Cell(ir + 19, left + 4, sht).set(md['fin.100.l1'])
    Cell(ir + 20, left + 2, sht).set(md['final.pass.status'])



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
        ir = ((i//2) * 29) + 1
        print(ir)
        left = 2 if i%2 == 0 else 9
        apply_template(sht, d['tmplt'], left, ir)
        draw_excel_populate_marks(wb, ir, student, left)
        if i%2 == 1:
            add_page_break(sht, ir + 28)


def populate_excel(wb):
    sht = wb.active
    sht.set_printer_settings(paper_size=sht.PAPERSIZE_A4,
                             orientation='landscape')
    load_data()
    apply_column_widths(sht, 1, [2, 8, 15, 7, 7, 7, 10, 4, 8, 15, 7, 7, 7, 10])
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

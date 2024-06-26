from lib import enter_marks, export_marks, individual_result, \
    refresh_exam_info, refresh_student_info, bulk_import, result_tabular
from lib.codehelper import backup_database, restore_database
from lib.developer import get_column_ids
from lib.uihelper import MyApp

app = MyApp("Result", 800, 600)

menu_ar = [
    ["Marks", "Enter Marks", lambda: enter_marks.show_ui(app)],
    ["Marks", "Export", lambda: export_marks.show_ui(app)],
    ['Marks', 'Bulk import', lambda: bulk_import.show_ui(app)],
    ["Result", "घटक चाचणी १",
     lambda: result_tabular.show_ui(app, "घटक चाचणी १")],
    ["Result", "घटक चाचणी २",
     lambda: result_tabular.show_ui(app, "घटक चाचणी २")],
    ["Result", "प्रथम सत्र",
     lambda: result_tabular.show_ui(app, "प्रथम सत्र")],
    ["Result", "द्वितीय सत्र",
     lambda: result_tabular.show_ui(app, "द्वितीय सत्र")],
    ["Result", "Final",
     lambda: result_tabular.show_ui(app, "final")],
    ["Result", "Report card", lambda: individual_result.show_ui(app)],
    ["Reference Data", "Refresh exam info", refresh_exam_info.do],
    ["Reference Data", "Refresh student info - Change",
     refresh_student_info.update],
    ["Reference Data", "Refresh student info - New year",
     lambda: refresh_student_info.new_year(app)],
    ['Reference Data', "Refresh Registration info",
     refresh_student_info.update_reg],
    ["Database", "Backup", lambda: backup_database(True)],
    ["Database", "Restore", restore_database],
    ["Developer", "Get Column IDs", get_column_ids]
]

app.add_menu(menu_ar)
app.clear_screen()
app.show()

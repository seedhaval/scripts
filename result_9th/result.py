from lib import enter_marks, export_marks, individual_result, \
    refresh_exam_info, refresh_student_info
from lib.codehelper import backup_database
from lib.uihelper import MyApp

app = MyApp("Result", 800, 600)

menu_ar = [
    ["Marks", "Enter Marks", lambda: enter_marks.show_ui(app)],
    ["Marks", "Export", lambda: export_marks.show_ui(app)],
    ["Result", "Individual Result", lambda: individual_result.show_ui(app)],
    ["Result", "Combined Result", lambda: 1],
    ["Reference Data", "Refresh exam info", refresh_exam_info.do],
    ["Reference Data", "Refresh student info - Change",
     refresh_student_info.update],
    ["Reference Data", "Refresh student info - New year",
     lambda: refresh_student_info.new_year(app)],
    ["Database", "Backup", lambda: backup_database(True)],
    ["Database", "Restore", lambda: 1]
]

app.add_menu(menu_ar)
app.clear_screen()
app.show()

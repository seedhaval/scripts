from lib import enter_marks, export_marks, individual_result
from lib.codehelper import backup_database
from lib.uihelper import MyApp

app = MyApp("Result", 800, 600)

menu_ar = [
    ["Marks", "Enter Marks", lambda: enter_marks.show_ui(app)],
    ["Marks", "Export", lambda: export_marks.show_ui(app)],
    ["Result", "Individual Result", lambda: individual_result.show_ui(app)],
    ["Result", "Combined Result", lambda: 1],
    ["Reference Data", "Refresh exam info", lambda: 1],
    ["Reference Data", "Refresh student info", lambda: 1],
    ["Database", "Backup", backup_database],
    ["Database", "Restore", lambda: 1]
]

app.add_menu(menu_ar)
app.clear_screen()
app.show()

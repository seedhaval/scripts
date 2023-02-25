from lib import enter_marks
from lib.codehelper import backup_database
from lib.uihelper import MyApp

app = MyApp("Result", 800, 600)

menu_ar = [
    ["Marks", "Enter Marks", lambda: enter_marks.show_ui(app)],
    ["Database", "Backup", backup_database]
]

app.add_menu(menu_ar)
app.clear_screen()
app.show()

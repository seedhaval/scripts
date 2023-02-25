from lib.uihelper import MyApp
from lib import enter_marks

app = MyApp("Result", 800, 600)

menu_ar = [
    ["Marks", "Enter Marks", lambda: enter_marks.show_ui(app)],
    ["Database", "Backup", lambda: None]
]

app.add_menu(menu_ar)
app.clear_screen()
app.show()

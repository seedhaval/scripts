from uihelper import MyApp
from uihelper import Menu
import enter_marks

app = MyApp("Result", 800, 600)
menubar = Menu(app.top)
app.top.config(menu=menubar)

marks_menu = Menu(menubar, tearoff=False)
marks_menu.add_command(label="Enter marks",
                       command=lambda: enter_marks.show_ui(app))
menubar.add_cascade(label="Marks", menu=marks_menu)

app.clear_screen()
app.show()

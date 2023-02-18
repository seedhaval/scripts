from uihelper import MyApp
from uihelper import Menu

app = MyApp("Result", 800, 600)
menubar = Menu(app.top)
app.top.config(menu=menubar)

marks_menu = Menu(menubar, tearoff=False)
marks_menu.add_command(label="Enter marks", command=lambda: None)
menubar.add_cascade(label="Marks", menu=marks_menu)

app.show()

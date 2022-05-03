import commonutil.helper as helper
import commonutil.tkhelper as tkhelper

app = tkhelper.MyApp()
menubar = tkhelper.Menu(app.top)

filemenu = tkhelper.Menu(menubar, tearoff=0)
filemenu.add_command(label="Create DB", command=helper.dummy)
filemenu.add_command(label="Exit", command=exit)
menubar.add_cascade(label="Edit", menu=filemenu)

app.top.config(menu=menubar)

app.show()

from tkinter import *


class MyApp:
    def __init__(self):
        self.top = Tk()
        self.top.attributes('-fullscreen', True)

    def show(self):
        self.top.mainloop()

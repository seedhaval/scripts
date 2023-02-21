import os
import openpyxl

from tkinter import *
from pathlib import Path

def pos(elm, pos_ar):
    row, col, rowspan, colspan = pos_ar
    elm.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, padx=5,
             pady=5)

def get_desktop_path():
    userprofile = Path(os.environ['USERPROFILE'])
    onedrivepth = list(userprofile.glob("OneDrive*/Desktop"))
    if onedrivepth:
        return onedrivepth[0]
    else:
        return str(userprofile / "Desktop")


def generate_excel(*args, **kwargs):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.cell(row=2,column=2,value="नववीचा निकाल")
    wb.save(f"{desktop}/test_dvs_20230218.xlsx")

desktop = get_desktop_path()

top = Tk()
top.title("test")
top.grid_propagate(False)
top.option_add("*font", "verdana 12")
top.geometry(f'400x400+10+10')
elm = Button(top, text="एक्सेल तयार करा", command=generate_excel)
pos(elm, [1,1,1,1])
top.mainloop()



import os
import random

import openpyxl
from openpyxl.styles import Alignment, Protection
from openpyxl.styles import Font
from openpyxl.styles.borders import Border, Side

thin_border = Border(left=Side(style='thin'),
                     right=Side(style='thin'),
                     top=Side(style='thin'),
                     bottom=Side(style='thin'))


class Cell:
    def __init__(self, row, col, sht):
        self.cell = sht.cell(row, col)
        self.sht = sht
        self.row = row
        self.col = col

    def wrap(self):
        self.cell.alignment = Alignment(wrap_text=True)
        return self

    def verticalwrap(self):
        self.cell.alignment = Alignment(wrap_text=True, textRotation=90)
        return self

    def center(self):
        self.cell.alignment = Alignment(horizontal='center')
        return self

    def color(self, clr):
        self.cell.font = Font(color=clr)
        return self

    def set(self, v):
        self.cell.value = v
        return self

    def border(self):
        self.cell.border = thin_border
        return self

    def unprotect(self):
        self.cell.protection = Protection(locked=False)


def read_all_rows(fl, shtnm):
    out = []
    wb = openpyxl.load_workbook(fl)
    if shtnm:
        sht = wb[shtnm]
    else:
        sht = wb.worksheets[0]
    for r in range(sht.max_row):
        row = []
        for c in range(sht.max_column):
            row.append(sht.cell(r + 1, c + 1).value)
        out.append(row)
    wb.close()
    return out

def protect_sheet(wb):
    sht = wb.active
    sht.protection.password = str(random.randint(10000, 99999))


def save_close_and_start(wb, filepath):
    wb.save(filepath)
    wb.close()
    os.startfile(filepath)

def add_table(sht, left, top, ar):
    for ir, row in enumerate(ar):
        for ic, col in enumerate(row):
            sht.cell(top+ir, left+ic).value = col

def all_borders(sht, left, top, right, bottom):
    for ir in range(top, bottom+1):
        for ic in range(left, right + 1):
            sht.cell(ir, ic).border = thin_border
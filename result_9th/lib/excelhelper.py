from openpyxl.styles import Alignment
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
        self.cell.font = Font(color = clr)
        return self

    def set(self, v):
        self.cell.value = v
        return self

    def border(self):
        self.cell.border = thin_border
        return self




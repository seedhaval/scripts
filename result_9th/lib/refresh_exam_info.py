from tkinter import messagebox

from lib import excelhelper, db
from lib.codehelper import backup_database, data_path


def do():
    backup_database(False)
    data = excelhelper.read_all_rows(
    f"{data_path}\\result_reference_data.xlsx", "exam_details")
    db.exam_details_delete()
    ar = []
    for row in data[1:]:
        ar.append( f"({row[0]},'{row[1]}','{row[2]}','{row[3]}',{row[4]})")
    db.bulk_insert_exam_details(ar)
    messagebox.showinfo("Done !!", "Done !!")

from lib.codehelper import backup_database, data_path, sqlite_exec_query
from lib import excelhelper, sql_template
from tkinter import messagebox

def do():
    backup_database(False)
    data = excelhelper.read_all_rows(
    f"{data_path}\\result_reference_data.xlsx", "exam_details")
    qry = sql_template.exam_details_delete
    sqlite_exec_query(qry, ())
    ar = []
    for row in data[1:]:
        ar.append( f"({row[0]},'{row[1]}','{row[2]}','{row[3]}',{row[4]})")
    qry = "insert into exam_details values " + ",\n".join(ar)
    sqlite_exec_query(qry, ())
    messagebox.showinfo("Done !!", "Done !!")

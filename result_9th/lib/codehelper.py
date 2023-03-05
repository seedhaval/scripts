import json
import os
import re
import shutil
import sqlite3
import string
import subprocess
from datetime import datetime
from pathlib import Path
from tkinter import filedialog


def sqlite_exec_query(qry, args):
    conn = sqlite3.connect(db_path)
    conn.execute(qry, args)
    conn.commit()
    conn.close()


def fetch_sqlite_rows(qry, args):
    conn = sqlite3.connect(db_path)
    cursor = conn.execute(qry, args)
    out = []
    for row in cursor:
        out.append([x for x in row])
    conn.close()
    return out


def tm_sfx():
    return datetime.now().strftime("%Y_%m_%d_%H_%M_%S")


def backup_database(show):
    output_file = str(Path(output_path) / f"result_{tm_sfx()}.db")
    shutil.copy(db_path, output_file)
    if show:
        subprocess.Popen(r'explorer /select,"' + output_file + '"')


def restore_database():
    file = filedialog.askopenfilename(initialdir=output_path)
    backup_database(False)
    if file:
        shutil.copy(file, db_path)


def load_config():
    with open(f"{data_path}\config.json", encoding='utf8') as f:
        return json.load(f)


def get_safe_output_xls_path(nm, add_tm):
    filenm = f"{nm}"
    if add_tm == True:
        filenm += f"_{tm_sfx()}"
    p = re.compile("[" + re.escape(string.punctuation) + " ]+")
    filenm = p.sub("_", filenm) + ".xlsx"
    return f"{output_path}\\{filenm}"


def get_column_config_for_subject(subject):
    with open(data_path + "\\export_columns.csv", encoding='utf8') as f:
        data = [x.strip().split(",") for x in f.readlines() if x.strip()]
    col_data = [x for x in data if x[0] == subject][0]
    col_info = []
    for col in col_data[1:]:
        curd = {}
        ar = col.split(":")
        if col[0] in '123456789':
            curd['type'] = 'exam id'
            curd['id'] = ar[0]
            if len(ar) > 2:
                curd['nm'] = ar[2]
            if len(ar) > 3:
                curd['total'] = int(ar[3])
            curd['color'] = '000000'
        else:
            curd['type'] = 'calculated'
            curd['id'] = ar[0]
            curd['total'] = int(ar[1]) if ar[1].strip() != '' else ''
            curd['nm'] = ar[2]
            curd['color'] = '0000FF'

        if curd['type'] == 'exam id' and len(ar) > 1:
            curd['alias'] = ar[1]
        if curd['type'] == 'calculated' and len(ar) > 3:
            curd['alias'] = ar[3]

        col_info.append(curd)
    return col_info


app_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
db_path = str(Path(app_path) / "data/results.db")
data_path = str(Path(app_path) / "data")
output_path = str(Path(app_path) / "output")
cfg = load_config()

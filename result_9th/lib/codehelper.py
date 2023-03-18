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
    with open(data_path + "\\export_columns.json", encoding='utf8') as f:
        data = json.load(f)
    col_data = data[subject]
    col_info = []
    for col in col_data:
        curd = col
        if curd['type'] == 'exam id':
            curd['color'] = '000000'
        else:
            curd['color'] = '0000FF'
        col_info.append(curd)
    return col_info


app_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
db_path = str(Path(app_path) / "data/results.db")
data_path = str(Path(app_path) / "data")
output_path = str(Path(app_path) / "output")
cfg = load_config()

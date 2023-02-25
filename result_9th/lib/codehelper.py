import os
import shutil
import sqlite3
import subprocess
from datetime import datetime
from pathlib import Path


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


app_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
db_path = str(Path(app_path) / "data/results.db")
data_path = str(Path(app_path) / "data")
output_path = str(Path(app_path) / "output")

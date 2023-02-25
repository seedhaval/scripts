from pathlib import Path
import os
import sqlite3


def fetch_sqlite_rows(qry):
    conn = sqlite3.connect(db_path)
    cursor = conn.execute(qry)
    out = []
    for row in cursor:
        out.append([x for x in row])
    conn.close()
    return out


app_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
db_path = str(Path(app_path) / "data/results.db")
data_path = str(Path(app_path) / "data")
output_path = str(Path(app_path) / "output")

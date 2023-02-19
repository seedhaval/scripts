from pathlib import Path
import os
import sqlite3


def get_desktop_path():
    userprofile = Path(os.environ['USERPROFILE'])
    onedrivepth = list(userprofile.glob("OneDrive*/Desktop"))
    if onedrivepth:
        return onedrivepth[0]
    else:
        return str(userprofile / "Desktop")

def fetch_sqlite_rows(qry):
    conn = sqlite3.connect(db_path)
    cursor = conn.execute(qry)
    out = []
    for row in cursor:
        out.append([x for x in row])
    conn.close()
    return out

desktop_path = get_desktop_path()
app_path = os.path.dirname(os.path.realpath(__file__))
db_path = str(Path(app_path) / "data/results.db")

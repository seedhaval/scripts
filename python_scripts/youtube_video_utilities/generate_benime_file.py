import os
import shutil
from zipfile import ZipFile
from pathlib import Path
import re

tmplt_fldr = r"D:\Documents\notes_doodle\benime_template"
inp_fldr = r"D:\Documents\notes_doodle"


def generate(inp_fl):
    out_fldr = r"D:\Documents\notes_doodle" + "\\" + inp_fl

    with open(tmplt_fldr + "//benime_document_parent.json") as f:
        out = f.read()

    with open(inp_fl + ".txt") as f:
        data = [x.strip() for x in f.readlines() if x.strip()]
    if data[-1].startswith("~"):
        return

    for i, ln in enumerate(data):
        ln = ln.replace("\\", "\\\\").replace('"', '\\"')
        if i % 6 == 0:
            t = i // 6
            fmt = "xt%s" % (t + 1)
        else:
            s = i // 6
            p = i % 6
            fmt = "xs%sp%s" % (s + 1, p)
        out = out.replace('"' + fmt + '"', '"' + ln + '"')

    os.mkdir(out_fldr)
    shutil.copyfile(tmplt_fldr + "//thumbnail.png",
                    out_fldr + "//thumbnail.png")
    with open(out_fldr + "//" + "benime_document_parent.json", "w") as f:
        f.write(out)

    zipfl = inp_fl + ".zip"

    with ZipFile(zipfl, 'w') as zip:
        for path, directories, files in os.walk(out_fldr):
            for file in files:
                file_name = os.path.join(path, file)
                zip.write(file_name, arcname=file)

    shutil.copy(zipfl, r"G:\My Drive\Home\notes")
    shutil.rmtree(out_fldr)
    base_nm = re.sub(r'_\d+$', '', inp_fl)
    cmplt_fldr = "completed/" + base_nm
    os.makedirs(cmplt_fldr)
    shutil.move(zipfl, cmplt_fldr + "/" + inp_fl + ".zip")
    shutil.move(inp_fl + ".txt", cmplt_fldr + "/" + inp_fl + ".txt")


def main():
    os.chdir(inp_fldr)
    for fl in Path(inp_fldr).glob("*.txt"):
        generate(fl.stem)

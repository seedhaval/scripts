import os
import shutil
from zipfile import ZipFile

tmplt_fldr = r"D:\Documents\notes_doodle\benime_template"
inp_fldr = r"D:\Documents\notes_doodle"

os.chdir(inp_fldr)

inp_fl = input("Enter file name : ")
out_fldr = r"D:\Documents\notes_doodle" + "\\" + inp_fl

with open(tmplt_fldr + "//benime_document_parent.json") as f:
    out = f.read()

with open(inp_fl + ".txt") as f:
    data = [x.strip() for x in f.readlines() if x.strip()]

for i, ln in enumerate(data):
    if i % 6 == 0:
        t = i // 6
        fmt = "xt%s" % (t + 1)
    else:
        s = i // 6
        p = i % 6
        fmt = "xs%sp%s" % (s + 1, p)
    out = out.replace('"' + fmt + '"', '"' + ln + '"')

os.mkdir(out_fldr)
shutil.copyfile(tmplt_fldr + "//thumbnail.png", out_fldr + "//thumbnail.png")
with open(out_fldr + "//" + "benime_document_parent.json", "w") as f:
    f.write(out)

zipfl = inp_fl + ".zip"

with ZipFile(zipfl, 'w') as zip:
    for path, directories, files in os.walk(out_fldr):
        for file in files:
            file_name = os.path.join(path, file)
            zip.write(file_name,arcname=file)

shutil.copy(zipfl,r"G:\My Drive\Home\notes")

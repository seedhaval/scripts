from typing import List
from python_scripts.commonutil.helper import get_choice_from_user, File
import os
import shutil

base_dir = r"C:\Users\Dell\OneDrive\Documents"
sprt_dir = base_dir + r"\Python programming for spiritual growth"
wrksht_dir = base_dir + r"\Python create puzzles"
tmplt_dir = base_dir + r"\template"

def main():
    ch = get_choice_from_user("Select category",["Spiritual growth","Student Worksheet"])
    nm = input("Enter name : ")
    if ch == "Student Worksheet":
        proj_dir = wrksht_dir + "\\" + nm.replace(" ", "_")
        os.mkdir(proj_dir)
        info_txt = File( tmplt_dir + r"\info_wrksht.txt").read()
        info_txt = info_txt.replace("$name",nm)
        File( proj_dir + r"\info.txt").write(info_txt)
        shutil.copy(tmplt_dir+r"\images.pptx",proj_dir)




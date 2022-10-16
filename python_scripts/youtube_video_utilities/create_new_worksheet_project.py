from typing import List
from python_scripts.commonutil.helper import get_choice_from_user, File
import os
import shutil

wrksht_dir = r"D:\Documents\Python create puzzles"
tmplt_dir = r"C:\Users\Dell\OneDrive\Documents\template"

def main():
    nm = input("Enter project name : ")
    proj_dir = wrksht_dir + "\\" + nm.replace(" ", "_")
    os.mkdir(proj_dir)
    info_txt = File( tmplt_dir + r"\info_wrksht.txt").read()
    info_txt = info_txt.replace("$name",nm)
    File( proj_dir + r"\info.txt").write(info_txt)
    shutil.copy(tmplt_dir+r"\worksheet_images.pptx",proj_dir)

if __name__ == "__main__":
    main()


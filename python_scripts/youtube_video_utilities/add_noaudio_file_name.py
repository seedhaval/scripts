from pathlib import Path
import os
import shutil

def main():
    os.chdir(r"D:\Documents\notes_doodle")
    for fl in [x.name for x in Path('.').glob("*.mp4")]:
        if '_noaudio' not in fl:
            shutil.move(fl,fl.replace(".mp4","_noaudio.mp4"))


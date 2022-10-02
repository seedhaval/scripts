import shutil
from pathlib import Path
import os
base_fl = "audacity_template.aup3"

def main():
    os.chdir(r"D:\Documents\notes_doodle")
    for fl in Path('.').glob("*_noaudio.mp4"):
        shutil.copy(base_fl,fl.stem.replace("_noaudio","")+".aup3")

if __name__ == "__main__":
    main()
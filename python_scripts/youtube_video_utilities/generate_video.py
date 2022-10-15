import subprocess
import os
from pathlib import Path
import re
import shutil


def generate(fl):
    prcs = subprocess.Popen(['ffmpeg', '-i', fl + '_noaudio.mp4', '-i',
                             fl + '.wav', '-map', '0:v', '-map', '1:a',
                             '-c:v', 'copy', '-shortest', fl + '.mp4'])
    prcs.wait()
    if prcs.returncode != 0:
        return prcs.returncode
    base_nm = re.sub(r'_\d+$', '', fl)
    part = re.findall(r'\d+$', fl)[0]
    cmplt_fldr = "completed/" + base_nm
    with open(cmplt_fldr + "/" + fl + ".txt") as f:
        title = f.readlines()[0].strip()
    shutil.move(fl + ".wav", cmplt_fldr + "/" + fl + ".wav")
    shutil.move(fl + "_noaudio.mp4", cmplt_fldr + "/" + fl + "_noaudio.mp4")
    shutil.copy(fl + ".mp4", cmplt_fldr + "/" + fl + ".mp4")
    os.remove(fl + ".aup3")
    shutil.move(fl + ".mp4", "Revision of " + title + " - " + part + ".mp4")
    return 0


def main():
    os.chdir(r'D:\Documents\notes_doodle')
    for fl in Path('.').glob('*.wav'):
        rc = generate(fl.stem)
        if rc != 0:
            return


if __name__ == "__main__":
    main()

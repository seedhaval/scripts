import subprocess
import os
from pathlib import Path

def generate(fl):
    subprocess.check_output( ['ffmpeg', '-i', fl+'_noaudio.mp4', '-i', fl+'.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-shortest', fl+'.mp4'] )

    input('Press enter key to continue')

def main():
    os.chdir(r'D:\Documents\notes_doodle')
    for fl in Path('.').glob('*.wav'):
        generate(fl.stem)

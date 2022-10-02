import subprocess
import os

def main():
    os.chdir(r'D:\Documents\notes_doodle')
    fl = input("Enter file name : ").strip()
    subprocess.check_output( ['ffmpeg', '-i', fl+'_noaudio.mp4', '-i', fl+'.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-shortest', fl+'.mp4'] )

    input('Press enter key to continue')
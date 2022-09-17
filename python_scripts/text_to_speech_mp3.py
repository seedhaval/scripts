import pyttsx3
import subprocess
from datetime import datetime
engine = pyttsx3.init()

txt = """
Here we define different components for the widget.
c v r is the container frame.
label contains the question.
There are buttons for add, edit and delete.
l b is the actual listbox.
""".strip()
engine.setProperty('rate',150)
engine.setProperty('voice', engine.getProperty('voices')[0].id)
engine.save_to_file(txt,r'C:\Users\Dell\OneDrive\Documents\Sound Recordings\out.mp3')
engine.runAndWait()
subprocess.Popen([r'C:\Users\Dell\Downloads\archive\ffmpeg-2022-08-25-git-9bf9d42d01-full_build\bin\ffmpeg.exe', '-i', r'C:\Users\Dell\OneDrive\Documents\Sound Recordings\out.mp3', '-c:a', 'aac', r'C:\Users\Dell\OneDrive\Documents\Sound Recordings\%s.m4a' % datetime.now().strftime('%Y_%m_%d_%H_%M_%S')]).wait()
engine.say(txt)
engine.runAndWait()



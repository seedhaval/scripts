import pyttsx3
import time

num_cycle = 3
pause_sec = 3

engine = pyttsx3.init()
for i in range(num_cycle):
    engine.say("breathe in")
    engine.runAndWait()
    time.sleep(pause_sec)
    engine.say("breathe out")
    engine.runAndWait()
    time.sleep(pause_sec)

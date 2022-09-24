import winsound
import time

num_iter = 108
pause_sec = 3

for i in range(num_iter):
    winsound.PlaySound(r"C:\Users\Dell\OneDrive\Documents\Sound Recordings\test.wav", winsound.SND_FILENAME)
    time.sleep(pause_sec)

import pyttsx3
import random
import time

engine = pyttsx3.init()
engine.say("I will be counting numbers in reverse order. You will have to identify what numbers I have skipped")
engine.runAndWait()

strt = random.randint(30, 99)
numiter = random.randint(20, 24)
numblnk = random.randint(3, 4)

ar = list(range(strt, strt - numiter, -1))
possible_blank = ar[1:-1]
random.shuffle(possible_blank)
blnk = possible_blank[:random.randint(3, 4)]

for num in [x for x in ar if x not in blnk]:
    engine.say(str(num))
    engine.runAndWait()
    time.sleep(random.randint(3, 5))

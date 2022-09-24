import tkhelper
import random

strt = random.randint(30, 99)
numiter = random.randint(20, 24)
numblnk = random.randint(3, 4)
curidx = 0

ar = list(range(strt, strt - numiter, -1))
possible_blank = ar[1:-1]
random.shuffle(possible_blank)
blnk = possible_blank[:random.randint(3, 4)]
ar = [x for x in ar if x not in blnk]

def show_next_number():
    global curidx
    lbl.set(ar[curidx])
    curidx += 1
    if curidx >= len(ar):
        app.top.destroy()
    app.top.after(random.randint(3000, 5000), show_next_number)

app = tkhelper.MyApp("Come back to present moment",width=200,height=200)
fr = app.add_frame("",190,190,[1,1,1,1])
lbl = fr.add_label("","",4,2,[1,1,1,1])
lbl.set_font_size(48)

show_next_number()
app.show()

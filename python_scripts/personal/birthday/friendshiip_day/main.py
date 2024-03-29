from tkinter import *
from fdhelper import MyApp, Scene

obj = {}
scn = []
scn_id = 0


def load_window():
    fr = app.add_frame('Enter Details', width=880, height=630, xy=[10, 10])
    obj['lbl1'] = fr.add_label('Name', width=12, height=1, xy=[50, 50])
    obj['txt1'] = fr.add_text('John Smith', width=10, height=1, xy=[400, 50])
    obj['lbl2'] = fr.add_label('Gender', width=12, height=1, xy=[50, 150])
    obj['dd1'] = fr.add_dropdown(['Male', 'Female'], 'Male', xy=[400, 140])
    obj['lbl3'] = fr.add_label('Age', width=12, height=1, xy=[50, 250])
    obj['txt2'] = fr.add_text('57', width=10, height=1, xy=[400, 250])
    obj['lbl4'] = fr.add_label('City', width=12, height=1, xy=[50, 350])
    obj['txt3'] = fr.add_text('Chennai', width=10, height=1, xy=[400, 350])
    obj['btn1'] = fr.add_button('Submit', cb=None, xy=[300, 450])
    obj['lblovr'] = fr.add_label('To all the text boxes', width=32, height=3, xy=[10, 150])
    obj['lblovr'].hide()


def load_scenes():
    scn.append(Scene(obj, 2000))
    scn[-1].set_show_once('lblovr', 'To all the Text Boxes', 2000)
    scn.append(Scene(obj, 2000))
    scn[-1].set_flash('txt1 txt2 txt3'.split(), '#368BC1', 200)

    scn.append(Scene(obj, 2000))
    scn[-1].set_show_once('lblovr', 'And to all the Drop Downs', 2000)
    scn.append(Scene(obj, 2000))
    scn[-1].set_flash(['dd1'], '#FBB917', 200)

    scn.append(Scene(obj, 2000))
    scn[-1].set_show_once('lblovr', 'And to all the Labels', 2000)
    scn.append(Scene(obj, 2000))
    scn[-1].set_flash('lbl1 lbl2 lbl3 lbl4'.split(), '#B87333', 200)

    scn.append(Scene(obj, 2000))
    scn[-1].set_show_once('lblovr', 'And to all the Buttons', 2000)
    scn.append(Scene(obj, 2000))
    scn[-1].set_flash(['btn1'], '#FF8040', 200)

    scn.append(Scene(obj, 1))
    scn[-1].set_show_once('lblovr', 'Take a break', 2000)
    scn.append(Scene(obj, 1))
    scn[-1].set_show_once('lblovr', 'And raise a toast', 2000)
    scn.append(Scene(obj, 1))
    scn[-1].set_show_once('lblovr', 'For my best friend ...', 2000)
    scn.append(Scene(obj, 4000))
    scn[-1].set_show_once('lblovr', 'Mukesh !!!', 2000)

    scn.append(Scene(obj, 2000))
    scn[-1].set_move({
        'lbl4': (100, 50)
        , 'dd1': (450, 40)
        , 'lbl1': (50, 150)
        , 'lbl2': (300, 150)
        , 'lbl3': (550, 150)
        , 'txt1': (50, 250)
        , 'txt2': (300, 250)
        , 'txt3': (550, 250)
        , 'btn1': (300, 350)})
    scn.append(Scene(obj, 4000))
    scn[-1].set_change_text(
        (('lbl4', '***')
         , ('dd1', '***')
         , ('lbl1', 'Wish')
         , ('lbl2', 'You')
         , ('lbl3', 'A')
         , ('txt1', 'Happy')
         , ('txt2', 'Friendship')
         , ('txt3', 'Day')
         , ('btn1', 'Mukesh !!!')), 400)

    scn.append(Scene(obj, 2000))
    scn[-1].set_move({
        'lbl1': (50, 150)
        , 'lbl2': (300, 150)
        , 'lbl3': (550, 150)
        , 'txt1': (50, 250)
        , 'txt2': (300, 250)
        , 'txt3': (550, 250)
        ,'lbl4': (50, 350)
        , 'btn1': (300, 330)
        , 'dd1': (550, 340)})
    scn.append(Scene(obj, 4000))
    scn[-1].set_change_text(
        (('lbl1','I')
        ,('lbl2', 'am')
        ,('lbl3', 'blessed')
        ,('txt1', 'to')
        ,('txt2', 'have' )
        ,('txt3','a')
        ,('lbl4','friend')
        ,('btn1','like')
        ,('dd1','you')), 400)

    scn.append(Scene(obj, 2000))
    scn[-1].set_move({
        'dd1': (300, 40)
        , 'txt1': (50, 150)
        , 'txt2': (300, 150)
        , 'txt3': (550, 150)
        , 'btn1': (300, 230)
        , 'lbl1': (100, 350)
        , 'lbl2': (400, 350)
        , 'lbl3': (100, 450)
        , 'lbl4': (400, 450)})
    scn.append(Scene(obj, 4000))
    scn[-1].set_change_text(
        (('dd1', '***')
         , ('txt1', 'May')
         , ('txt2', 'all')
         , ('txt3', 'your')
         , ('btn1', 'dreams')
         , ('lbl1', 'come')
         , ('lbl2', 'true')
         , ('lbl3', '***')
         , ('lbl4', '***')), 400)

    scn.append(Scene(obj, 2000))
    scn[-1].set_move({
        'lbl1': (50, 50)
        , 'txt1': (400, 50)
        , 'lbl2': (50, 150)
        , 'dd1': (400, 140)
        , 'lbl3': (50, 250)
        , 'txt2': (400, 250)
        , 'lbl4': (50, 350)
        , 'txt3': (400, 350)
        , 'btn1': (300, 450)})
    scn.append(Scene(obj, 4000))
    scn[-1].set_change_text(
        (('lbl1', 'Name')
         , ('txt1', 'John Smith')
         , ('lbl2', 'Gender')
         , ('dd1', 'Male')
         , ('lbl3', 'Age')
         , ('txt2', '57')
         , ('lbl4', 'City')
         , ('txt3', 'Chennai')
         , ('btn1', 'Submit')), 400)

    scn[0].init()


def animate():
    global scn_id
    s = scn[scn_id]
    s.next_step()
    if not s.is_finished:
        app.top.after(s.delay_ms, animate)
    elif scn_id < len(scn) - 1:
        dly = s.pafter
        scn_id += 1
        s = scn[scn_id]
        s.init()
        app.top.after(dly, animate)


app = MyApp('Happy Friendship Day !!', width=900, height=650)
load_window()
load_scenes()
app.top.after(3000, animate)
app.show()

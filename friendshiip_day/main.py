from tkinter import *
from fdhelper import MyApp, Scene

obj = {}
scn = []
scn_id = 0

def load_window():
	fr = app.add_frame('Enter Details',width=880,height=630,xy=[10,10])
	obj['lbl1'] = fr.add_label('Name',width=12,height=1,xy=[50,50])
	obj['txt1'] = fr.add_text('John Smith',width=10,height=1,xy=[400,50])
	obj['lbl2'] = fr.add_label('Gender',width=12,height=1,xy=[50,150])
	obj['dd1'] = fr.add_dropdown(['Male','Female'],'Male',xy=[400,130])
	obj['lbl3'] = fr.add_label('Age',width=12,height=1,xy=[50,250])
	obj['txt2'] = fr.add_text('57',width=10,height=1,xy=[400,250])
	obj['lbl4'] = fr.add_label('City',width=12,height=1,xy=[50,350])
	obj['txt3'] = fr.add_text('Chennai',width=10,height=1,xy=[400,350])
	obj['btn1'] = fr.add_button('submit',cb=None,xy=[300,450])
	obj['lblovr'] = fr.add_label('To all the text boxes',width=32,height=3,xy=[10,150])
	obj['lblovr'].hide()
	

def load_scenes():
	scn.append( Scene(obj) )
	scn[0].init()
	scn[0].init_move({
	'lbl4': (100,50)
	,'dd1': (450,30)
	,'lbl1': (50,150)
	,'lbl2': (300,150)
	,'lbl3': (550,150)
	,'txt1': (50,250)
	,'txt2': (300,250)
	,'txt3': (550,250)
	,'btn1': (300,350)})
	

def animate():
	global scn_id
	s = scn[scn_id]
	s.next_step()
	if not s.is_finished:
		app.top.after(s.delay_ms,animate)
	elif scn_id < len(scn) - 1:
		scn_id += 1		
		s = scn[scn_id]
		s.init()
		app.top.after(s.delay_ms,animate)
				
app = MyApp('Happy Friendship Day !!',width=900,height=650)
load_window()
load_scenes()
animate()
app.show()

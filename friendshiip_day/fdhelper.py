from tkinter import *
from typing import List


def dummy(*args, **kwargs):
	pass


def pos(elm, xy: List[int]):
	elm.place(x=xy[0], y=xy[1])


class MyWidget:
	def __init__(self,elm,xy: List[int]):
		self.elm = elm
		self.default_bg = self.elm.cget('background')
		self.x,self.y = xy
		pos(self.elm,xy=xy)

	def move(self,x:int,y:int):
		self.x, self.y = x,y
		pos(self.elm,xy=[x,y])
		
	def bg(self,clr:str):
		self.elm.config(bg=clr)
		
	def reset_bg(self):
		self.elm.config(bg=self.default_bg)
		
	def hide(self):
		self.elm.place_forget()
		
	def show(self):
		pos(self.elm,xy=[self.x,self.y])
		
	

class MyButton(MyWidget):
	def __init__(self, prnt, text: str, cb, xy: List[int]):
		self.prnt = prnt
		self.elm = Button(self.prnt, text=text, command=cb)		
		super().__init__(self.elm,xy)
		
class MyDropdown(MyWidget):
	def __init__(self, prnt, options: List[str], text: str, xy: List[int]):
		self.prnt = prnt
		self.var: StringVar = StringVar()
		self.var.set(text)
		self.elm = OptionMenu(self.prnt, self.var,*options)					
		super().__init__(self.elm,xy)

	def set(self, text):
		self.var.set(text)
			

class MyLabel(MyWidget):
	def __init__(self, prnt, text: str, width: int, height: int, xy: List[int]):
		self.prnt = prnt
		self.var: StringVar = StringVar()
		self.elm = Label(self.prnt, textvariable=self.var)
		self.var.set(text)
		self.elm.config(width=width)
		self.elm.config(height=height)		
		super().__init__(self.elm,xy)

	def set(self, text):
		self.var.set(text)
	

class MyText(MyWidget):
	def __init__(self, prnt, text: str, width: int, height: int, xy: List[int]):
		self.prnt = prnt	   
		self.elm = Text(self.prnt, width=width, height=height)
		self.set(text)		
		super().__init__(self.elm,xy)

	def clear(self):
	   self.elm.delete('1.0',END)
	   
	def set(self, text):
		self.clear()
		self.elm.insert(END,text)

class MyFrame:
	def __init__(self, prnt, title: str, width: int, height: int, xy: List[int]):
		self.elm: LabelFrame = LabelFrame(prnt, text=title)
		self.elm.config(width=width)
		self.elm.config(height=height)
		pos(self.elm, xy)
		self.children = {}

	def add_label(self, text: str, width: int, height: int, xy: List[int]) -> MyLabel:
		self.children[text]: MyLabel = MyLabel(self.elm, text, width, height, xy)
		return self.children[text]
		
	def add_text(self, text: str, width: int, height: int, xy: List[int]) -> MyText:
		self.children[text]: MyText = MyText(self.elm, text, width, height, xy)
		return self.children[text]

	def add_button(self, text: str, cb, xy: List[int]) -> MyButton:
		self.children[text]: MyButton = MyButton(self.elm, text, cb, xy)
		return self.children[text]

	def add_dropdown(self, options: List[str], text: str, xy: List[int]) -> MyDropdown:
		self.children[text]: MyDropdown = MyDropdown(self.elm, options, text, xy)
		return self.children[text]

class MyApp:
	def __init__(self, title: str, width: int, height: int):
		self.top = Tk()
		self.top.title(title)
		self.top.grid_propagate(False)
		self.top.geometry(f'{width}x{height}+10+10')
		self.children = {}
		

	def add_frame(self, title: str, width: int, height: int, xy: List[int]) -> MyFrame:
		self.children['title'] = MyFrame(self.top, title, width, height, xy)
		return self.children['title']

	def show(self):
		self.top.mainloop()

class Scene:
	def __init__(self,obj,pafter=0):
		self.obj = obj				
		self.is_finished = False		
		self.cur_step = 0
		self.pafter = pafter
		
		

	def init(self):		
		self.strt = {k:(v.x,v.y) for k,v in self.obj.items()}
		
	def init_move(self, tgt):
		self.steps = 15
		self.delay_ms = 200
		self.tgt = tgt
		self.delta = {}
		for k,v in tgt.items():
			dx = (tgt[k][0]-self.strt[k][0])*1.0/self.steps
			dy = (tgt[k][1]-self.strt[k][1])*1.0/self.steps
			self.delta[k] = (dx,dy)
		self.action = self.move
		
	def move(self):
		for k in self.tgt.keys():
			obj = self.obj[k]
			dx,dy = self.delta[k]
			obj.move(obj.x+dx,obj.y+dy)
		self.cur_step += 1
		if self.cur_step >= self.steps:
			self.is_finished = True

	def next_step(self):
		self.action()

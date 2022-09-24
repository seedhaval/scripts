import json
from typing import List
import re
from datetime import datetime, timedelta
import random

nw = datetime.now()
hr = int(nw.strftime('%H'))
wkdy = nw.weekday()

class Activity:
	def __init__(self,d):
		self.title = d['title']
		self.days = d['days']
		self.time = d['time']
		self.gapdays = d['gapdays']
		self.last = d['last']
		self.person = re.findall(r'\d+_\d+', self.title)[0]
		self.pattern = self.title.replace(self.person,'***')
		
	def get_dict(self):
		return {
			'title': self.title
			,'days': self.days
			,'time': self.time
			,'gapdays': self.gapdays
			,'last': self.last
		}
		
	def do(self):
		self.last = nw.strftime('%Y-%m-%d %H:%M:%S')
		
	def get_text(self):
		if not 'text message' in self.title:
			return self.title
		with open('sms_collection.txt') as f:
			data = random.choice([x.strip() for x in f.readlines() if x.strip()])
		return f'{self.title} -> {data}'
		
	def is_ready(self):
		flag = True
		dt = datetime.strptime(self.last, '%Y-%m-%d %H:%M:%S')
		mmin,mmax = map(int, self.gapdays.split(':'))
		wmin,wmax = map(int,self.days.split(':'))
		hmin,hmax = map(int,self.time.split(':'))
		if not hmin <= hr <= hmax:
			flag = False			
		if flag and not wmin <= wkdy <= wmax:
			flag = False			
		if flag and nw < dt + timedelta(days=random.randint(mmin,mmax)):
			flag = False				
		return flag


class ActivityList:
		def __init__(self):
			with open('activity.json') as f:
				ar = json.load(f)
			self.actar: List[Activity] = [Activity(x) for x in ar]
			with open('sensor_status.txt') as f:
				self.status = f.read().strip()
			
		def getcnt(self):
			return len([x for x in self.actar if x.title])
			
		def shuffle(self):
			random.shuffle(self.actar)
			
		def pause(self):
			with open('sensor_status.txt','w') as f:
				f.write('paused')
			
		def write(self):
			ar = [x.get_dict() for x in self.actar if x.title]
			with open('activity.json','w') as f:
				f.write(json.dumps(ar,indent=2))

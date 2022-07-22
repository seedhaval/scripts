import json
from datetime import datetime, timedelta
import random

nw = datetime.now()
pset = {}
pset['1'] = '2_795'.split()
pset['2'] = '66_72 27_75 6_0275 4_31 0925_71 0461_1394 4676_94'.split()
pset['3'] = '476_21 9466_31'.split()
pset['4'] = '0925_312 712_312 049_721'.split()
pset['5'] = [*pset['1'],*pset['2'],*pset['4']]
pset['6'] = [*pset['5'],*pset['3']]
pset['7'] = [*pset['1'],*pset['4']]

with open('activity.json') as f:
	data = json.load(f)
	
d = {}
d['days'] = input('Days of week (0 6): ').replace(' ',':')
if not d['days']:
	d['days'] = '0:6'
d['time'] = input('Time : ').replace(' ',':')
d['gapdays'] = input('Gap Days (7 14): ').replace(' ',':')
if not d['gapdays']:
	d['gapdays'] = '7:14'	
d['last'] = (nw - timedelta(days=int(d['gapdays'].split(':')[1]))).strftime('%Y-%m-%d 08:00:00')
print('Last : ',d['last'])
refp = input('Enter person set # : ')
with open('title.txt') as f:
	for title in [x.strip() for x in f.readlines() if x.strip()]:	
		for prsn in pset[refp]:
			curd = {k:v for k,v in d.items()}
			curd['title'] = title.replace('$per',prsn)
			data.append(curd)
	
print(len(data))	
with open('activity.json','w') as f:
	f.write(json.dumps(data,indent=2))

from datetime import datetime, timedelta
import random
from acthelper import Activity, ActivityList

nw = datetime.now()

def read():
	acl = ActivityList()
	print('length when reading ',acl.getcnt())
	return acl
	
def write( acl ):
	print('length when writing ',acl.getcnt())
	acl.write()
	

def remove_duplicates(acl):
	title = set([])
	for act in acl.actar:
		if act.title in title:
			act.title = None
		else:			
			title |= set([act.title])
	return acl

def process(acl):
	out = remove_duplicates(acl)
	return out
	
write(process(read()))
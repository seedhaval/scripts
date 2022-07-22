from acthelper import ActivityList

acl = ActivityList()

if acl.status == 'paused':
	print('None',end='')
	exit()
		
acl.shuffle()
for act in acl.actar:
	if act.is_ready():
		print(act.get_text(),end='')
		act.do()
		acl.write()
		acl.pause()
		exit()
	
print('None',end='')
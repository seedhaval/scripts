from acthelper import ActivityList, Activity
from collections import defaultdict
from collections import Counter

acl = ActivityList()
def search():
	srch = input('enter text to search : ')
	d = defaultdict(list)
	
	for act in acl.actar:
		if srch in act.title:
			d[act.pattern].append(act.person)

	for k,v in d.items():
		print(k,v,'\n')

def get_person_count():
	print(Counter([x.person for x in acl.actar]))
	
#search()
#get_person_count()
for act in acl.actar:
	if 'text message' in act.title:
		print(act.get_text())

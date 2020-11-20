import json

def sort_by_name(item):
	return item[0]

with open("data-hold/domestic-jobcount.json") as f:
	data = json.loads(f.read())

sorted_data = sorted(data, key=sort_by_name)

for d in sorted_data:
	if d[1] < 100:
		print("%s, %s" %(d[0], d[1]))




number = range(1,31)
list = []
for i in number:
	if i %3==0:
		list.append(i)
	else:
		continue
for q in list:
	print(q)

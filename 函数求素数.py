def sushu(b):
	list = []
	for i in range(2,b+1):
		w = False
		for q in range(2,i):
			if i%q ==0:
				w =True
				break
		if w ==False:
			list.append(i)
	return list






ww = sushu(100)
print(ww)

for i in range(2,100):
	fn = 0
	for j in range(2,i):
		if i%j ==0:
			fn =1
			break
	if fn ==0:
		print(i)

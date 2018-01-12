def sushu(x,y):
	for i in range(x,y):
		ow = 0
		for j in range(2,i):
			if i%j ==0:
				ow = 1
				break
		if ow == 0:
			print(i)
sushu(100,200)			

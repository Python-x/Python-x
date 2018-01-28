def sh(num):
	while num >0:
		if num>1:
			return num*sh(num-1)
		else:
			print(num)
			return num
sh(10)

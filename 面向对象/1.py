for l in range(101,201):
	w =True
	for i in range(101,l+1):
		if l%i == 0:
			w = False
			break

	if w == True:
		print(i)

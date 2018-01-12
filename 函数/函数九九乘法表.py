def print_cfkj(x,y):
	for i in range(x,y+1):
		for j in range(x,i+1):
			print("%d×%d=%d"%(j,i,i*j),end="\t")
		print()
print_cfkj(1,10)
	

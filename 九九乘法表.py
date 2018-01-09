count = 1
while count <=9:
	acount = 1
	while acount <=count:
		print("%d×%d=%d"%(acount,count,count*acount),end="\t")
		acount +=1
	print()

	count +=1

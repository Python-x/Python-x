number = int(input("请输入数字\n"))
if number %10 == 0:
	print("没猜错的话,他是10的%d倍"%(number/10))
else:
	print("他不是10的倍数")

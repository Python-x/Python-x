list1 = ["1","2","3","4","5"]
list2 = ["6","7","8","9","10"]
for w in range(1,6):
	t = True
	k = (input("输入用户名"))
	o = k.lower()
	for i in list1:
		if o == i:
			t = False
		else:
			pass
	for q in list2:
		if o == q:
			t = False
		else:
			pass
	if t == True:
		print("%s可用"%o) 
	else:
		print("%s已经存在"%o)

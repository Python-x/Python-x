list1 = ["小红","管理员","小明","小刚","小李"]
for i in list1:
	if i == "管理员":
		print("管理员爸爸你要看一下状态报告吗")
	else:
		print("%s,欢迎再次登录"%i)
for q in list1:
	list1.clear()
	if list1:
		print("%s你好,欢迎登录"%q)
	else:
		print("抱歉,没有找到任何用户")

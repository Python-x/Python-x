favorite_fruits = ["香蕉","苹果","橙子"]
for i in range(1,6):
	fruit = input("输入水果\n")
	if fruit in favorite_fruits:
		print("我喜欢%s\n"%fruit)
	else:
		print("不,我并不喜欢%s\n"%fruit)

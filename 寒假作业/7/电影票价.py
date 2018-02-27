money = ""
while True:
	i = input("1买票  2退出")
	if int(i) == 1:
		money = input("请输入你的年龄")
		if int(money) < 3:
			print("小朋友,免费哦")
		elif 3 <= int(money) <= 12:
			print("你好,10美元")
		elif int(money) >12:
			print("你好,15美元")		
	elif int(i) == 2:
		break


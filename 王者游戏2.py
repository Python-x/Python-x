ID = "panzhiwei"
PWD = 123456
count =0
i = 0
while count <3 and i==0:
	Id = input("请输入账号")
	pwd = int(input("请输入密码"))
	if ID == Id and PWD == pwd:
		print("登录成功")
		fanwei = int(input("选择英雄范围\n0代表ADC\n1代表肉\n3代表法师\n"))
		if fanwei == 0:
			print("鲁班大师，智商二百五")
		elif fanwei == 1:
			print("程咬金，一个字，干")
		elif fanwei == 3:
			print("王昭君")
		else:
			print("这都不会，你还能干啥")
		break
	if Id != ID or pwd != PWD :
		print("请输入账号")
		print("请输入密码")
		count+=1
print("游戏愉快")

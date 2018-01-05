Id = "panzhiwei"
passwd = 123456
ist = True
cishu = 0
while ist:
	ID = input("请输入您的账号")
	pwd = int(input("请输入您的密码"))


	if ID == Id and passwd ==pwd:
		print("登录成功")
		fanwei = int(input("请选择英雄范围\n0代表ADC\n1代表肉\n3代表法师"))
		if fanwei == 0:
			print("鲁班大师，智商二百五")
		elif fanwei == 1:
			print("程咬金，一个字，干")
		elif fanwei == 3:
			print("王昭君")
		else:
			print("这仨都不会，你要上天呐")
		ist = False
	else:
		print("登录失败")	
		cishu += 1
		if cishu ==3:
			ist = False
			print("次数过多")

account = 24680
passwd = "panzhiwei"
money = 1000
Account = int(input("请输入账号"))
Passwd = input("请输入密码")

if Account == account and Passwd == passwd:
	print("正在查询,请稍后")

	mode = int(input("请选择方式:1取  2存"))
	if mode == 1:

		qukuan = int(input("请输入要取的金额"))

		if qukuan > money:
				print("余额不足，没钱取个毛线")
		if qukuan < money:
				print("这次操作您取款%d元，账户余额为%d元"%(qukuan,money-qukuan))
	if mode == 2:

		cunqian = int(input("请存入要存的金额"))
		if cunqian >= 0:
			print("请稍后...\n这次操作您存入%d,账户余额为%d"%(cunqian,money+cunqian))
else:
	print("账号或密码错误！")


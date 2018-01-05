print('中国建设银行欢迎您')
account = input("请输入账户")
password = input("请输入您的密码")
nick_name = input("请输入您的姓名")
money = 8010000
need_money = input("请输入您要提取的金额")
sum = money - int(need_money)
print("账号%s\n密码******\n姓名%s\n您原有的存款为%d\n您这次要提取的金额为%s\n交易完成，您的账户余额为%d"%(account,nick_name,money,need_money,sum))

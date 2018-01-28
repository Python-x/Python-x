def panduan(account):
	if len(account) < 11:
		print("手机号不合法")
		return 0
	else:
		return 1
def zhuce(account,pwd):
	if panduan(account):
		print("注册成功")
		login(account)
def login(account):
	if panduan(accout):
		print("登录成功")
def Userinif(account):
	if panduan(account,pwd):
		print("你好，赵日天")

zhuce(18635620259,123456)

def panduan(account,pwd):
	if len(account) < 11:
		print("手机号不合法")
		return 0
	else:
		return 1
def zhuce(account,pwd):
	if panduan(account,pwd):
		print("注册成功")
		login(account,pwd)
def login(account,pwd):
	if panduan(accout,pwd):
		print("登录成功")
def Userinif(account,pwd):
	if panduan(account,pwd):
		print("你好，赵日天")

zhuce(18635620259,123456)

import time
list = []
account = ""
pwd =""
list2 = []
inif ={}
#注册账号
def zhuce():
	welcome = "欢迎来到相亲网!"
	print(welcome.center(30,"*"))
	global account,pwd
	account = input("在这里填入您的账号")
	pwd = input("在这里填入您的密码")
	age = int(input("请输入您的年龄"))	
	tel = input("请输入您的电话号码")
	print("已向你发送验证码")
	time.sleep(1)
	if age <18:
		print("对不起,您尚未成年")
	else:
		if len(tel) == 11:
			inif = {"账号":account,"密码":pwd}	
			list2.append(inif)	
			print("尊敬的用户，稍后我们会电话和您沟通，为您安排推荐^-^")
			time.sleep(3)
		else:
			print("请确认您输入的电话号码是否合法,谢谢")
			

#写入自身信息
def login():
	for i in list2:
		while True:
			account1 = input("输入您的账号")		
			pwd1 = input("输入您的密码")	
			mm = False
			if account1 == i["账号"] and pwd1 == i["密码"]:
			
				inif = {}
				print("尊敬的用户,请在这里填入您的具体个人信息")
				name = input("姓名:")
				age = int(input("年龄:"))
				sex = input("性别:")
				area = input("所在地区:")
				xueli = input("学历:")
				job = input("职业")
				money = input("收入水平:")
				marital = input("婚姻状况:")
				height = float(input("身高(cm):"))
				weight = float(input("体重(kg):"))
				wechat = input("微信:")
				inif = {"姓名":name,"年龄":age,"性别":sex,"所在地区":area,"学历":xueli,"职业":job,"收入水平":money,"婚姻状况":marital,"身高":height,"体重":weight,"微信":wechat}
				print("正在写入....")
				time.sleep(2)
				list.append(inif)
				
				print(list)
				mm = True
				break
			if mm ==False:
				print("账号或密码错误")
#修改信息
def xiugai():
	for i in list:
		
		amend = int(input("请输入你要修改的信息\n1、姓名  2、年龄  3、性别  4、所在地区  5、学历  6、职业  7、收入水平  8、婚姻状况  9、身高  10、体重  11、微信"))
		owd = input("请输入修改后的信息")
		if owd == i["姓名"]:
			print("已经有这个用户了")
			break
		else:
			if amend ==1:
				i["姓名"]=owd
			elif amend ==2:
				i["年龄"]=owd
			elif amend ==3:
				i["性别"]=owd
			elif amend ==4:
				i["所在地区"]=owd
			elif amend ==5:
				i["学历"]=owd
			elif amend ==6:
				i["职业"]=owd
			elif amend ==7:
				i["收入水平"]=owd
			elif amend ==8:
				i["婚姻状况"]=owd
			elif amend ==9:
				i["身高"]=owd
			elif amend ==10:
				i["体重"]=owd
			elif amend ==11:
				i["微信"]=owd
			else:
				print("不要搞事")
			break
	print(list)
#相亲查询
def xiangqin():
	print(list)
	cha = input("请输入你的名字")		
	for i in list:
		if cha ==i["姓名"]:
			if i["性别"]=="男":
				print("稍等，正在寻找最近的妹子")
				time.sleep(3)
				print("由于你太丑，没有人能看上你")	
			elif i["性别"]=="女":
				print("正在查找离你最近的帅哥")
				time.sleep(3)
				print("抱歉，附近没有瞎子能看上你")
		else:
			print("没这个人")
#删除信息
def shanchu():
	delete = input("请输入您的姓名")
	for i in list:
		w = False
		if delete == i["姓名"]:
			list.remove(i)
			time.sleep(2)
			print("删除成功，祝你幸福")
			w = True
			break
		if w == False:
			print("输入有误")
#查询
def chaxun():
	print(list)
	inquire = input("请输入你要查询的单身狗姓名")
	time.sleep(2)
	for i in list:
		if inquire == i["姓名"]:
			print(i)
		else:
			print("查无此人")
def pankong():
	cha = input("  输入姓名")
	for i in list:
		if cha == i["姓名"]:
			return 1
		else:
			return 0
			

while True:
	open1 = int(input("  请输入您要进行的操作\n  1、注册\n  2、登录\n  3、我有对象了我要删除相亲信息\n  4、查询相亲信息\n  5、修改信息\n  6、开始寻找我的另一半\n  7、退出系统\n  "))
	if open1 ==1:
		zhuce()
	elif open1 ==2:
		login()
	elif open1 ==3:
		if pankong():
			shanchu()		
		else:
			print("\n  没有这个用户\n")
	elif open1 ==4:
		if pankong():
			chaxun()
		else:
			print("\n  没有这个人\n")
	elif open1 ==5:
		if pankong():
			xiugai()
		else:
			print("\n  没有这个用户\n")
	elif open1 ==6:
			xiangqin()
	elif open1 ==7:
		break
	else:
		print("\n  别开玩笑了\n")

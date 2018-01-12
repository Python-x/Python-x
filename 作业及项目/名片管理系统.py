str1 = "名片管理系统"
print(str1.center(20,"*"))
list = []
#删除函数:
def shanchu():
	delete = input("请输入你要删除的名片的姓名")
	for i in list:
		w = False
		if i["name"]==delete:
			list.remove(i) 
			print(list)		
			w = True
			break
		if w == False:
			print("你输入的姓名不存在")
#添加函数:
def tianjia():
	inif = {}
	name1 = input("请输入姓名")
	age1 = int(input("请输入年龄"))
	sex1 = input("请输入性别")
	minzu1 = input("请输入民族")
	Tel = int(input("请输入电话号码"))
	height1 = float(input("请输入身高"))
	weight1 = float(input("请输入体重"))
	if not list:
		inif = {"name":name1,"age":age1,"sex":sex1,"民族":minzu1,"电话":Tel,"身高":height1,"体重":weight1}
		list.append(inif)
		print(list)
	else:
		ow = False
		for i in list:
			for k,v in i.items():
				if v == name1:
					print("输入的名片已存在")
					ow = True
					break
		if not ow:
			inif = {"name":name1,"age":age1,"sex":sex1,"民族":minzu1,"电话":Tel,"身高":height1,"体重":weight1}
			list.append(inif)
			print(list)
#修改函数
def xiugai():
	amendname = input("请输入要修改的名片姓名")
	for i in list:
		if amendname == i["name"]:
			amend = int(input("请输入你要修改的信息\n1、姓名 2.年龄 3.性别 4、民族 5、电话 6、身高 7、体重\n"))
			owd = input("请输入改后的信息")
			if amend ==1:
				i["name"]=owd
			elif amend ==2:
				i["age"]=owd
			elif amend ==3:
				i["sex"]=owd
			elif amend ==4:
				i["民族"]=owd
			elif amend ==5:
				i["电话"]=owd
			elif amend ==6:
				i["身高"]=owd 
			elif amend ==7:
				i["体重"]=owd
			else:
				print("别闹")
		else:
			print("没这人啊")
	print(list)			
def chaxun():
	inquire = input("请输入你要查询的名片姓名")
	for i in list:
		if inquire ==i["name"]:
			print(i)
while True:
	oprtion = int(input("1、添加名片 2、删除名片 3、修改名片 4、查询名片 5、退出系统"))
	if oprtion ==1:
		tianjia()
	if oprtion ==2:
		shanchu()
	if oprtion ==3:
		xiugai()
	if oprtion ==4:
		chaxun()
	if oprtion ==5:
		break
	else:
		print("你确定没在逗我?")

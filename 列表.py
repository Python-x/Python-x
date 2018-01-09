tip = "个人信息管理系统"
print(tip.center(30,'*'))
list = []
while True:
		mode = int(input("请选择功能 1:新增 2:查看 3:修改 4:删除 5:退出"))
		if mode == 1:
			name = input("请输入名字")
			age = input("请输入年龄")
			sex = input("请输入性别")
			job = input("请输入工作")
			list.append(name)
			list.append(age)
			list.append(sex)
			list.append(job)
			print(list)
		elif mode == 2:
			position = int(input("请输入索引"))
			print(list[position])
		elif mode == 3:
			oldname = input("请输入名字")
			newname = input("请输入新的名字")
			list[0] = newname
			print(list)
		elif mode == 4:
			delname = input("请输入你要删除的名字:")
			list.remove(delname)
			print(list)
		elif mode == 5:
			break








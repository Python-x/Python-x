list = []
def shuru():
	while True:
		inif = {}
		name = input("请输入姓名")
		age = input("请输入年龄")
		if not list:
			inif["name"]= name
			inif["age"]= age
			list.append(inif)
		else:
			ow =False
			for i in list:
				for k,v in i.items():
					if v == name:
						print("输入有误")
						ow = True
						break
			if not ow:
				inif["name"]=name
				inif["age"]=age
				list.append(inif)
		for i in list:
			print(i)


shuru()

		
	

def print_shuru():
	list1 = []
	while True:
		info = {}
		name1 = input("请输入名字")
		age1 = int(input("请输入年龄"))
		if not list1:

			info["name"]= name1
			info["age"]= age1
			list1.append(info)
			
		else:
			ow = False
			for i in list1:
				for k,v in i.items():
					if v == name1:	
						print("输入有误")
						ow = True			
					break
			if not ow:
				info["name"]= name1
				info["age"]= age1
				list1.append(info)
		for i in list1:
			print(i)
			
				
print_shuru()

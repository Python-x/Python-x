me = {}
me ["first_name"] = "潘"
me ["last_name"] = "志伟"
me ["name"] = "潘志伟"
me ["age"] = "18"
me ["city"] = "阳城"
xiaohong = {"name":"小红","age":"14"}
xiaogang = {"name":"小刚","age":"22"}
list1 = [me,xiaohong,xiaogang]
for i in list1:
	print("我叫%s,我%d岁了"%(i["name"],int(i["age"])))


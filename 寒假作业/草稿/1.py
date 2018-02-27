def name(first_name,last_name,middle_name = ""):
	if middle_name:
		name1 = first_name+middle_name+last_name
	else:
		name1 = first_name+last_name
	return name1.title()
t = name(first_name = "潘 ",last_name = "伟 ")
o = name("pan ","wei ","zhi ")
print(o)
print(t)

list1 = ["海鲜至尊披萨","香荤至尊披萨","荤素满堂披萨"]
for i in list1:
	print(i+"非常的好吃")
print("4008123123")
list2 = list1[:]
list1.append("我的披萨")
list2.append("他的披萨")
print("我最喜欢的披萨有:")
for q in list1:
	print(q)
print("他最喜欢的披萨:")
for s in list2:
	print(s)

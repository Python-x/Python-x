menu = ["1号","2号","3号","4号","5号","6号"]
order_form = []
for i in menu:
	print("我们店里有%s三明治"%i)	
	order_form.append(i)
print(order_form)
print("3号卖完了")
while "3号" in menu:
	menu.remove("3号")
print(menu)

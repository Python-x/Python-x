age = int(input("输入你的年龄"))
if age < 2:
	print("还是个婴儿")
elif 2 <= age < 4:
	print("你正在蹒跚学步")
elif 4 <= age < 13:
	print("你是儿童")
elif 13 <= age < 20:
	print("你是青少年")
elif 20 <= age < 65:
	print("你是成年人")
elif age >= 65:
	print("恭喜你步入老年")
else:
	print("你怕不是个妖怪")

high = float(input("请输入身高"))
money = int(input("请输入身价"))
yanzhi = int(input("请输入颜值分"))

if high > 180 and money > 1000000 and yanzhi > 90:
	print("标准的高富帅")
elif high < 180 and money > 1000000 and yanzhi > 90:
	print("可能你的人生有些瑕疵")
elif high < 180 and money < 1000000 and yanzhi > 90:
	print("这辈子你也就只能靠脸吃饭了")
elif high < 160 and money < 100 and yanzhi < 60:
	print("抬走，抬走!")

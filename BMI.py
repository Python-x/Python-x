hight = float(input("请输入身高 (m)"))
weight = float(input("请输入体重(kg)"))
BMI = weight/hight**2
if BMI < 18.5:
	print("过轻")
if BMI > 18.5 and BMI < 25:
	print("正常")
if BMI > 25 and BMI < 28:
	print("过重")
if BMI > 28 and BMI < 32:
	print("肥胖")
if BMI > 32:
	print("严重肥胖")


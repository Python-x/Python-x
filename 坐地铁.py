km = float(input("请输入距离"))
sum = 0
money = 0
for i in range(1,61):
	if km <=6:
		money =3
	elif km >6 and km <=12:
		money = 4
	elif km >12 and km <=22:
		money = 5
	elif km >22 and km <=32:
		money = 6
	elif km >32:
		if (km-32)%20 ==0:
			money = 6+(km-32)/20
		else:
			money = 6 + int((km-32)/20)+1
	if sum >=100 and sum <150:
		money = money*0.8
	elif sum >=150 and sum <400:
		money = money*0.5
	sum += money
print("你一个月花了%.2f"%sum)


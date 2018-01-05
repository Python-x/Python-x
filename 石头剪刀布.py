import random
player1 = random.randint(1,3)
I = int(input("请输入\n1、石头\n2、剪刀\n3、布\n"))

if (I == 1 and player1 == 2) or (I == 2 and player1 == 3) or (I == 3 and player1 == 1):
	print("不，你作弊")
elif I == player1:
	print("我们再来一次")
else:
	print("哈哈，你输了")


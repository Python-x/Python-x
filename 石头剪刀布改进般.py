import random
player = random.randint(1,3)
while True:
		I = int(input("请输入\n1、石头\n2、剪刀\n3、布\n"))
		if player == 1:
			if I == 2:
				print("啊，石头，早知道出布了")
			elif I == 1:
				print("哈哈我也是石头")
			else:
				print("哈哈，早就猜到你要出石头")
		if player == 2:
			if I == 3:
				print("哎呀，我是布，你肯定作弊")
			elif I == 2:
				print("哎呀，剪刀对剪刀")
			else:
				print("我是石头，我赢了")
		if player == 3:
			if I == 1:
				print("你一定是看到了我藏在背后的石头")
			elif I == 3:
				print("两个布......")
			else:
				print("我是剪刀，哈哈")



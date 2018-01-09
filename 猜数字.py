import random
player = random.randint(1,100)
count = 1
while count <=10:
	
		I = int(input("请输入你猜的数字"))
		if I > player:
			print("猜的太大了，再小点")
			continue
		if I < player:
			print("猜的这么小，再大点")
			continue
		if I == player:
			print("哇，猜到了")
			break
count+=1	

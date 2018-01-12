
def print_oushu():
	sum1 = 0
	for i in range(1,101):
		if i%2 ==0:
			sum1 +=i
	print("偶数和为%d"%sum1)


def print_jishu():
	sum2 = 0
	for j in range(1,101):
		if j%2!=0:
			sum2 +=j
	print("奇数和为%d"%sum2)


def print_he():
	sum = 0
	for p in range(1,101):
		sum +=p	
	print("总和为%d"%sum)




print_oushu()

print_he()




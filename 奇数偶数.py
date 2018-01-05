a = int(input("输入"))
count = 0
sum0 = 0
sum1 = 0
sum2 = 0
while count <= a:
	sum0 = sum0+count

	if count%2 ==0:
		sum1 = sum1+count
	else:
		sum2 = sum2+count
	count +=1
print("总和为%d 奇数和为%d 偶数和为%d"%(sum0,sum2,sum1))

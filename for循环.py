"""
name = "panzhiwei"

for i in name:

	print("身体各个部分分解%s"%i)"""


"""
summ = 0
for i in range(1,101):
	summ =summ +i
print(summ)"""



summ = 0
sum1 = 0
sum2 = 0
for i in range(1,101):
	if i%2 == 0:
		sum1 = sum1 +i
	if i%2 != 0:
		sum2 = sum2 +i

		summ = summ+i
print("总和为:%d,偶数和为:%d,奇数和为:%d"%summ,sum1,sum2)



count = 0

msum = 0 

a = int(input("请输入一个数字"))
while count < a :
	if count%2 ==0:
		msum = msum - count
	else:
		msum = msum + count
	count+=1
print("和是%d"%msum)

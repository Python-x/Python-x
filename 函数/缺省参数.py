def qiuhe(a,b=100,p=0):
	sum1 = 0
	if p ==0:
		print("for")
		for i in range(a,b+1):
			sum1+=i
	else:
		print("while")
		while a <= b:
			sum1 +=a
			a+=1
	return sum1
j = qiuhe(1,100,2)
print(j)

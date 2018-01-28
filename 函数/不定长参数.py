def sum(a,b,c,*ww,**kwkw):
	sum2 = 0
	sum3 = 0
	sum1 = a+b+c

	for i in ww:
		sum2 +=i
	for k,v in kwkw.items():
		sum3 +=v 
	o = sum1+sum2+sum3
	return o
jw = sum(1,2,3,4,5,6,7,8,10,age1 =2,age3= 155,age2 = 200)
print(jw)

def make_car(manufacturer1,model1,*tuple1,**kv):
	print("这辆车的具体信息是:")
	print("制造商"+"="+manufacturer1)
	print("型号"+"="+model1)
	for i in tuple1:
		print(i)
	for k,v in kv.items():
		print(k+":"+v)

#make_car("制作商","型号",1,2,3,color = "yello",价格 = "1000000")

#try:
#	p = int(input("输入整数"))
#except Exception as e:
#	print("报错:%s"%e)	
#else:
#	print("没出错")
#finally:
#	print("代码运行完毕")
#print("输入两个数字相除输入'q'退出")

#try:
#	while True:
#		
#		first_num = input("第一个数字:")
#		if first_num == "q":
#			break		
#		last_num = input("第二个数字")
#		if first_num == "q":
#			break

#		print(int(first_num)/int(last_num))
		
#except ZeroDivisionError:
#	print("除零错误") 

#except Exception as w:
#	print("发现未定义错误:%s"%w)

#else:
#	print("这次没有发现异常,正常运行")
#finally:
#	print("运行完毕finally")
def errow():
	i = input("输入密码")
	if len(i) >= 8:
		return i
	p = Exception("密码少于8位")

	raise p
while True:
	try:
		print_mm = errow()
		print(print_mm)
	except Exception as ow:
		print("报错:%s"%ow)

	else:
		print("格式正确")

	finally:
		print("finally")
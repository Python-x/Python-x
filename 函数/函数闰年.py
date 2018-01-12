def year(x):
	if (x%4 ==0 and x%100!=0) or x%400 ==0:
		print("闰年")
	else:
		print("平年")
year(1900)

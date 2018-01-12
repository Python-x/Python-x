def shuru():
	year = int(input("请输入年份"))
	month = int(input("请输入月份"))
	Day = int(input("请输入日期"))
	panduan(year,month,Day)
def panduan(year,month,Day):
	day = 0
	dayue = [1,3,5,7,8,10,12]
	xiaoyue = [4,6,9,11]
	for i in range(1,month):
		if i in dayue:
			day+=31
		elif i in xiaoyue:
			day+=30
		else:
			if run(year):
				day+=29
			elif not run(year):
				day+=28
	day+=Day
	print("这天是第%s天"%day)

def run(year):
	if (year%4==0 and year%100!=0) or year%400:
		return 1
	else:
		return 0
	
shuru()	

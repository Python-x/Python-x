dic = {"小黄":"C","小绿":"C++","小红":"PHP"}
list = ["小红","小黄","小绿","小蓝","小兰"]
list2 = list
for u in dic:
	if u in list:
		print("%s,感谢你的参与"%u)
		list2.remove(u)
	else:
		pass
for i in list2:
	print("%s,你好,有兴趣参与我们的调查吗"%i)

favorite_number = {"小红":["1","2","3"],"小刚":["4","5","6"],"小李":["7","8","9"]}
for k,v in favorite_number.items():
	print("%s最喜欢的数字有:"%k)
	for i in v:
		print("%s\t"%i)

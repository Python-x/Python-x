list1 =[{"beijin":{"renkou":123123,'mianji':1290},"shanghai":{'renkou':123123,'mianji':12331}}]
for i in list1:
	for j in i:
		c = i[j]
		for p in c:
			print(j,p,c[p])

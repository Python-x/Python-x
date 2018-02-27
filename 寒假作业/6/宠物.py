dog = {"主人":"李富贵","品种":"哈士奇"}
dog2 = {"主人":"狗哥","品种":"萨摩"}
pets = [dog,dog2]
for i in pets:
	print("%s的狗子叫%s"%(i["主人"],i["品种"]))

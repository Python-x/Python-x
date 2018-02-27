init = {}
init ["print"] = "输出"
init ["input"] = "输入"
init ["list"] = "列表"
init ["tuple"] = "元祖"
init ["dictionary"] = "字典"
print(init)
for i in sorted(init):
	print("%s:%s"%(i,init[i]))

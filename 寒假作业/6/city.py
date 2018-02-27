cities = {"北京":{"country":"中国","population":"不知道"},"首尔":{"country":"韩国","population":"不多"},"东京":{"country":"日本","population":"也不多"}}
for k,v in cities.items():
	print("%s所属国家是%s,人口有%s"%(k,v["country"],v["population"]))

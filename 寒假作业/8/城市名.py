def city_country(city,country):
	str1 = '"'+city+","+country+'"'
	return str1.title()
str2 = city_country("shang hai","china")
str3 = city_country("bei jin","china")
str4 = city_country("tokyo","japan")
print(str2)
print(str3)
print(str4)

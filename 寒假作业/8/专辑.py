def make_album(name,album_name,quantity = ""):
	if quantity:
		dic = {"歌手姓名":name,"专辑姓名":album_name,"专辑歌曲数目":quantity}
	else:
		dic = {"歌手姓名":name,"专辑姓名":album_name}
	return dic
#dic1 = make_album("歌手1","专辑1",12)
#print(dic1)
#dic2 = make_album("歌手2","专辑2")
#print(dic2)
#dic3 = make_album("歌手3","专辑3")
#print(dic3)
while True:
	name1 = input("输入歌手的名字:\n")
	if name1 == "q":
		break
	else:
		pass
	album_name1 = input("输入专辑名字:\n")
	if album_name1 == "q":
		break
	else:
		pass
	quantity1 = input("输入专辑歌曲数目(如若不知,请直接回车):\n")
	if quantity1 == "q":
		break
	else:
		pass
	print(make_album(name1,album_name1,quantity1))

class Houseitem(object):
	def __init__(self, name , area1):
		self.name = name
		self.area1 = area1

	

		
	def __str__(self):
		return "%s的占地面积是%.2f㎡"%(self.name,self.area1)
bed = Houseitem("席梦思",4)
cheas = Houseitem("衣柜",2)
table = Houseitem("餐桌",1.5)
print(bed)
print(cheas)
print(table)

class House(object):
	def __init__(self, house_type, area):
		self.house_type = house_type
		self.area = area
		self.free_area = area
		self.item_list = []
	
	def  add_item(self, item):
		print("将要添加%s"%item.name)
		if item.area1 > self.free_area:
			print("抱歉,你家已经没地方放%s了"%item.area1)
		self.item_list.append(item.name)
		self .free_area -= item.area1
	def __str__(self):
		return ("户型:%s 总面积:%.2f㎡ 剩余面积:%.2f㎡ 家具:%s"%(self.house_type,self.area,self.free_area,self.item_list))

my_house = House("两室一厅", 60)
my_house.add_item(bed)
my_house.add_item(cheas)
my_house.add_item(table)
print(my_house)
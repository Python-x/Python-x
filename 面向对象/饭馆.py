str1 = "9-1"
str2 = "9-2"

print(str1.center(20,"-"))
class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.name = restaurant_name
		self.typename = cuisine_type
	def describe_restaurant(self):
		print("欢迎光临%s,本店的特色菜系是%s"%(self.name,self.typename))
	def open_restaurant(self):
		print("餐馆正在经营!!!\n")
restaurant = Restaurant("restaurant","粤菜")
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(str2.center(20,"-"))
restaurant1 = Restaurant("张记铁板烧","铁板炒饭")
restaurant1.describe_restaurant()
restaurant2 = Restaurant("天天快餐","熟食")
restaurant2.describe_restaurant()
restaurant3 = Restaurant("老北京面馆","炸酱面")
restaurant3.describe_restaurant()
print("-"*20)


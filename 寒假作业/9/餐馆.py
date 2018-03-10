class Restaurant(object):

	def __init__(self, name, type):
		self.name = name
		self.type = type
		number_served = 0

	def describe_restaurant(self):
		print("欢迎来到"+self.name+","+"本店的菜系是"+self.type)

	def open_restaurant(self):
		print(self.name+"正在营业")

	def set_number_served(self):
		pass
		
restaurant= Restaurant("2号餐厅", "2号")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant= Restaurant("3号餐厅", "3号")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant= Restaurant("4号餐厅", "4号")
restaurant.describe_restaurant()
restaurant.open_restaurant()


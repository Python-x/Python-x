class Car(object):
	Count = 0
	def __init__(self):
		self.color = "黑色"
	def move(cls):
		print("车在移动")
	def __del__(self):

#print(Car.Count)
Car.Count

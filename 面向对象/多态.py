class Dog(object):
	def __init__(self,name):
		self.name = name

	def game(self):
		print(self.name+"在玩")

class XiaoTian_Dog(Dog):
	def game(self):
		print(self.name+"在天上玩")

class Person(object):
	def __init__(self,name):
		self.name = name
	def game_with_dog(self,dog):		
		print("%s和%s在玩耍"%(self.name,dog.name))
#gou = Dog("狗")
ren = Person("小明")
xiaotian = XiaoTian_Dog("哮天犬")
ren.game_with_dog(xiaotian)
xiaotian.game()

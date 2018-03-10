i =2
class Person(object):
	def __init__(self,name):
		self.name = name



	def eat(self):
		print("%s在吃"%self.name)


p = Person("qwe")
p.eat()

class Man(Person):
	def __init__(self,name):
		self.name = name
	def eat(self):
		if i ==1:
			super().eat()
		else:
			print("%s在吃屎"%self.name)



a = Man("a")
a.eat()


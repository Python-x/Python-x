class Person(object):
	def __new__(cls,*w):
		super().__new__(cls)


	def __init__(self,name):
		self.name = name



a = Person("a")
print(a)
class Aniaml(object):
	def __init__(self):
		self.pin_zhong = "动物"
	def print_name(self):
		print("父类的")

class Dog(Aniaml):
	def pao(self):
		print("狗在跑")
	def cry(self):
		print("狗在哭")
	def print_name(self):
		super().print_name() 
		#print("子类的")
class Cat(Aniaml):
	def miao(self):	
		print("猫在吃")
	def cry(self):
		print("猫在哭")
class Zajiao(Dog,Cat):
	def tui(self,name):
		print("%s有腿"%name)


















		
a = Zajiao()
#a.pin_zhong = "杂交品种"
a.print_name()
#a.miao()
#a.pao()
#a.tui("猫狗兽")
#a.cry()


#haha = Dog()
#haha.pin_zhong = "狗"
#haha.print_name()
#haha.pao()



#a = Aniaml()
#a.__pin_zhong = "哈巴狗"
#a.print_name()


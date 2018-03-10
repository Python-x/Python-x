class Person(object):
	def __init__(self, name):
		self.name = name

	def read(self):
		print(self.name +"正在读书")

	def watch_TV(self):
		print(self.name+"在看电视")

class Woman(Person):

	def maoyi(self):
		print(self.name+"在逛街")
mama = Woman("妈妈")
mama.maoyi()
mama.watch_TV()
class Man(Person):
		
	def football(self):
		print(self.name+"在看球赛")	

baba = Man("爸爸")
baba.football()
baba.read()
class Son(Person):

	instance = None
	init_flag = False
	def __new__(cls,*w,**q):
		if cls.instance is None:
			cls.instance = super().__new__(cls)
		return cls.instance

	def __init__(self,name):
		if not Son.init_flag:
			self.name = name
			print("我叫"+self.name+"我是爸爸妈妈唯一的一个孩子")
			Son.init_flag = True
		
	def go_to_play(self,father,mother):
		print("%s和%s%s出去玩了"%(self.name,father.name,mother.name))


xiaoming = Son("小明")
print(id(xiaoming))
xiaoming.go_to_play(baba,mama)

xiaogang = Son("hahaha")
print(id(xiaogang))
xiaogang.go_to_play(baba, mama)

xiaoli = Son("lllll")
xiaoli.go_to_play(baba, mama)
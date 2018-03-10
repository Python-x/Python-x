class Gun(object):
	def __init__(self, model):
		self.model = model

		self.bullet_count = 0	

	def add_bullet(self,count):
		self.bullet_count += count

	def shoot(self):
		if self.bullet_count < 0:
			print("没子弹了...")
			return
		self.bullet_count -= 1
		print("砰,%s还有%d颗子弹"%(self.model,self.bullet_count))

ak47 = Gun("ak47")


class Soldier(object):
	def __init__(self,name):
		self.name = name
		self.gun = None



	def fire(self):
		if self.gun is None:
			print("%s没有枪"%self.name)
			return
	def get_gun(self):
		ak47.add_bullet(60)
		ak47.shoot()
		print("冲啊,许三多")

		ak47.shoot()

xusanduo = Soldier("许三多")
xusanduo.fire()
xusanduo.get_gun()

class User():

	login_attempts = 0
	def __init__(self, first_name, last_name, age):
		self.xin = first_name
		self.ming = last_name
		self.age = age
		
		self.name = (self.xin+" "+self.ming).title()
	def describe_user(self):

		print("姓名:%s,年龄:%d"%(self.name,self.age))

	def greet_user(self):
		print("你好啊%s"%self.name)

	@classmethod
	def increment_login_attempts(cls):
		cls.login_attempts+=1
		print("现在有%d个用户已登录"%cls.login_attempts)
	@classmethod
	def reset_login_attempts(cls):
		cls.login_attempts = 0
		print("现已强制所有人下线,在线人数%d"%cls.login_attempts)
zhangsan = User("zhang", "san", 19)
zhangsan.describe_user()
zhangsan.greet_user()
User.increment_login_attempts()

lisi = User("li", "si", 100)
lisi.describe_user()
lisi.greet_user()
User.increment_login_attempts()

User.reset_login_attempts()
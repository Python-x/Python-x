str1 = "9-3"
print(str1.center(20,"*"))
class User():
	def __init__(self,first_name,last_name,sex):
		self.first_name = first_name
		self.last_name = last_name
		self.sex = sex
	def describe(self):
		print("性别:%s  姓名:%s"%(self.sex,self.first_name+self.last_name))
	def greet(self):
		if self.sex == "女":
			print("%s女士你好"%(self.first_name+self.last_name))
		elif self.sex == "男":
			print("%s先生你好"%(self.first_name+self.last_name))
name1 = User("贾","淼浩","男")
name1.describe()
name1.greet()

import random
class PanZhiWei_Num(object):
	def __init__(self):
		self.PanZhiWei_sum = 0
		self.PanZhiWei_sum1 = 0
		self.PanZhiWei_list = []
		self.PanZhiWei_dic = {}
		
		self.PanZhiWei_count1 = 1

	def PanZhiWei_cai(self):
		self.PanZhiWei_count = 0
		i = random.randint(0, 100)
		while True:
			
			player = int(input("输入你猜的数字")) 
			if player > i:
				print("猜的数字太大了")
				self.PanZhiWei_count+=1
				continue
			if player <i:
				print("猜的太小了哈哈")
				self.PanZhiWei_count+=1
			if player == i:
				print("哇,猜中了")
				self.PanZhiWei_count1+=1
				self.PanZhiWei_dic = {self.PanZhiWei_count1 - 1:self.PanZhiWei_count}
				self.PanZhiWei_list.append(self.PanZhiWei_dic)
				
				
				o = int(input("请问您还要继续玩吗\n1.继续  2.退出"))
				if o == 1:
					print("又开始喽")
					self.PanZhiWei_count = 0
					continue
				if o == 2:
					
					print("你一共玩了%d次"%(self.PanZhiWei_count1-1))
					for i in self.PanZhiWei_list:
						for k,v in i.items():
							print("你第%d次猜了%d次才猜中"%(k,v))
							self.PanZhiWei_sum1+=v
					print("平均猜中的次数是%d"%(self.PanZhiWei_sum1/(self.PanZhiWei_count1-1)))
					break
if __name__ == "__main__":
	panzhiwei = PanZhiWei_Num()
	panzhiwei.PanZhiWei_cai()
	panzhiwei
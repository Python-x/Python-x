import random
import time
def saoyisao(mima):
	print("正在登录")
	login(mima)
	
	

def login(mima):
	if mima == "panzhiwei":
		print("尊敬的QQ会员您好")
		play()		
	else:
		print("请先购买会员，亲")
def play():
	list = ["医疗箱×1","9毫米#","红点瞄准镜","4倍镜#","绷带×5","2级防弹衣","1级背包","破片手榴弹","能量饮料×1","肾上腺激素×1","8倍镜#","护腚神奇平底锅","98k"]
	my = []
	for o in range(1,len(list)+1):
		o = random.choice(list)
		time.sleep(4)
		my.append(list[o])
		print(my)

saoyisao("panzhiwei")

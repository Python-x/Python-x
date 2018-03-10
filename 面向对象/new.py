class MusicPlay(object):
	count = 0
	ww = None
	def __new__(cls):
		if cls.ww is None:
			cls.ww = super().__new__(cls)
		return cls.ww
	def __init__(self):
		MusicPlay.count+=1
		self.name = "123"
a = MusicPlay()
a1 = MusicPlay()
a2 = MusicPlay()
a3 = MusicPlay()
a.name = "贾淼浩"
print(a1.name)
print(a2.name)
print(a3.name)
print(a==a1)

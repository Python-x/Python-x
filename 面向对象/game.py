class Game(object):
	#游戏最高分
	top_score = 99

#显示帮助信息
	@classmethod
	def show_help(cls):
		print("你好")

	@classmethod
	def show_top_score(cls):
		print("最高分是%d"%cls.top_score)
	def __init__(self,name):
		self_player_name = name
	def start_game(self):
		print("开始游戏")
zhangsan = Game("张三")
zhangsan.show_help()
zhangsan.start_game()
Game.show_top_score()
Game.show_top_score()

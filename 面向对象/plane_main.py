import pygame
from plane_sprites import *
class Game(object):
	@staticmethod
	def __game_over():
		print("游戏结束!")
		pygame.quit()
		exit()

	def __init__(self):
		print("初始化")
		#创建游戏的窗口
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)
		#创建时钟
		self.clock = pygame.time.Clock()
		#调用私有方法
		self.__create_sprites()
		#创建精灵
	def __create_sprites(self):
		#背景组
		self.back_group = pygame.sprite.Group()
		#英雄组
		self.hero_group = pygame.sprite.Group()
		#敌机组
		self.enemp_group = pygame.sprite.Group()
	def play_game(self):
		print("开始游戏!")
		while True:
			#设置游戏刷新频率
			self.clock.tick(60)
			#事件监听
			self.__event_handler()
			#碰撞监测
			self.__check_collide()
			#更新精灵组
			self.__update_sprites()
			#更新屏幕刷新
			pygame.display.update()
	#事件监听		
	def __event_handler(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.__game_over()
	#碰撞监测
	def __check_collide(self):
		pass
	#更新精灵组
	def __update_sprites(self):
		for self.group in [self.back_group,self.enemp_group,self.hero_group]:
			self.group.update()
			self.group.draw(self.screen)

		pygame.display.update()


if __name__ == '__main__':
	game = Game()
	game.play_game()
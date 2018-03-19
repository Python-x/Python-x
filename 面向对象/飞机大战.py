import pygame
from sprites import *

class Plane_game(object):
	print("游戏初始化")

	#创建游戏窗口 pygame.display.set_mode 创建游戏窗口 需要传宽和高 会给我们返回一个窗口
	#。size 取宽高  .x取x轴的值  .y取y轴的值
	self.screen = pygame.display.set_mode()
	#创建游戏时钟 pygame.time.Clock()会给我们返回一个时钟对象
	self.clock = pygame.time.Clock()
	#调用私有方法 里面的创建精灵和精灵组
	self.__create_sprites()
	

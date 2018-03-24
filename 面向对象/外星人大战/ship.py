import pygame

class Ship(object):

	def __init__(self, screen):
		self.screen = screen
		#加载飞机图像并获取其外接矩形
		self.image = pygame.image.load("./image/me1.png")
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#将每艘飞船放在屏幕底部中央
		
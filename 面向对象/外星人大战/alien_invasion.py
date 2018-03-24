import pygame
import sys
from settings import *
def run_game():
	#初始化
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.width, ai_settings.height))
	pygame.display.set_mode("外星人大战")
	
	#开始游戏循环
	while True:
		#监视键盘鼠标的事件
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		screen.fill(ai_settings.bg_color)
		#让最近绘制的屏幕可见
		pygame.display.flip()


run_game
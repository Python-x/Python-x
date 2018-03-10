import pygame
# 初始化方法
pygame.init()

# 创建游戏屏幕
screen = pygame.display.set_mode((480, 700))
# 加载背景图片
bg = pygame.image.load('./images/background.png')
# 确定英雄的初始位置 返回回来的是一个坐标系(217,500,47,53)
hero_rect = pygame.Rect(189, 500, 102, 126)
# 绘制到屏幕
# screen.blit(bg, (0, 0))


# 创建英雄
hero = pygame.image.load("./images/me2.png")
# 绘制到屏幕上
screen.blit(hero, hero_rect)
# 刷新屏幕
pygame.display.update()


# 时钟对象

clock = pygame.time.Clock()

#

while True:

	hero_rect.y -= 1
	hero_rect = pygame.Rect(189, 500, 102, 126)
	screen.blit(bg, (0, 0))
	screen.blit(hero, hero_rect)
	pygame.display.update()
	clock.tick(60)
	if (hero_rect.y + hero_rect.height) <= 0:
		hero_rect.y = 700
	for event in pygame.event.get():
		print(event)
		if event.type == pygame.KEYDOWN:
			if event.key == 276:
				hero_rect.x -= 10
				print("←")
			elif event.key == 273:
				print("↑")
				hero_rect.y += 10
			elif event.key == 275:
				print("→")
				hero_rect.x += 10
			elif event.key == 274:
				print("↓")
				hero_rect.y += 10
		if event.type == pygame.QUIT:
			print("退出")
			pygame.quit()
			exit()

















# 退出  卸载
pygame.quit()

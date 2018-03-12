import pygame
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
class PlaneGame(pygame.sprite.Sprite):
	
	def __init__(self,new_image,new_speed = 1):
		super().__init__()
		#图片  速度  位置
		self.image = pygame.image.load(new_image)
		self.speed = new_speed
		#获取图片的宽和高
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.y += 1

class Background(PlaneGame):
	def __init__(self, new_image):
		super().__init__(new_image)
		
	def update(self):
		super().update()
		if self.rect.y == SCREEN_RECT.height:
			self.rect.y = 0

		
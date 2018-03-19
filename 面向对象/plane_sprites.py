import pygame
import random
# 游戏屏幕的大小
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 敌机的定时器事件常量
CREATE_ENEMY_EVENT = pygame.USEREVENT

# 定义一个子弹的常量
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class PlaneGame(pygame.sprite.Sprite):
    """游戏精灵的基类"""

    def __init__(self, new_image, new_speed=1):
        # 调用父类的初始化方法
        super().__init__()
        # 图片  速度  位置
        self.image = pygame.image.load(new_image)
        self.speed = new_speed
        # 获取图片的宽和高
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += self.speed


class Background(PlaneGame):
    def __init__(self, is_alt=False):
        super().__init__("./images/background.png")
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()
        if self.rect.y == SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(PlaneGame):
    """敌机精灵类"""

    def __init__(self):
        # 调用父类的方法,创建敌机精灵,并且指定地基的图像
        super().__init__("./images/enemy1.png")

        # 设置敌机的随机初始速度

        self.speed = random.randint(3, 5)

        # 设置敌机的随机初始位置

        self.rect.bottom = 0

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        panduan = random.randint(0, 2)
        if panduan == 0:
            # 调用父类的方法 让敌机在垂直方向运动
            super().update()
        elif panduan == 1:
            self.rect.y += self.speed
            self.rect.x -= self.speed
        elif panduan == 2:
            self.rect.y += self.speed
            self.rect.x += self.speed

        # 判断是否飞出屏幕 如果是 需要将敌机从精灵组删除
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        print("敌机挂掉了%s" % self.rect)


class Hero(PlaneGame):
    """英雄的精灵"""

    def __init__(self):

        super().__init__("./images/me1.png", 0)

        # 给英雄设置一个初始位置
        self.rect.centerx = SCREEN_RECT.centerx - 123
        self.rect.bottom = SCREEN_RECT.height - 120
        self.speed1 = 0
        # 创建一个子弹的精灵
        self.bullets = pygame.sprite.Group()

    def update(self):

        # super().update()
        # 飞机水平移动
        self.rect.x += self.speed
        self.rect.y += self.speed1

        # 判断飞机屏幕边界
        if self.rect.right < 0:
            self.rect.left = SCREEN_RECT.width

        if self.rect.left > SCREEN_RECT.right:
            self.rect.right = 0

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_RECT.height:
            self.rect.bottom = SCREEN_RECT.height

    def fire(self):
        print("发射子弹")

        for i in (1, 2, 3):
            # 创建子弹
            bullet = Bullet()
            bullet1 = Bullet1()
            bullet2 = Bullet1()
            # 设置子弹的位置
            bullet.rect.bottom = self.rect.y + 20
            bullet.rect.centerx = self.rect.centerx
            bullet1.rect.bottom = self.rect.y + 30
            bullet1.rect.centerx = self.rect.centerx + 15
            bullet2.rect.bottom = self.rect.y + 30
            bullet2.rect.centerx = self.rect.centerx - 15

            # 将子弹添加到精灵组
            self.bullets.add(bullet, bullet1, bullet2)


class Hero2(PlaneGame):
    def __init__(self):
        super().__init__("./images/me2.png", 0)
        self.rect.centerx = SCREEN_RECT.centerx + 123
        self.rect.bottom = SCREEN_RECT.height - 120
        self.speed1 = 0
        self.bullets = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.speed1

        # 判断飞机屏幕边界
        if self.rect.right < 0:
            self.rect.left = SCREEN_RECT.width

        if self.rect.left > SCREEN_RECT.right:
            self.rect.right = 0

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_RECT.height:
            self.rect.bottom = SCREEN_RECT.height

    def fire(self):
        print("发射子弹")

        for i in (1, 2, 3):
            # 创建子弹
            bullet = Bullet1()
            bullet1 = Bullet()
            bullet2 = Bullet()
            # 设置子弹的位置
            bullet.rect.bottom = self.rect.y + 20
            bullet.rect.centerx = self.rect.centerx
            bullet1.rect.bottom = self.rect.y + 30
            bullet1.rect.centerx = self.rect.centerx + 15
            bullet2.rect.bottom = self.rect.y + 30
            bullet2.rect.centerx = self.rect.centerx - 15

            # 将子弹添加到精灵组
            self.bullets.add(bullet, bullet1, bullet2)


class Bullet1(PlaneGame):
    """子弹精灵类"""

    def __init__(self):

        # 调用父类的方法
        super().__init__("./images/bullet1.png", -6)

    def update(self):

        super().update()

        # 判断子弹是否超出屏幕 如果是 我们要让子弹从精灵组删除

        if self.rect.bottom < 0:
            self.kill()


class Bullet(PlaneGame):
    """子弹精灵类"""

    def __init__(self):

        # 调用父类的方法
        super().__init__("./images/bullet2.png", -6)

    def update(self):

        super().update()

        # 判断子弹是否超出屏幕 如果是 我们要让子弹从精灵组删除

        if self.rect.bottom < 0:
            self.kill()

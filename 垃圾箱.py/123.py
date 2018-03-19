import pygame
from lala import *

pygame.mixer.init()

pygame.mixer.music.load("阿克江LilAkin - Yours.mp3")

pygame.mixer.music.play()


class Game(object):
    @staticmethod
    def __game_over():
        print("游戏结束!")
        pygame.quit()
        exit()

    def __init__(self):
        print("初始化")
        # 创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法
        self.__create_sprites()
        #设置定时器时间 - 每秒创建一架战机
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 500)
        # 每隔0.5秒发射一个子弹
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

        # 创建精灵
    def __create_sprites(self):
        bg1 = Background()
        bg2 = Background(True)
        bg2.rect.y = -bg2.rect.height

        # 背景组
        self.back_group = pygame.sprite.Group(bg1, bg2)
        # 英雄组
        self.hero = Hero()
        self.hero2 = Hero2()
        self.hero_group = pygame.sprite.Group(self.hero)
        self.hero2_group = pygame.sprite.Group(self.hero2)
        # 敌机组 self.enemp_group = []
        self.enemy_group = pygame.sprite.Group()

    def play_game(self):
        print("开始游戏!")
        while True:
            self.clock.tick(60)
            # 事件监听
            self.__event_handler()
            # 碰撞监测
            self.__check_collide()
            # 更新精灵组
            self.__update_sprites()
            # 更新屏幕刷新
            pygame.display.update()
    # 事件监听

    def __event_handler(self):

        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                self.__game_over()

            elif event.type == CREATE_ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
                self.hero2.fire()

            key_pressed = pygame.key.get_pressed()
            key_pressed1 = pygame.key.get_pressed()
            #if key_pressed[pygame.K_SPACE]:
                #self.hero.fire()
            if key_pressed[pygame.K_RIGHT]:
                print("向右边移动")
                self.hero.speed = 8

            elif key_pressed[pygame.K_LEFT]:
                self.hero.speed = -8
                print("向左边移动")

            elif key_pressed[pygame.K_UP]:
                self.hero.speed1 = -8
                print("向上移动")
            elif key_pressed[pygame.K_DOWN]:
                self.hero.speed1 = 8
                print("向下移动")

            else:
                self.hero.speed = 0
                self.hero.speed1 = 0
            #if key_pressed1[pygame.K_j]:
                #self.hero2.fire()
            if key_pressed1[pygame.K_a]:
                self.hero2.speed = -8

            elif key_pressed1[pygame.K_d]:
                self.hero2.speed = 8

            elif key_pressed1[pygame.K_s]:
                self.hero2.speed1 = 8

            elif key_pressed1[pygame.K_w]:
                self.hero2.speed1 = -8

            else:
                self.hero2.speed = 0
                self.hero2.speed1 = 0
                #self.hero2.speed = 0
                #self.hero2.speed1 = 0
    # 碰撞监测

    def __check_collide(self):
        # 子弹摧毁飞机
        pygame.sprite.groupcollide(
            self.hero.bullets, self.enemy_group, True,True)
        #pygame.sprite.groupcollide(
            #self.hero1.bullets, self.enemy_group, True, True)
        pygame.sprite.groupcollide(
            self.hero2.bullets, self.enemy_group, True, True)
        # 英雄撞到敌机
        enemies = pygame.sprite.spritecollide(
            self.hero, self.enemy_group, False, False)
        enemies1 = pygame.sprite.spritecollide(
            self.hero2, self.enemy_group, False, False)
        print("enemies:%s" % enemies)
        print("enemies1:%s" % enemies1)
        if len(enemies) == 1:
            # 让英雄牺牲
            print("1号战机战亡")
            self.hero.kill()
            self.hero.rect.x = -SCREEN_RECT.width
            
        if len(enemies1) == 1:
            self.hero2.kill()
            self.hero2.rect.x = -SCREEN_RECT.width
            
            print("2号战机战亡")
            # 结束游戏

        if self.hero.rect.x == -SCREEN_RECT.width and self.hero2.rect.x == -SCREEN_RECT.width:
            print("游戏结束")
            Game.__game_over()

    # 更新精灵组

    def __update_sprites(self):
        for group in [self.back_group, self.enemy_group, self.hero.bullets, self.hero_group, self.hero2.bullets, self.hero2_group]:
            group.update()
            group.draw(self.screen)


if __name__ == '__main__':
    game = Game()
    game.play_game()

import pygame
import random
from plane_sprites import *

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
        #设置定时器时间 - 每秒创建一架战
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
            key_pressed2 = pygame.key.get_pressed()
            # if key_pressed[pygame.K_SPACE]:
            # self.hero.fire()
            if key_pressed[pygame.K_RIGHT]:
                print("向右边移动")
                self.hero.speed = 8

            elif key_pressed[pygame.K_LEFT]:
                self.hero.speed = -8
                print("向左边移动")
            else:
                self.hero.speed = 0

            if key_pressed[pygame.K_UP]:
                self.hero.speed1 = -8
                print("向上移动")
            elif key_pressed[pygame.K_DOWN]:
                self.hero.speed1 = 8
                print("向下移动")

            else:
                
                self.hero.speed1 = 0
            # if key_pressed1[pygame.K_j]:
                # self.hero2.fire()
            if key_pressed1[pygame.K_a]:
                self.hero2.speed = -8

            elif key_pressed1[pygame.K_d]:
                self.hero2.speed = 8

            else:
                self.hero2.speed = 0

            if key_pressed1[pygame.K_s]:
                self.hero2.speed1 = 8

            elif key_pressed1[pygame.K_w]:
                self.hero2.speed1 = -8

            else:
                
                self.hero2.speed1 = 0
                #self.hero2.speed = 0
                #self.hero2.speed1 = 0

            # if key_pressed2[pygame.K.KP5]:
            #     self.music1.load_music()

            # if key_pressed2[pygame.K_KP6]:
            #     print("6666666666666666666666666666666666666666666666666666666666666666666666666")
            #     o = random.randint(0, len(music1.name_list)-1)
            #     pygame.mixer.music.queue(music1.name_list[o])

            if key_pressed2[pygame.K_KP1]:
                music1.stop_music()

            if key_pressed2[pygame.K_KP3]:
                music1.pause_music()

            if key_pressed2[pygame.K_KP0]:
                music1.unpause_music()

            if key_pressed2[pygame.K_KP6]:
                music1.next_music()
    # 碰撞监测

    def __check_collide(self):
        # 子弹摧毁飞机
        pygame.sprite.groupcollide(
            self.enemy_group, self.hero.bullets, True, True)
        # pygame.sprite.groupcollide(
        # self.hero1.bullets, self.enemy_group, True, True)
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
class Music(Game):
    def __init__(self):
        self.name_list = ["./images/流派未月亭 - 雅舞.mp3","./images/马阿俊 - 口说无凭事实为证.mp3","./images/英雄联盟 - Ekko.mp3"]
        
        
        self.stop = pygame.mixer.music.stop()
        self.pause = pygame.mixer.music.pause()
        self.unpause = pygame.mixer.music.unpause()
        self.i = random.randint(0, len(self.name_list)-1)
    # def load_music(self):
    #     i = random.randint(0, len(self.name_list))
    #     self.load(i)

    def pause_music(self):
        pygame.mixer.music.pause()

    def unpause_music(self):
        pygame.mixer.music.unpause()

    def stop_music(self):
        pygame.mixer.music.stop()

    def next_music(self):
        pygame.mixer.music.stop()
        
        p = random.randint(0, len(music1.name_list) - 1)
        pygame.mixer.music.load(music1.name_list[p])
        pygame.mixer.music.play()    


pygame.mixer.init()
music1 = Music()
i = random.randint(0, len(music1.name_list)-1)
print("6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666")
pygame.mixer.music.load(music1.name_list[i])
pygame.mixer.music.play()


if __name__ == '__main__':
    game = Game()

    game.play_game()

    o = random.randint(0, len(music1.name_list)-1)
    pygame.mixer.music.queue(music1.name_list[o])

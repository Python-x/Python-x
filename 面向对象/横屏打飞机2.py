import pygame
from lala2 import *



class PanZhiWei_Game(object):


    def __init__(self):
        print("初始化")
        # 创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法
        self.__create_sprites()
        # 设置定时器时间 - 每秒创建一架战机
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 300)
        # 每隔0.5秒发射一个子弹
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)
        self.wanjia1 = 0
        self.wanjia2 = 0
        # 创建精灵

    @staticmethod
    def __game_over():
        print("游戏结束!")
        
        pygame.quit()
        exit()
    def __create_sprites(self):
        bg1 = PanZhiWei_Background()
        bg2 = PanZhiWei_Background(True)
        bg2.rect.right = 0

        # 背景组
        self.back_group = pygame.sprite.Group(bg1, bg2)
        # 英雄组
        self.hero = PanZhiWei_Hero()
        self.hero.rect.centery = SCREEN_RECT.centery+123
        self.hero2 = PanZhiWei_Hero()
        self.hero2.rect.centery = SCREEN_RECT.centery-123
        self.hero_group = pygame.sprite.Group(self.hero)
        self.hero_group1 = pygame.sprite.Group(self.hero2)
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
            self.print_score()
            # 更新屏幕刷新d
            pygame.display.update()
    # 事件监听

    def __event_handler(self):

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                self.__game_over()

            elif event.type == CREATE_ENEMY_EVENT:
                enemy = PanZhiWei_Enemy()
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

            if key_pressed1[pygame.K_RIGHT]:
                print("向右边移动")
                self.hero2.speed = 8

            elif key_pressed1[pygame.K_LEFT]:
                self.hero2.speed = -8
                print("向左边移动")
            else:
                self.hero2.speed = 0
            if key_pressed1[pygame.K_UP]:
                self.hero2.speed1 = -8
                print("向上移动")
            elif key_pressed1[pygame.K_DOWN]:
                self.hero2.speed1 = 8
                print("向下移动")

            else:
                self.hero2.speed1 = 0

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

            if key_pressed2[pygame.K_KP1]:
                music1.stop_music()

            if key_pressed2[pygame.K_SPACE]:
                music1.int1+=1
                music1.pause_music()
            # if key_pressed2[pygame.K_KP3]:
            #     music1.pause_music()

            # if key_pressed2[pygame.K_KP0]:
            #     music1.unpause_music()

            if key_pressed2[pygame.K_BACKSPACE]:
                music1.next_music()
    # 碰撞监测

    def __check_collide(self):

        if pygame.sprite.groupcollide(self.enemy_group, self.hero.bullets, True, True):
            self.wanjia1 += 1
            
        # pygame.sprite.groupcollide(
        # self.hero1.bullets, self.enemy_group, True, True)
        # pygame.sprite.groupcollide(
        #     self.hero2.bullets, self.enemy_group, True, True)
        if pygame.sprite.groupcollide(self.hero2.bullets, self.enemy_group, True, True):
            self.wanjia2 += 1
            
        # 子弹摧毁飞机
        pygame.sprite.groupcollide(
            self.enemy_group, self.hero.bullets, True, True)
        pygame.sprite.groupcollide(
        self.hero2.bullets, self.enemy_group, True, True)

        # 英雄撞到敌机
        enemies = pygame.sprite.spritecollide(
            self.hero, self.enemy_group, False, False)
        enemies1 = pygame.sprite.spritecollide(
            self.hero2, self.enemy_group, False, False)
        
        if len(enemies) == 1:
            # 让英雄牺牲
            print("1号战机战亡")
            self.hero.kill()
            self.hero.rect.y = -SCREEN_RECT.height

        if len(enemies1) == 1:
            self.hero2.kill()
            self.hero2.rect.y = -SCREEN_RECT.height

            print("2号战机战亡")
            # 结束游戏

        if self.hero.rect.y == -SCREEN_RECT.height and self.hero2.rect.y == -SCREEN_RECT.height:
            print("游戏结束")
            print("英雄1的杀敌数:%d"%self.wanjia1)
            print("英雄2的杀敌数:%d"%self.wanjia2)
            Game.__game_over()

    def print_score(self):
        pygame.font.init()
        # 位置
        pos1 = (100, 0)
        pos2 = (240, 0)
        # 颜色
        color = (0, 0, 0)
        text1 = "player1:" + str(self.wanjia1)
        text2 = "player2:" + str(self.wanjia2)
        # 字体?
        cur_font = pygame.font.SysFont("楷体", 30)
        text_fort1 = cur_font.render(text1, 1, color)
        text_font2 = cur_font.render(text2, 1, color)
        self.screen.blit(text_fort1, pos1)
        self.screen.blit(text_font2, pos2)
        # print(self.screen.blit(text_fort1, pos1))
        # print(self.screen.blit(text_font2, pos2))
    # 更新精灵组

    def __update_sprites(self):
        for group in [self.back_group, self.enemy_group, self.hero.bullets, self.hero_group, self.hero_group1, self.hero2.bullets]:
            group.update()
            group.draw(self.screen)


    

class PanZhiWei_Music(PanZhiWei_Game):
    def __init__(self):
        self.name_list = ["./images/流派未月亭 - 雅舞.mp3",
                          "./images/马阿俊 - 口说无凭事实为证.mp3", "./images/英雄联盟 - Ekko.mp3"]
        self.int1 = 2
        self.stop = pygame.mixer.music.stop()
        self.pause = pygame.mixer.music.pause()
        self.unpause = pygame.mixer.music.unpause()
        self.i = random.randint(0, len(self.name_list) - 1)
    # def load_music(self):
    #     i = random.randint(0, len(self.name_list))
    #     self.load(i)

    def pause_music(self):
        if self.int1 % 2 !=0:
            pygame.mixer.music.pause()
        elif self.int1 %2 == 0:
            pygame.mixer.music.unpause()

    def stop_music(self):
        pygame.mixer.music.stop()

    def next_music(self):
        pygame.mixer.music.stop()

        p = random.randint(0, len(music1.name_list) - 1)
        pygame.mixer.music.load(music1.name_list[p])
        pygame.mixer.music.play()


pygame.mixer.init()
music1 = PanZhiWei_Music()
i = random.randint(0, len(music1.name_list) - 1)
pygame.mixer.music.load(music1.name_list[i])
pygame.mixer.music.play()


if __name__ == '__main__':
    game = PanZhiWei_Game()

    game.play_game()

    o = random.randint(0, len(music1.name_list) - 1)
    pygame.mixer.music.queue(music1.name_list[o])
print
import pygame
from pygame.locals import   *
import sys
from itertools import  cycle # 迭代工具
import random

SCREENWIDTH=822  #窗口宽度
SCREENHEIGHT=199 #窗口高度
FPS=30 # 更新画面的时间


class Obstacle(object):
    score=1
    move=5
    obstacle_y=150
    def __init__(self):
        self.rect=pygame.Rect(0,0,0,0)
        self.missile=pygame.image.load('image/missile.PNG').convert_alpha()
        self.pipe=pygame.image.load('image/pipe.PNG').convert_alpha()
        self.numbers=(pygame.image.load('image/0.PNG').convert_alpha(),
                      pygame.image.load('image/1.PNG').convert_alpha(),
                      pygame.image.load('image/2.PNG').convert_alpha(),
                      pygame.image.load('image/3.PNG').convert_alpha(),
                      pygame.image.load('image/4.PNG').convert_alpha(),
                      pygame.image.load('image/5.PNG').convert_alpha(),
                      pygame.image.load('image/6.PNG').convert_alpha(),
                      pygame.image.load('image/7.PNG').convert_alpha(),
                      pygame.image.load('image/8.PNG').convert_alpha(),
                      pygame.image.load('image/9.PNG').convert_alpha()




                      )

        r=random.randint(0,1)
        if r==0:
            self.image=self.missile
            self.move=15
            self.obstacle_y=100
        else:
            self.image=self.pipe

        self.rect.size=self.image.get_size()
        self.width,self.height=self.rect.size

        self.x=800
        self.y=self.obstacle_y
        self.rect.center=(self.x,self.y)

    def obstacle_move(self):
        self.rect.x-=self.move

    def draw_obstacle(self):
        SCREEN.blit(self.image,(self.rect.x,self.rect.y))

    def getScore(self):
        # self.score
        temp=self.score
        if temp==1:
            # self.score_audio.play()
            print('1')
        else:
            self.score=0
        return temp

    def showScore(self,score):
        self.scoreDigits=[int(x) for x in list(str(score))]
        totalwidth=0
        for digit in self.scoreDigits:
            totalwidth+=self.numbers[digit].get_width()
        Xoffset=(SCREENWIDTH-(totalwidth+30))
        for digit in self.scoreDigits:
            SCREEN.blit(self.numbers[digit],(Xoffset,SCREENWIDTH*0.1))
            Xoffset+=self.numbers[digit].get_width()


def game_over():
    screen_w=pygame.display.Info().current_w
    screen_h=pygame.display.Info().current_h
    over_img=pygame.image.load('image/gameover.PNG').convert_alpha()
    SCREEN.blit(over_img,((screen_w-over_img.get_width())/2,(screen_h-over_img.get_height())/2))

def mainGame():
    score=0
    over=False
    global SCREEN,FPSLOCK
    pygame.init()
    #使用python时钟控制每个循环多长时间运行一次，在使用时钟前必须先创建clock对象的一个实例
    FPSLOCK=pygame.time.Clock()
    SCREEN=pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
    pygame.display.set_caption('玛丽冒险')#设置窗体标题
    bg1 = MyMap(0, 0)
    bg2 = MyMap(800, 0)
    marie=Marie()
    addObstacleTimer = 0
    list = []

    while True:
        #获取单击事件
        for event in pygame.event.get():
            #如果单击了关闭窗体就将窗体关闭
            if event.type==QUIT:
                pygame.quit() #退出窗口
                sys.exit()   #关闭窗口

            if event.type==KEYDOWN and event.key==K_SPACE:
                if marie.rect.y>=marie.lowest_y:
                    # marie.jump_audio.play()
                    marie.jump() # 开启玛丽跳的状态
            if over==True:
                mainGame()
        addObstacleTimer+=20
        pygame.display.update() #更新整个窗体
        FPSLOCK.tick(FPS)      #循环多久时间运行一次

        if over == False:
            bg1.map_update()
            bg1.map_rolling()
            bg2.map_update()
            bg2.map_rolling()
            marie.move()
            marie.draw_marie()

            if addObstacleTimer >= 1300:
                r = random.randint(0, 100)
                if r > 40:
                    obstacle = Obstacle()
                    list.append(obstacle)
                addObstacleTimer = 0
            for i in range(len(list)):
                list[i].obstacle_move()
                list[i].draw_obstacle()
                if pygame.sprite.collide_rect(marie,list[i]):
                    over=True
                    game_over()
                else:
                    if (list[i].rect.x+list[i].rect.width)<marie.rect.x:
                        score+=list[i].getScore()
                list[i].showScore(score)



class MyMap(object):

    def __init__(self,x,y):
        '''移动地图类'''
        #加载背景图片
        self.bg=pygame.image.load('image/bg.PNG').convert_alpha()
        self.x=x
        self.y=y
        # print(self.bg,self.x,self.y)


    def map_rolling(self):
        if self.x<-790: #小于-790说明地图已经完全移动完毕
            self.x=800 #给地图一个新的坐标点
        else:
            self.x-=5 #向左移动五个像素

    def map_update(self):
        SCREEN.blit(self.bg,(self.x,self.y))


class Marie():
    def __init__(self):
        #初始化玛丽矩形
        self.rect=pygame.Rect(0,0,0,0)
        self.jumpState=False #跳跃的状态
        self.jumpHeight=130 #跳跃的高度
        self.lowest_y=140  #最低坐标
        self.jumpValue=0 # 跳跃增变量

        self.marieIndex=0
        self.marieIndexGen=cycle([0,1,2])

        # 加载玛丽图片
        self.adventure_img=(
            pygame.image.load('image/ad1.PNG').convert_alpha(),
            pygame.image.load('image/ad2.PNG').convert_alpha(),
            pygame.image.load('image/ad3.PNG').convert_alpha(),
        )
        # self.jump_audio=pygame.mixer.Sound('audio/jump.wav')
        self.rect.size=self.adventure_img[0].get_size()
        self.x=50
        self.y=self.lowest_y
        self.rect.topleft=(self.x,self.y)

    def jump(self):
        self.jumpState=True

    def move(self):
        if self.jumpState:
            if self.rect.y>=self.lowest_y:
                self.jumpValue=-5
            if self.rect.y<=self.lowest_y-self.jumpHeight:
                self.jumpValue=5
            self.rect.y+=self.jumpValue
            if self.rect.y>=self.lowest_y:
                self.jumpState=False

    def draw_marie(self):
        marieIndex=next(self.marieIndexGen)

        SCREEN.blit(self.adventure_img[marieIndex],(self.x,self.rect.y))



if __name__=='__main__':
    mainGame()








































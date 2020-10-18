import pygame

class Menu():
    def __init__(self,screen):
        self.screen=screen
        self.brush=None
        self.colors=[
            (0xff, 0x00, 0xff), (0x80, 0x00, 0x80),
            (0x00, 0x00, 0xff), (0x00, 0x00, 0x80),
            (0x00, 0xff, 0xff), (0x00, 0x80, 0x80),
            (0x00, 0xff, 0x00), (0x00, 0x80, 0x00),
            (0xff, 0xff, 0x00), (0x80, 0x80, 0x00),
            (0xff, 0x00, 0x00), (0x80, 0x00, 0x00),
            (0xc0, 0xc0, 0xc0), (0x00, 0x00, 0x00),
            (0x80, 0x80, 0x80), (0x00, 0xc0, 0x80),
        ]

        self.eraser_color=(0xff,0xff,0xff)
        self.color.rect=[]
        for (i,rgb) in enumerate(self.colors):
            rect=pygame.Rect(10+i%2*32,254+i/2*32,32,32)
            self.colors_rect.append(rect)

        self.pens=[
            pygame.image.load('img/pen.PNG').convert_alpha(),
        ]
        self.erasers=[
            pygame.image.load('img/eraser.PNG').convert_alpha(),
        ]

        self.erasers_rect=[]
        for (i,img) in enumerate(self.erasers):
            rect=pygame.Rect(10,10+(i+1)*64,64,64)
            self.erasers_rect.append(rect)


        self.pens_rect=[]
        for (i,img) in enumerate(self.pens):
            rect=pygame.Rect(10,10+i*64,64,64)
            self.pens_rect.append(rect)

        self.sizes=[
            pygame.image.load('img/plus.PNG').convert_alpha(),
            pygame.image.load('img/minus.PNG').convert_alpha()
        ]


        self.sizes_rect=[]
        for (i,img) in enumerate(self.sizes):
            rect=pygame.Rect(10+i*32,138,32,32)
            self.sizes_rect.append(rect)


    def set_brush(self,bresh):
        self.brush=bresh







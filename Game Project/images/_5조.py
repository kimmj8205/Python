#프로그래밍 기초 팀프로젝트 5조(강유민, 김교원, 김민준, 이서연)

import pygame,time,sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((960,550))
pygame.display.set_caption("슬라임의 '기묘한' 여행 - 프로그래밍 기초 팀프로젝트 5조                                                                                                       ESC : 종료")

clock = pygame.time.Clock()
white = (255,255,255)
dwhite = (230,230,230)
grey = (200,200,200)
dgrey = (150,150,150)
sdgrey = (100,100,100)
stg=0

#이미지
title = pygame.image.load("title.png")
bg0 = pygame.image.load("island.jpg")
bg1_0 =pygame.image.load("seatofo0.png")
bg1 = pygame.image.load("seatofo.png")
bg2 = pygame.image.load("forest1.png")
sky = pygame.image.load("sky.png")
bg3 = pygame.image.load("city.png")
bg3_0 = pygame.image.load("city_0.png")
bg4 = pygame.image.load("city0.png")
bg5 = pygame.image.load("house.png")
bg7 = pygame.image.load("bg7.png")
bg7_0 = pygame.image.load("bg7_1.png")
player = pygame.image.load("player.png")
eat1 = pygame.image.load("eat11.png")
eat2 = pygame.image.load("eat22.png")
smoke1 = pygame.image.load("smoke.png")
smoke0 = pygame.image.load("smoke0.png")
ball = pygame.image.load("ball.png")
ball1 = pygame.image.load("ball1.png")
ball2 = pygame.image.load("ball2.png")
ball3 = pygame.image.load("ball3.png")
plane0 = pygame.image.load("plane0.png")
plane = pygame.image.load("plane.png")
car = pygame.image.load("car.png")
sship = pygame.image.load("sship.png")
sship2 = pygame.image.load("sship2.png")
sship3 = pygame.image.load("ed22.png")
ufo = pygame.image.load("ufo1.png")
end1bg = pygame.image.load("end1.png")
end2bg = pygame.image.load("end2.png")
end3bg = pygame.image.load("end3.png")

ballbutton=pygame.image.load("ballbutton.png")
planebutton=pygame.image.load("planebutton.png")
carbutton=pygame.image.load("carbutton.png")
plusbutton=pygame.image.load("plus.png")
edbutton=pygame.image.load("ed.png")

#좌표
titlerect = title.get_rect()
titlerect.x = 0
bg0rect = bg0.get_rect()
bg0rect.x = 0
bg1rect = bg1.get_rect()
bg1rect.x = 1
bg2rect = bg2.get_rect()
bg2rect.x = 0
bg3rect = bg3.get_rect()
bg3rect.x = 0
bg4rect = bg4.get_rect()
bg4rect.x = 0


stg1prect = player.get_rect()
stg1prect.x = 98
stg1prect.y = 163

stg2prect = player.get_rect()
stg2prect.x = 0
stg2prect.y = 350

stg3prect = player.get_rect()
stg3prect.x = 0
stg3prect.y = 220

sky1prect = player.get_rect()
sky1prect.x = 100
sky1prect.y = 550

stg4prect = player.get_rect()
stg4prect.x = 300
stg4prect.y = 0

stg5prect = player.get_rect()
stg5prect.x = -100
stg5prect.y = 300

stg6prect = player.get_rect()
stg6prect.x = 130
stg6prect.y = 465

stg7prect = player.get_rect()
stg7prect.x = -100
stg7prect.y = 400

end3prect = player.get_rect()
end3prect.x = -100
end3prect.y = 350

ballrect = ball.get_rect()
ballrect.x = 200
ballrect.y =160

plane0rect = plane0.get_rect()
plane0rect.x = 0 
plane0rect.y = 200

carrect = car.get_rect()
carrect.x = 700 
carrect.y = 400

sshiprect = sship.get_rect()
sshiprect.x =  516
sshiprect.y = 54

end2sshiprect = sship.get_rect()
end2sshiprect.x =  750
end2sshiprect.y = 550

uforect = ufo.get_rect()
uforect.x = 200
uforect.y = 550

ballbutton1rect = ballbutton.get_rect()
ballbutton1rect.x = 0
ballbutton1rect.y = 424
ballbutton2rect = ballbutton.get_rect()
ballbutton2rect.x = -240
ballbutton2rect.y = 424
ballbutton3rect = ballbutton.get_rect()
ballbutton3rect.x = -320
ballbutton3rect.y = 424
ballbutton4rect = ballbutton.get_rect()
ballbutton4rect.x = -415
ballbutton4rect.y = 55

planebutton2rect = planebutton.get_rect()
planebutton2rect.x = 480
planebutton2rect.y = 424
planebutton3rect = planebutton.get_rect()
planebutton3rect.x = 240
planebutton3rect.y = 424
planebutton4rect = planebutton.get_rect()
planebutton4rect.x = -175
planebutton4rect.y = 330

carbutton3rect = carbutton.get_rect()
carbutton3rect.x = 640
carbutton3rect.y = 424
carbutton4rect = carbutton.get_rect()
carbutton4rect.x = 730
carbutton4rect.y = 200
carbutton5rect = carbutton.get_rect()
carbutton5rect.x = 730
carbutton5rect.y = 55

plusbutton1rect = plusbutton.get_rect()
plusbutton1rect.x = 320
plusbutton1rect.y = 424
plusbutton2rect = plusbutton.get_rect()
plusbutton2rect.x = 560
plusbutton2rect.y = 424
plusbutton3rect = plusbutton.get_rect()
plusbutton3rect.x = 640
plusbutton3rect.y = 424

edbuttonrect = edbutton.get_rect()
edbuttonrect.x = 735
edbuttonrect.y = 330


#버튼
def button(x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if (click[0] == 1 and action != None):
            if action=='exit':
                exit()
            elif action=='stg1move1':
                stg1move1()
            elif action=='stg1move2':
                stg1move2()
            elif action=='stg2move1':
                stg2move1()
            elif action=='stg2move2':
                stg2move2()
            elif action=='stg2move3':
                stg2move3()
            elif action=='stg2move4':
                stg2move4()
            elif action=='stg2move4':
                stg2move4()
            elif action=='stg3move1':
                stg3move1()
            elif action=='stg3move2':
                stg3move2()
            elif action=='stg3move3':
                stg3move3()
            elif action=='stg3move4':
                stg3move4()
            elif action=='stg4move1':
                stg4move1()
            elif action=='stg4move2':
                stg4move2()
            elif action=='stg4move3':
                stg4move3()
            elif action=='stg4move4':
                stg4move4()
            elif action=='stg4move3_1':
                stg4move3_1()
            elif action=='stg4move4_1':
                stg4move4_1()
            elif action=='stg4move5':
                stg4move5()
            elif action=='stg4move6':
                stg4move6()
            elif action=='stg6move1':
                stg6move1()
            elif action=='stg6move1_1':
                stg6move1_1()
            elif action=='stg6move2':
                stg6move2()
            elif action=='stg6move3':
                stg6move3()
            elif action=='stg6move4':
                stg6move4()
            elif action=='stg6move5':
                stg6move5()
            elif action=='stg6move6':
                stg6move6()
            elif action=='stg6move7':
                stg6move7()
            elif action=='stg6move8':
                end1()
            elif action=='stg7move1':
                stg7move1()
            elif action=='stg7move2':
                stg7move2()
            elif action=='stg7move3':
                stg7move3()
            elif action=='stg7move4':
                stg7move4()
            elif action=='stg7move5':
                stg7move5()
            elif action=='stg7move6':
                stg7move6()
            elif action=='stg7move7':
                stg7move7()
            elif action=='stg7move7_1':
                stg7move7_1()
                  
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))
        
#움직임 함수들
def eat(p,playerrect,bg,bgrect,s,srect):
    for _ in range(5):
        screen.blit(bg, bgrect)
        screen.blit(s, srect)
        screen.blit(eat1,playerrect)
        playerrect.x += 5
        pygame.display.update()
        time.sleep(0.5)
    screen.blit(bg, bgrect)
    screen.blit(eat2,playerrect)
    pygame.display.update()
    time.sleep(1)
def trans(p,playerrect,bg,bgrect,s):
    playerrect.x+=10
    playerrect.y-=20
    for _ in range(2):
        screen.blit(bg, bgrect)
        screen.blit(smoke0, playerrect)
        pygame.display.update()
        time.sleep(0.5)
        screen.blit(bg, bgrect)
        screen.blit(smoke1, playerrect)
        pygame.display.update()
        time.sleep(0.5)
    playerrect.x-=10
    playerrect.y+=20
    screen.blit(bg, bgrect)
    screen.blit(s,playerrect)
    pygame.display.update()
    time.sleep(1)
def up(p,playerrect,bg,bgrect,s=None,srect=None):
    playerrect.y -= 5
    screen.blit(bg, bgrect)
    screen.blit(p,playerrect)
    if (s!=None and srect!=None):
        screen.blit(s, srect)
    pygame.display.update()
    time.sleep(0.05)
def down(p,playerrect,bg,bgrect,s=None,srect=None):
    playerrect.y += 5
    screen.blit(bg, bgrect)
    screen.blit(p,playerrect)
    if (s!=None and srect!=None):
        screen.blit(s, srect)
    pygame.display.update()
    time.sleep(0.05)
def left(p,playerrect,bg,bgrect):
    playerrect.x -= 5
    screen.blit(bg, bgrect)
    screen.blit(p,playerrect)
    pygame.display.update()
    time.sleep(0.05)
def right(p,playerrect,bg,bgrect,s=None,srect=None):
    playerrect.x += 5
    screen.blit(bg, bgrect)
    screen.blit(p,playerrect)
    if (s!=None and srect!=None):
        screen.blit(s, srect)
    pygame.display.update()
    time.sleep(0.05)
def upright(p,playerrect,bg,bgrect,s=None,srect=None):
    playerrect.x += 5
    playerrect.y -=5
    screen.blit(bg, bgrect)
    screen.blit(p,playerrect)
    if (s!=None and srect!=None):
        screen.blit(s, srect)
    pygame.display.update()
    time.sleep(0.05)
def upleft(p,playerrect,bg,bgrect,s=None,srect=None):
    playerrect.x -= 5
    playerrect.y -=5
    screen.blit(bg, bgrect)
    screen.blit(p,playerrect)
    if (s!=None and srect!=None):
        screen.blit(s, srect)
    pygame.display.update()
    time.sleep(0.05)
def downleft(p,playerrect,bg,bgrect,s=None,srect=None):
    playerrect.x -= 5
    playerrect.y += 5
    screen.blit(bg, bgrect)
    screen.blit(p,playerrect)
    if (s!=None and srect!=None):
        screen.blit(s, srect)
    pygame.display.update()
    time.sleep(0.05)
    
def downright(p,playerrect,bg,bgrect,s=None,srect=None):
    playerrect.x += 5
    playerrect.y += 5
    screen.blit(bg, bgrect)
    screen.blit(p,playerrect)
    if (s!=None and srect!=None):
        screen.blit(s, srect)
    pygame.display.update()
    time.sleep(0.05)


def stg1move1():
    eat(player,stg1prect,bg0,bg0rect,ball,ballrect)
def stg1move2():
  trans(player,stg1prect,bg0,bg0rect,ball)
  for _ in range(4):
    right(ball,stg1prect,bg0,bg0rect)
    right(ball,stg1prect,bg0,bg0rect)
    right(ball1,stg1prect,bg0,bg0rect)
    downright(ball1,stg1prect,bg0,bg0rect)
    right(ball2,stg1prect,bg0,bg0rect)
    right(ball2,stg1prect,bg0,bg0rect)
    downright(ball3,stg1prect,bg0,bg0rect)
    right(ball3,stg1prect,bg0,bg0rect)
    right(ball,stg1prect,bg0,bg0rect)
    downright(ball,stg1prect,bg0,bg0rect)
    right(ball1,stg1prect,bg0,bg0rect)
    right(ball1,stg1prect,bg0,bg0rect)
    downright(ball2,stg1prect,bg0,bg0rect)
    right(ball2,stg1prect,bg0,bg0rect)
    downright(ball3,stg1prect,bg0,bg0rect)
    right(ball3,stg1prect,bg0,bg0rect)
  
  downright(ball,stg1prect,bg0,bg0rect)
  right(ball,stg1prect,bg0,bg0rect)
  for _ in range(22):
    downright(ball,stg1prect,bg0,bg0rect)
    right(ball,stg1prect,bg0,bg0rect)
    right(ball,stg1prect,bg0,bg0rect)
    upright(ball,stg1prect,bg0,bg0rect)
    right(ball,stg1prect,bg0,bg0rect)
def stg2move0():
    right(ball,stg2prect,bg1_0,bg1rect)
    right(ball,stg2prect,bg1_0,bg1rect)
    right(ball,stg2prect,bg1_0,bg1rect)
    right(ball,stg2prect,bg1_0,bg1rect)
    right(ball,stg2prect,bg1_0,bg1rect)
    right(ball,stg2prect,bg1_0,bg1rect)
    right(ball,stg2prect,bg1_0,bg1rect)
    right(ball,stg2prect,bg1_0,bg1rect)
    right(ball,stg2prect,bg1_0,bg1rect)
    right(ball,stg2prect,bg1_0,bg1rect)
    upright(ball1,stg2prect,bg1_0,bg1rect)
    upright(ball1,stg2prect,bg1_0,bg1rect)
    upright(ball2,stg2prect,bg1_0,bg1rect)
    right(ball2,stg2prect,bg1_0,bg1rect)
    right(ball3,stg2prect,bg1_0,bg1rect)
    right(ball3,stg2prect,bg1_0,bg1rect)
    right(ball,stg2prect,bg1_0,bg1rect)
    right(ball,stg2prect,bg1_0,bg1rect)
    right(ball1,stg2prect,bg1_0,bg1rect)
    right(ball1,stg2prect,bg1_0,bg1rect)
    right(ball2,stg2prect,bg1_0,bg1rect)
    time.sleep(0.5)
    trans(ball,stg2prect,bg1_0,bg1rect,player)
    time.sleep(1)
    
def stg2move1():
    trans(player,stg2prect,bg1_0,bg1rect,ball)
    time.sleep(3)
    trans(ball,stg2prect,bg1_0,bg1rect,player)
def stg2move2():
    for _ in range(5):
        screen.blit(bg1_0, bg1rect)
        screen.blit(eat1,stg2prect)
        stg2prect.x += 10
        pygame.display.update()
        time.sleep(0.5)
    screen.blit(bg1, bg1rect)
    screen.blit(eat2,stg2prect)
    pygame.display.update()
    time.sleep(1)
def stg2move3():
    trans(player,stg2prect,bg1,bg1rect,plane)
    time.sleep(1)
    for _ in range(24):
        upright(plane,stg2prect,bg1,bg1rect)
        right(plane,stg2prect,bg1,bg1rect)
        upright(plane,stg2prect,bg1,bg1rect)
        right(plane,stg2prect,bg1,bg1rect)
    for _ in range(15):
        right(plane,stg2prect,bg1,bg1rect)
    for _ in range(25):
        downright(plane,stg2prect,bg1,bg1rect)
        right(plane,stg2prect,bg1,bg1rect)
    
def stg2move4():
    trans(player,stg2prect,bg1,bg1rect,ball)
    time.sleep(3)
    trans(ball,stg2prect,bg1,bg1rect,player)
def stg3move0():
    for _ in range(38):
        right(plane,stg3prect,bg2,bg2rect)
    for _ in range(13):
        downright(plane,stg3prect,bg2,bg2rect)
    time.sleep(1)
    trans(plane,stg3prect,bg2,bg2rect,player)
def stg3move1():
    trans(player,stg3prect,bg2,bg2rect,ball)
    right(ball,stg3prect,bg2,bg2rect)
    right(ball,stg3prect,bg2,bg2rect)
    right(ball1,stg3prect,bg2,bg2rect)
    right(ball1,stg3prect,bg2,bg2rect)
    right(ball2,stg3prect,bg2,bg2rect)
    right(ball2,stg3prect,bg2,bg2rect)
    right(ball3,stg3prect,bg2,bg2rect)
    right(ball3,stg3prect,bg2,bg2rect)
    right(ball3,stg3prect,bg2,bg2rect)
    right(ball,stg3prect,bg2,bg2rect)
    for _ in range(3):
        downright(ball,stg3prect,bg2,bg2rect)
        downright(ball,stg3prect,bg2,bg2rect)
        downright(ball1,stg3prect,bg2,bg2rect)
        downright(ball1,stg3prect,bg2,bg2rect)
        downright(ball2,stg3prect,bg2,bg2rect)
        downright(ball2,stg3prect,bg2,bg2rect)
        downright(ball3,stg3prect,bg2,bg2rect)
        downright(ball3,stg3prect,bg2,bg2rect)
        
    
    trans(ball,stg3prect,bg2,bg2rect,player)
    
def stg3move2():
    trans(player,stg3prect,bg2,bg2rect,plane)
    for _ in range(23):
        upright(plane,stg3prect,bg2,bg2rect)
    for _ in range(23):
        upleft(plane,stg3prect,bg2,bg2rect)
    for _ in range(23):
        downleft(plane,stg3prect,bg2,bg2rect)
    for _ in range(23):
        downright(plane,stg3prect,bg2,bg2rect)
    trans(plane,stg3prect,bg2,bg2rect,player)
    
def stg3move3():
    trans(player,stg3prect,bg2,bg2rect,ball)
    time.sleep(3)
    trans(ball,stg3prect,bg2,bg2rect,player)

def stg3move4():
    trans(player,stg3prect,bg2,bg2rect,plane)
    for _ in range(100):
        upright(plane,stg3prect,bg2,bg2rect)
    
    
def sky1move():
    for _ in range(50):
        sky1prect.x += 5
        sky1prect.y -=5
        screen.blit(sky, bg2rect)
        screen.blit(plane,sky1prect)
        pygame.display.update()
        time.sleep(0.02)

    for _ in range(50):
        sky1prect.x += 5
        screen.blit(sky, bg2rect)
        screen.blit(plane,sky1prect)
        pygame.display.update()
        time.sleep(0.02)

    for _ in range(50):
        sky1prect.x += 5
        sky1prect.y +=5
        screen.blit(sky, bg2rect)
        screen.blit(plane,sky1prect)
        pygame.display.update()
        time.sleep(0.02)
        
def stg4move0():
    for _ in range(20):
        downright(plane,stg4prect,bg3_0,bg3rect)
    for _ in range(25):
        downleft(plane,stg4prect,bg3_0,bg3rect)
    for _ in range(25):
        downright(plane,stg4prect,bg3_0,bg3rect)
    for _ in range(10):
        downleft(plane,stg4prect,bg3_0,bg3rect)
    trans(plane,stg4prect,bg3_0,bg3rect,player)
    
def stg4move1():
    trans(player,stg4prect,bg3_0,bg3rect,ball)
    for _ in range(10):
        upleft(ball,stg4prect,bg3_0,bg3rect)
    for _ in range(25):
        upright(ball,stg4prect,bg3_0,bg3rect)
    for _ in range(25):
        upleft(ball,stg4prect,bg3_0,bg3rect)
    for _ in range(20):
        upright(ball,stg4prect,bg3_0,bg3rect)
    for _ in range(6):
        right(ball,stg4prect,bg3_0,bg3rect)
        right(ball,stg4prect,bg3_0,bg3rect)
        right(ball1,stg4prect,bg3_0,bg3rect)
        right(ball1,stg4prect,bg3_0,bg3rect)
        right(ball2,stg4prect,bg3_0,bg3rect)
        right(ball2,stg4prect,bg3_0,bg3rect)
        right(ball3,stg4prect,bg3_0,bg3rect)
        right(ball3,stg4prect,bg3_0,bg3rect)
    right(ball,stg4prect,bg3_0,bg3rect)
    right(ball,stg4prect,bg3_0,bg3rect)
    right(ball,stg4prect,bg3_0,bg3rect)
    for _ in range(80):
        down(ball,stg4prect,bg3_0,bg3rect)
    time.sleep(0.5)
    trans(ball,stg4prect,bg3_0,bg3rect,player)
def stg4move2():
    trans(player,stg4prect,bg3_0,bg3rect,plane)
    for _ in range(10):
        upright(plane,stg4prect,bg3_0,bg3rect)
    for _ in range(10):
        upleft(plane,stg4prect,bg3_0,bg3rect)
    for _ in range(10):
        downleft(plane,stg4prect,bg3_0,bg3rect)
    for _ in range(10):
        downright(plane,stg4prect,bg3_0,bg3rect)
    trans(plane,stg4prect,bg3_0,bg3rect,player)
def stg4move3():
    trans(player,stg4prect,bg3_0,bg3rect,ball)
    time.sleep(3)
    trans(ball,stg4prect,bg3_0,bg3rect,player)
def stg4move4():
    trans(player,stg4prect,bg3_0,bg3rect,plane)
    for _ in range(10):
        upright(plane,stg4prect,bg3_0,bg3rect)
    for _ in range(10):
        upleft(plane,stg4prect,bg3_0,bg3rect)
    for _ in range(10):
        downleft(plane,stg4prect,bg3_0,bg3rect)
    for _ in range(10):
        downright(plane,stg4prect,bg3_0,bg3rect)
    trans(plane,stg4prect,bg3_0,bg3rect,player)
def stg4move3_1():
    trans(player,stg4prect,bg3,bg3rect,ball)
    time.sleep(3)
    trans(ball,stg4prect,bg3,bg3rect,player)
def stg4move4_1():
    trans(player,stg4prect,bg3,bg3rect,plane)
    for _ in range(10):
        upright(plane,stg4prect,bg3,bg3rect)
    for _ in range(10):
        upleft(plane,stg4prect,bg3,bg3rect)
    for _ in range(10):
        downleft(plane,stg4prect,bg3,bg3rect)
    for _ in range(10):
        downright(plane,stg4prect,bg3,bg3rect)
    trans(plane,stg4prect,bg3,bg3rect,player)
def stg4move5():
    for _ in range(5):
        screen.blit(bg3_0, bg3rect)
        screen.blit(eat1,stg4prect)
        stg4prect.x += 10
        pygame.display.update()
        time.sleep(0.5)
    screen.blit(bg3, bg3rect)
    screen.blit(eat2,stg4prect)
    pygame.display.update()
    time.sleep(1)
def stg4move6():
    trans(player,stg4prect,bg3,bg3rect,car)
    for _ in range(51):
        right(car,stg4prect,bg3,bg3rect)
def stg5move0():
    for _ in range(40):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
        right(car,stg5prect,bg4,bg4rect)
    for _ in range(13):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
        up(car,stg5prect,bg4,bg4rect)
    for _ in range(75):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
        right(car,stg5prect,bg4,bg4rect)
    for _ in range(44):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
        down(car,stg5prect,bg4,bg4rect)
    for _ in range(46):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
        right(car,stg5prect,bg4,bg4rect)
    for _ in range(44):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
        up(car,stg5prect,bg4,bg4rect)
    for _ in range(22):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
        right(car,stg5prect,bg4,bg4rect)
    up(car,stg5prect,bg4,bg4rect)
    down(car,stg5prect,bg4,bg4rect)
    up(car,stg5prect,bg4,bg4rect)
    down(car,stg5prect,bg4,bg4rect)
    time.sleep(1)
def stg6move1():
    trans(player,stg6prect,bg5,bg3rect,ball)
    for _ in range(5):
        right(ball,stg6prect,bg5,bg3rect)
        right(ball,stg6prect,bg5,bg3rect)
        right(ball1,stg6prect,bg5,bg3rect)
        right(ball1,stg6prect,bg5,bg3rect)
        right(ball2,stg6prect,bg5,bg3rect)
        right(ball2,stg6prect,bg5,bg3rect)
        right(ball3,stg6prect,bg5,bg3rect)
        right(ball3,stg6prect,bg5,bg3rect)
    left(ball,stg6prect,bg5,bg3rect)
    left(ball,stg6prect,bg5,bg3rect)
    left(ball3,stg6prect,bg5,bg3rect)
    left(ball3,stg6prect,bg5,bg3rect)
    left(ball2,stg6prect,bg5,bg3rect)
    left(ball2,stg6prect,bg5,bg3rect)
    left(ball1,stg6prect,bg5,bg3rect)
    left(ball1,stg6prect,bg5,bg3rect)
    trans(ball,stg6prect,bg5,bg3rect,player)
def stg6move1_1():
    trans(player,stg6prect,bg5,bg3rect,ball)
    for _ in range(5):
        right(ball,stg6prect,bg5,bg3rect)
        right(ball,stg6prect,bg5,bg3rect)
        right(ball1,stg6prect,bg5,bg3rect)
        right(ball1,stg6prect,bg5,bg3rect)
        right(ball2,stg6prect,bg5,bg3rect)
        right(ball2,stg6prect,bg5,bg3rect)
        right(ball3,stg6prect,bg5,bg3rect)
        right(ball3,stg6prect,bg5,bg3rect)
    right(ball,stg6prect,bg5,bg3rect)
    left(ball,stg6prect,bg5,bg3rect)
    left(ball,stg6prect,bg5,bg3rect)
    left(ball3,stg6prect,bg5,bg3rect)
    left(ball3,stg6prect,bg5,bg3rect)
    left(ball2,stg6prect,bg5,bg3rect)
    left(ball2,stg6prect,bg5,bg3rect)
    left(ball1,stg6prect,bg5,bg3rect)
    left(ball1,stg6prect,bg5,bg3rect)
    trans(ball,stg6prect,bg5,bg3rect,player)
def stg6move2():
    trans(player,stg6prect,bg5,bg2rect,plane)
    upright(plane,stg6prect,bg5,bg3rect)
    upright(plane,stg6prect,bg5,bg3rect)
    upright(plane,stg6prect,bg5,bg3rect)
    upright(plane,stg6prect,bg5,bg3rect)
    downleft(plane,stg6prect,bg5,bg3rect)
    downleft(plane,stg6prect,bg5,bg3rect)
    downleft(plane,stg6prect,bg5,bg3rect)
    downleft(plane,stg6prect,bg5,bg3rect)
    trans(plane,stg6prect,bg5,bg2rect,player)
def stg6move3():
    for _ in range(3):
        screen.blit(bg5, bg3rect)
        screen.blit(smoke0, stg6prect)
        pygame.display.update()
        time.sleep(0.5)
        screen.blit(bg5, bg3rect)
        screen.blit(smoke1, stg6prect)
        pygame.display.update()
        time.sleep(0.5)
    screen.blit(bg5, bg3rect)
    screen.blit(player,stg6prect)
    pygame.display.update()
    time.sleep(1)
def stg6move4():
    trans(player,stg6prect,bg5,bg3rect,ball)
    right(ball,stg6prect,bg5,bg3rect)
    right(ball,stg6prect,bg5,bg3rect)
    right(ball1,stg6prect,bg5,bg3rect)
    right(ball1,stg6prect,bg5,bg3rect)
    right(ball2,stg6prect,bg5,bg3rect)
    right(ball2,stg6prect,bg5,bg3rect)
    right(ball3,stg6prect,bg5,bg3rect)
    right(ball3,stg6prect,bg5,bg3rect)
    left(ball,stg6prect,bg5,bg3rect)
    left(ball,stg6prect,bg5,bg3rect)
    left(ball3,stg6prect,bg5,bg3rect)
    left(ball3,stg6prect,bg5,bg3rect)
    left(ball2,stg6prect,bg5,bg3rect)
    left(ball2,stg6prect,bg5,bg3rect)
    left(ball1,stg6prect,bg5,bg3rect)
    left(ball1,stg6prect,bg5,bg3rect)
    trans(ball,stg6prect,bg5,bg3rect,player)
def stg6move5():
    trans(player,stg6prect,bg5,bg2rect,plane)
    for _ in range(20):
        upright(plane,stg6prect,bg5,bg3rect)
    for _ in range(10):
        upleft(plane,stg6prect,bg5,bg3rect)
    for _ in range(13):
        left(plane,stg6prect,bg5,bg3rect)
    for _ in range(15):
        downleft(plane,stg6prect,bg5,bg3rect)
    trans(plane,stg6prect,bg5,bg2rect,player)
def stg6move6():
    trans(player,stg6prect,bg5,bg2rect,ball)
    for _ in range(6):
        right(ball,stg6prect,bg5,bg3rect)
        right(ball,stg6prect,bg5,bg3rect)
        right(ball1,stg6prect,bg5,bg3rect)
        right(ball1,stg6prect,bg5,bg3rect)
        right(ball2,stg6prect,bg5,bg3rect)
        right(ball2,stg6prect,bg5,bg3rect)
        right(ball3,stg6prect,bg5,bg3rect)
        right(ball3,stg6prect,bg5,bg3rect)
    downright(ball,stg6prect,bg5,bg3rect)
    downright(ball,stg6prect,bg5,bg3rect)
    downright(ball1,stg6prect,bg5,bg3rect)
    downright(ball1,stg6prect,bg5,bg3rect)
    downright(ball2,stg6prect,bg5,bg3rect)
    downright(ball2,stg6prect,bg5,bg3rect)
    downright(ball3,stg6prect,bg5,bg3rect)
    downright(ball3,stg6prect,bg5,bg3rect)
    downright(ball,stg6prect,bg5,bg3rect)
    downright(ball,stg6prect,bg5,bg3rect)
    for _ in range(12):
        right(ball,stg6prect,bg5,bg3rect)
        right(ball,stg6prect,bg5,bg3rect)
        right(ball1,stg6prect,bg5,bg3rect)
        right(ball1,stg6prect,bg5,bg3rect)
        right(ball2,stg6prect,bg5,bg3rect)
        right(ball2,stg6prect,bg5,bg3rect)
        right(ball3,stg6prect,bg5,bg3rect)
        right(ball3,stg6prect,bg5,bg3rect)
def stg6move7():
    trans(player,stg6prect,bg5,bg2rect,plane)
    for _ in range(20):
        upright(plane,stg6prect,bg5,bg3rect)
    for _ in range(20):
        upleft(plane,stg6prect,bg5,bg3rect)
    for _ in range(20):
        downleft(plane,stg6prect,bg5,bg3rect)
    for _ in range(20):
        downright(plane,stg6prect,bg5,bg3rect)
    trans(plane,stg6prect,bg5,bg2rect,player)
    
def stg7move0():
    right(ball,stg7prect,bg7_0,bg2rect)
    right(ball,stg7prect,bg7_0,bg2rect)
    right(ball1,stg7prect,bg7_0,bg2rect)
    right(ball1,stg7prect,bg7_0,bg2rect)
    right(ball2,stg7prect,bg7_0,bg2rect)
    right(ball2,stg7prect,bg7_0,bg2rect)
    right(ball3,stg7prect,bg7_0,bg2rect)
    right(ball3,stg7prect,bg7_0,bg2rect)
    right(ball,stg7prect,bg7_0,bg2rect)
    right(ball,stg7prect,bg7_0,bg2rect)
    
    for _ in range(2):
        upright(ball,stg7prect,bg7_0,bg2rect)
        upright(ball,stg7prect,bg7_0,bg2rect)
        upright(ball1,stg7prect,bg7_0,bg2rect)
        upright(ball1,stg7prect,bg7_0,bg2rect)
        upright(ball2,stg7prect,bg7_0,bg2rect)
        upright(ball2,stg7prect,bg7_0,bg2rect)
        upright(ball3,stg7prect,bg7_0,bg2rect)
        upright(ball3,stg7prect,bg7_0,bg2rect)
    upright(ball,stg7prect,bg7_0,bg2rect)
    upright(ball,stg7prect,bg7_0,bg2rect)
    upright(ball1,stg7prect,bg7_0,bg2rect)
    upright(ball1,stg7prect,bg7_0,bg2rect)
    time.sleep(0.5)
    trans(ball,stg7prect,bg7_0,bg2rect,player)
def stg7move1():
    trans(player,stg7prect,bg7_0,bg2rect,ball)
    time.sleep(3)
    trans(ball,stg7prect,bg7_0,bg2rect,player)
def stg7move2():
    trans(player,stg7prect,bg7_0,bg2rect,plane)
    time.sleep(1)
    for _ in range(23):
        upright(plane,stg7prect,bg7_0,bg2rect)
    for _ in range(15):
        right(plane,stg7prect,bg7_0,bg2rect)
    time.sleep(0.5)
    trans(plane,stg7prect,bg7_0,bg2rect,player)
def stg7move3():
  trans(player,stg7prect,bg7_0,bg2rect,ball)
  for _ in range(8):
    right(ball,stg7prect,bg7,bg0rect,sship, sshiprect)
    right(ball,stg7prect,bg7,bg0rect,sship, sshiprect)
    downright(ball1,stg7prect,bg7,bg0rect,sship, sshiprect)
    right(ball1,stg7prect,bg7,bg0rect,sship, sshiprect)
    right(ball2,stg7prect,bg7,bg0rect,sship, sshiprect)
    downright(ball2,stg7prect,bg7,bg0rect,sship, sshiprect)
    right(ball3,stg7prect,bg7,bg0rect,sship, sshiprect)
    downright(ball3,stg7prect,bg7,bg0rect,sship, sshiprect)
  for _ in range(16):
    right(ball,stg7prect,bg7,bg0rect,sship, sshiprect)
  end2()
def stg7move4():
    trans(player,stg7prect,bg7_0,bg2rect,plane)
    for _ in range(23):
        upright(plane,stg7prect,bg7_0,bg2rect)
    for _ in range(23):
        upleft(plane,stg7prect,bg7_0,bg2rect)
    for _ in range(23):
        downleft(plane,stg7prect,bg7_0,bg2rect)
    for _ in range(24):
        downright(plane,stg7prect,bg7_0,bg2rect)
    time.sleep(0.5)
    trans(plane,stg7prect,bg7_0,bg2rect,player)
    for _ in range(100):
        sshiprect.y -= 5
        screen.blit(bg7, bg0rect)
        screen.blit(player, stg7prect)
        screen.blit(sship2,sshiprect)
        pygame.display.update()
        time.sleep(0.03)
    
def stg7move5():
  trans(player,stg7prect,bg7,bg2rect,ball)
  for _ in range(9):
    right(ball,stg7prect,bg7,bg0rect)
    right(ball,stg7prect,bg7,bg0rect)
    downright(ball1,stg7prect,bg7,bg0rect)
    right(ball1,stg7prect,bg7,bg0rect)
    right(ball2,stg7prect,bg7,bg0rect)
    downright(ball2,stg7prect,bg7,bg0rect)
    right(ball3,stg7prect,bg7,bg0rect)
    downright(ball3,stg7prect,bg7,bg0rect)
  for _ in range(6):
      right(ball,stg7prect,bg7,bg0rect)
      right(ball,stg7prect,bg7,bg0rect)
      right(ball1,stg7prect,bg7,bg0rect)
      right(ball1,stg7prect,bg7,bg0rect)
      right(ball2,stg7prect,bg7,bg0rect)
      right(ball2,stg7prect,bg7,bg0rect)
      right(ball3,stg7prect,bg7,bg0rect)
      right(ball3,stg7prect,bg7,bg0rect)
  downright(ball,stg7prect,bg7,bg0rect)
  downright(ball,stg7prect,bg7,bg0rect)
  downright(ball1,stg7prect,bg7,bg0rect)
  for _ in range(20):
      right(ball1,stg7prect,bg7,bg0rect)
  end3()
  
    
def stg7move6():
    trans(player,stg7prect,bg7_0,bg2rect,plane)
    for _ in range(23):
        right(plane,stg7prect,bg7_0,bg2rect)
        up(plane,stg7prect,bg7_0,bg2rect)
    for _ in range(23):
        left(plane,stg7prect,bg7_0,bg2rect)
        up(plane,stg7prect,bg7_0,bg2rect)
    for _ in range(23):
        left(plane,stg7prect,bg7_0,bg2rect)
        down(plane,stg7prect,bg7_0,bg2rect)
    for _ in range(23):
        right(plane,stg7prect,bg7_0,bg2rect)
        down(plane,stg7prect,bg7_0,bg2rect)
    trans(plane,stg7prect,bg7_0,bg2rect,player)
def stg7move7():
    trans(player,stg7prect,bg7_0,bg2rect,car)
    time.sleep(2)
    trans(car,stg7prect,bg7_0,bg2rect,player)
def stg7move7_1():
    trans(player,stg7prect,bg7,bg2rect,car)
    time.sleep(2)
    trans(car,stg7prect,bg7,bg2rect,player)

#엔딩
def end1():
    stg6prect.x+=10
    stg6prect.y-=20
    for _ in range(6):
        screen.blit(bg5, bg3rect)
        screen.blit(smoke0, stg6prect)
        pygame.display.update()
        time.sleep(0.5)
        screen.blit(bg5, bg3rect)
        screen.blit(smoke1, stg6prect)
        pygame.display.update()
        time.sleep(0.5)
    time.sleep(1)
    while True:
      for _ in range(200):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
        end2sshiprect.x -= 5            
        end2sshiprect.y -= 5
        screen.blit(end1bg, bg2rect)
        screen.blit(plane,end2sshiprect)
        pygame.display.update()
        time.sleep(0.03)
      end2sshiprect.x = 750
      end2sshiprect.y = 550
      for _ in range(150):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
        uforect.x += 5
        uforect.y -= 5
        screen.blit(end1bg, bg0rect)
        screen.blit(ball,uforect)
        pygame.display.update()
        time.sleep(0.03)
      uforect.x =  200
      uforect.y = 550
def end2():
  for _ in range(100):
    sshiprect.y -= 5
    screen.blit(bg7, bg0rect)
    screen.blit(sship2,sshiprect)
    pygame.display.update()
    time.sleep(0.03)
  while True:
    for _ in range(200):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
        end2sshiprect.x -= 5            
        end2sshiprect.y -= 5
        screen.blit(end2bg, bg2rect)
        screen.blit(sship3,end2sshiprect)
        pygame.display.update()
        time.sleep(0.03)
    end2sshiprect.x = 750
    end2sshiprect.y = 550
    for _ in range(150):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
        uforect.x += 5
        uforect.y -= 5
        screen.blit(end2bg, bg0rect)
        screen.blit(ufo,uforect)
        pygame.display.update()
        time.sleep(0.03)
    uforect.x =  200
    uforect.y = 550
def end3():
    for _ in range(30):
      right(ball,end3prect,end3bg,bg0rect)
      right(ball,end3prect,end3bg,bg0rect)
    time.sleep(0.5)
    trans(ball,end3prect,end3bg,bg0rect,player)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
        screen.blit(end3bg, bg2rect)
        screen.blit(player,end3prect)
        pygame.display.update()
#종료    
def exit():
  pygame.quit()
  sys.exit()

#main
while True:
  if stg==0:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
    pygame.display.flip()
    screen.blit(title, titlerect)
    click = pygame.mouse.get_pressed()
    if (click[0] == 1):
        stg=1
        
  if stg==1:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
                
    pygame.display.flip()
    screen.blit(bg0, bg0rect)
    if stg1prect.x==123 and stg1prect.y==163:
        
        button(0,450,960,150,white,grey,'stg1move2')
        if stg1prect.x==1003 and stg1prect.y==268:
            stg=2
        screen.blit(ballbutton,ballbutton1rect)
        
    if stg1prect.x==98 and stg1prect.y==163:
        screen.blit(ball,ballrect)
        button(0,450,960,150,white,grey,'stg1move1')
        screen.blit(plusbutton,plusbutton1rect)
    screen.blit(player, stg1prect)       
        
  if stg==2:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
                
    pygame.display.flip()
    if stg2prect.x==0 and stg2prect.y==350:
        screen.blit(bg1_0, bg1rect)
        screen.blit(player, stg2prect)
        stg2move0()
    if stg2prect.x==155 and stg2prect.y==335:
        screen.blit(bg1, bg1rect)
        screen.blit(player, stg2prect)
        button(0,450,480,150,white,grey,'stg2move4')
        button(480,450,480,150,dwhite,dgrey,'stg2move3')
        if stg2prect.x==960 and stg2prect.y==220:
            stg=3
        screen.blit(ballbutton,ballbutton2rect)
        screen.blit(planebutton,planebutton2rect)
    if stg2prect.x==105 and stg2prect.y==335:
        screen.blit(bg1_0, bg1rect)
        screen.blit(player, stg2prect)
        button(0,450,480,150,white,grey,'stg2move1')
        button(480,450,480,150,dwhite,dgrey,'stg2move2')
        screen.blit(ballbutton,ballbutton2rect)
        screen.blit(plusbutton,plusbutton2rect)
    
  if stg==3:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
    if stg3prect.x==0 and stg3prect.y==220:
        screen.blit(bg2, bg2rect)
        screen.blit(plane, stg3prect)
        stg3move0()
    pygame.display.flip()
    screen.blit(bg2, bg2rect)
    screen.blit(player, stg3prect)
    if stg3prect.x==425 and stg3prect.y==405:
        button(0,450,480,150,white,grey,'stg3move3')
        button(480,450,480,150,dwhite,dgrey,'stg3move4')
        if stg3prect.x==925 and stg3prect.y==-95:
            stg='sky1'
        screen.blit(ballbutton,ballbutton2rect)
        screen.blit(planebutton,planebutton2rect)
    if stg3prect.x==255 and stg3prect.y==285:
        button(0,450,480,150,white,grey,'stg3move1')
        button(480,450,480,150,dwhite,dgrey,'stg3move2')
        screen.blit(ballbutton,ballbutton2rect)
        screen.blit(planebutton,planebutton2rect)

  if stg=='sky1':
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
    if sky1prect.x==100 and sky1prect.y==550:
        sky1move()
    pygame.display.flip()
    screen.blit(sky, bg2rect)
    screen.blit(plane, sky1prect)
    if sky1prect.x==850 and sky1prect.y==550:
        stg=4
    
  if stg==4:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
    pygame.display.flip()
    if stg4prect.x==705 and stg4prect.y==400:
        screen.blit(bg3, bg3rect)
        screen.blit(player, stg4prect)
        button(0,450,320,150,white,grey,'stg4move3_1')
        button(320,450,320,150,dwhite,dgrey,'stg4move4_1')
        button(640,450,320,150,grey,sdgrey,'stg4move6')
        if stg4prect.x==960 and stg4prect.y==400:
            stg=5
        screen.blit(ballbutton,ballbutton3rect)
        screen.blit(planebutton,planebutton3rect)
        screen.blit(carbutton,carbutton3rect)
    if stg4prect.x==655 and stg4prect.y==400:
        screen.blit(bg3_0, bg3rect)
        screen.blit(player, stg4prect)
        button(0,450,320,150,white,grey,'stg4move3')
        button(320,450,320,150,dwhite,dgrey,'stg4move4')
        button(640,450,320,150,grey,sdgrey,'stg4move5')
        screen.blit(ballbutton,ballbutton3rect)
        screen.blit(planebutton,planebutton3rect)
        screen.blit(plusbutton,plusbutton3rect)
    if stg4prect.x==350 and stg4prect.y==400:
        screen.blit(bg3_0, bg3rect)
        screen.blit(player, stg4prect)
        button(0,450,480,150,white,grey,'stg4move1')
        button(480,450,480,150,dwhite,dgrey,'stg4move2')
        screen.blit(ballbutton,ballbutton2rect)
        screen.blit(planebutton,planebutton2rect)
        
    if stg4prect.x==300 and stg4prect.y==0:
        screen.blit(bg3_0, bg3rect)
        screen.blit(plane, stg4prect)
        stg4move0()            
    
  if stg==5:
    pygame.display.flip()
    if stg5prect.x==-100 and stg5prect.y==300:
        screen.blit(bg4, bg4rect)
        screen.blit(car, stg5prect)
        stg5move0()
        stg=6
    
  if stg==6:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
    if stg6prect.x==200 and stg6prect.y==390:
        screen.blit(bg5, bg4rect)
        screen.blit(player, stg6prect)
        button(0,0,130,275,white,grey,'stg6move6')
        button(0,275,130,275,dwhite,dgrey,'stg6move7')
        button(830,0,130,275,grey,sdgrey,'stg6move3')
        button(830,275,130,275,dgrey,white,'stg6move8')
        if stg6prect.x==970 and stg6prect.y==440:
           stg=7
        screen.blit(ballbutton,ballbutton4rect)
        screen.blit(planebutton,planebutton4rect)
        screen.blit(carbutton,carbutton5rect)
        screen.blit(edbutton,edbuttonrect)
    if stg6prect.x==290 and stg6prect.y==465:
        screen.blit(bg5, bg4rect)
        screen.blit(player, stg6prect)
        button(0,0,130,275,white,grey,'stg6move4')
        button(0,275,130,275,dwhite,dgrey,'stg6move5')
        button(830,0,130,550,grey,sdgrey,'stg6move3')
        screen.blit(ballbutton,ballbutton4rect)
        screen.blit(planebutton,planebutton4rect)
        screen.blit(carbutton,carbutton4rect)
    if stg6prect.x==130 and stg6prect.y==465:
        screen.blit(bg5, bg4rect)
        screen.blit(player, stg6prect)
        button(0,0,130,275,white,grey,'stg6move1')
        button(0,275,130,275,dwhite,dgrey,'stg6move2')
        button(830,0,130,550,grey,sdgrey,'stg6move3')
        screen.blit(ballbutton,ballbutton4rect)
        screen.blit(planebutton,planebutton4rect)
        screen.blit(carbutton,carbutton4rect)
    pygame.display.flip()

  if stg==7:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
    pygame.display.flip()
    if stg7prect.x==245 and stg7prect.y==190:
        screen.blit(bg7, bg2rect)
        screen.blit(player, stg7prect)
        button(0,450,320,150,white,grey,'stg7move5')
        button(320,450,320,150,dwhite,dgrey,'stg7move6')
        button(640,450,320,150,grey,sdgrey,'stg7move7_1')
        screen.blit(ballbutton,ballbutton3rect)
        screen.blit(planebutton,planebutton3rect)
        screen.blit(carbutton,carbutton3rect)
    if stg7prect.x==240 and stg7prect.y==185:
        screen.blit(bg7_0, bg2rect)
        screen.blit(player, stg7prect)
        screen.blit(sship, sshiprect)
        button(0,450,320,150,white,grey,'stg7move3')
        button(320,450,320,150,dwhite,dgrey,'stg7move4')
        button(640,450,320,150,grey,sdgrey,'stg7move7')
        screen.blit(ballbutton,ballbutton3rect)
        screen.blit(planebutton,planebutton3rect)
        screen.blit(carbutton,carbutton3rect)
    if stg7prect.x==50 and stg7prect.y==300:
        screen.blit(bg7_0, bg2rect)
        screen.blit(player, stg7prect)
        screen.blit(sship, sshiprect)
        button(0,450,320,150,white,grey,'stg7move1')
        button(320,450,320,150,dwhite,dgrey,'stg7move2')
        button(640,450,320,150,grey,sdgrey,'stg7move7')
        screen.blit(ballbutton,ballbutton3rect)
        screen.blit(planebutton,planebutton3rect)
        screen.blit(carbutton,carbutton3rect)
    if stg7prect.x==-100 and stg7prect.y==400:
        screen.blit(bg7_0, bg2rect)
        screen.blit(player, stg7prect)
        screen.blit(sship, sshiprect)
        stg7move0()
        

  clock.tick(30)


pygame.quit()

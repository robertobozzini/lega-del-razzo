
import pygame,sys
#importa #altre funzioni da pygame
from pygame.locals import *
from random import randint
#from ball import Ball
from car import Car
from ball import Ball
pygame.init()

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
purlpe=(128,0,128)
grey=(128, 128, 128)


#green=pygame.transform.scale(greenn, (1800, 1000))
#pygame.transform.rotate
fps=90
fpsclock=pygame.time.Clock()
pygame.display.set_caption("lega del razzo")

WIDTH=1800
HEIGHT=1000
screen=pygame.display.set_mode((WIDTH,HEIGHT))
display = pygame.Surface((1800, 1000))


mappa=pygame.image.load("./immagini/mappa.png")
mappa=pygame.transform.scale(mappa, (1800, 1000))
font=pygame.font.Font("freesansbold.ttf",32)
testo=font.render("secondi=", True, black, white)
spaziotesto=testo.get_rect()
spaziotesto.center=(0,0)

car1=Car(display,1,1)
car2=Car(display,2,2)
ball=Ball(WIDTH,HEIGHT,display)

conta=0
while True:

    #if car1.muoviruota(conta):
        #conta=0
    #else: conta+=1
    #car1.Onground()
    #screen.blit(mappa,(0,0))
    display.blit(mappa,(0,0))
    car1.Draw()
    print("right left top bottom")
    #print(car1.x+car1.width,car1.x,car1.y,car1.y+car1.height)
    
    #print(ball.punticardinali)
    #print(ball.puntistorti)


    
    #print(car1.angle)
    k = pygame.key.get_pressed()
        #car1
    #cond1=
    ball.collide(car1)
    #print(ball.cond)
    ball.Draw()
    screen.blit(display,(0,0))
    ball.Move()

    #if not cond1:
    if (k[K_w] or k[K_s] or k[K_a] or k[K_d]):
        if car1.y<=700:
            car1.y+=7
    if k[K_w]:
        car1.move("up")
        #print("up",end=" ")
        #print(car1.dove)
    elif k[K_s]:
        car1.move("down")
        #print("down",end=" ")w
        #print(car1.dove)
    if k[K_a]:
        car1.move("left")
    elif k[K_d]:
        car1.move("right")

    #if not car1.hit("down"):
     #   car1.y=car1.y*1.1
    '''
    if not ball.collide(car2):
        if k[K_UP]:
            car2.move("up")
            #print("up",end=" ")
            #print(car1.dove)
        elif k[K_DOWN]:
            car2.move("down")
            #print("down",end=" ")
            #print(car1.dove)
        if k[K_LEFT]:
            car2.move("left")
        elif k[K_RIGHT]:
            car2.move("right")
    '''
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ball.dirx=5
    if ball.gol():
        pass
        
        #elif event.type==pygame.KEYDOWN:
        '''
        k = pygame.key.get_pressed()
            #car1
        if k[K_w]:
            car1.move("up")
        elif k[K_s]:
            car1.move("down")
        if k[K_a]:
            car1.move("left")
        elif k[K_d]:
            car1.move("right")
        '''


        
            #car2
            #if k[K_UP]:
            #if k[K_LEFT]:
            #if k[K_DOWN]:
            #if k[K_RIGHT]:

            
    fpsclock.tick(fps)
    pygame.display.update()
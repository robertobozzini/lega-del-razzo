
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
fps=60
fpsclock=pygame.time.Clock()
pygame.display.set_caption("lega del razzo")

WIDTH=1800
HEIGHT=1000
screen=pygame.display.set_mode((WIDTH,HEIGHT))
display = pygame.Surface((1800, 1000))


mappa=pygame.image.load("./immagini/mappa.png")
mappa=pygame.transform.scale(mappa, (1800, 1000))
font=pygame.font.Font("freesansbold.ttf",32)
#testo=font.render("secondi=", True, black, white)
#spaziotesto=testo.get_rect()
#spaziotesto.center=(0,0)
gravit=3

car1=Car(display,1,1,0,gravit)
car2=Car(display,2,2,180,gravit)
ball=Ball(WIDTH,HEIGHT,display)
font=font = pygame.font.Font(None, 70)


punteggio=font.render(f'{ball.punteggio[0]}                   {ball.punteggio[1]}', True, "White", None)
rectpunti=punteggio.get_rect()#midtop=
rectpunti.topleft=(890-rectpunti.right/2, 100)
conta=0
cond=False
cond2=False

def schermata():
     
while True:

    #if car1.muoviruota(conta):
        #conta=0
    #else: conta+=1
    #car1.Onground()
    
    display.blit(mappa,(0,0))
    car1.Draw()
    car2.Draw()
    #print("right left top bottom")
    #print(car1.x+car1.width,car1.x,car1.y,car1.y+car1.height)
    
    #print(ball.punticardinali)
    #print(ball.puntistorti)


    k = pygame.key.get_pressed()


    cond=ball.collide(car1)
    #print(ball.cond)
    ball.Draw()
    screen.blit(display,(0,0))
    ball.Move()

    if ball.gol():
        car1.golcar()
        car1.Draw()
        car2.golcar()
        car2.Draw()

    punteggio=font.render(f'{ball.punteggio[1]}                   {ball.punteggio[0]}', True, "White", None)
   # rectpunti=punteggio.get_rect()#midtop=
    #rectpunti.topleft=(920-rectpunti.right/2, 100)
    screen.blit(punteggio, rectpunti)



    
    if (k[K_w] or k[K_s] or k[K_a] or k[K_d]):
        if car1.y<850-car1.height:
            car1.y+=gravit
    if k[K_w]:
        car1.move("up",cond)

    elif k[K_s]:
        car1.move("down",cond)

    if k[K_a]:
        car1.move("left",cond)
    elif k[K_d]:
        car1.move("right",cond)
 
 #bisgona mettere hitbox car 2

    if (k[K_UP] or k[K_DOWN] or k[K_LEFT] or k[K_RIGHT]):
        if car2.y<850-car2.height:
            car2.y+=gravit
    cond2=ball.collide(car2)

    if k[K_UP]:
        car2.move("up",cond2)
    elif k[K_DOWN]:
        car2.move("down", cond2)
            #print("down",end=" ")
            #print(car1.dove)
    if k[K_LEFT]:
            car2.move("left", cond2)
    elif k[K_RIGHT]:
            car2.move("right", cond2)

    ball.Draw()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        #elif event.type==pygame.KEYDOWN:
            ##if event.key == pygame.K_RIGHT:
                #ball.dirx=5

        
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
    screen.blit(punteggio, rectpunti)
    fpsclock.tick(fps)
    pygame.display.update()
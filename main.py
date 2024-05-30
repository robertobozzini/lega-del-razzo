
import pygame,sys

from pygame.locals import *
from random import randint

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

def schermata(screen):
    schermata=pygame.Surface((1800, 1000))
    schermata=pygame.image.load("./immagini/SCHERMO.png")
    schermata=pygame.transform.scale(schermata,(1800,1000))
    rectone=schermata.get_rect()

    font=pygame.font.Font(None, 70)
    gioca=font.render("GIOCA", True, "white", None)
    rectbot=gioca.get_rect(midbottom=(900,600))
    clock=pygame.time.Clock()
    fps=60
    b=True
    while b==True:
        lista=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                if rectbot.collidepoint(lista):
                    b=False

        screen.blit(schermata,rectone)
        screen.blit(gioca,rectbot)
        clock.tick(fps)
        pygame.display.flip()


def schermatafinale(screen,chi):
    font=font = pygame.font.Font(None, 120)
    schermata1=pygame.Surface((1800, 1000))
    schermata1=pygame.image.load("./immagini/SCHERMO.png")
    schermata1=pygame.transform.scale(schermata1,(1800,1000))
    rectone=schermata1.get_rect()
    if chi==1:
        chihavinto=font.render("HA VINTO GIOCATORE 1", True, "White", None)
    else:
        chihavinto=font.render("HA VINTO GIOCATORE 2", True, "White", None)
    rectchi=chihavinto.get_rect()
    rectchi.left=900-rectchi.right/2
    rectchi.top=400
    clock=pygame.time.Clock()
    fps=60

    while True:
        screen.blit(schermata1,rectone)
        screen.blit(chihavinto,rectchi)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==K_ESCAPE:
                    pygame.quit()
        clock.tick(fps)
        pygame.display.flip()


schermata(screen)
while True:


    display.blit(mappa,(0,0))
    car1.Draw()
    car2.Draw()

    k = pygame.key.get_pressed()


    cond=ball.collide(car1)
    
    ball.Draw()
    screen.blit(display,(0,0))
    ball.Move()

    if ball.gol():
        car1.golcar()
        car1.Draw()
        car2.golcar()
        car2.Draw()


    punteggio=font.render(f'{ball.punteggio[1]}                   {ball.punteggio[0]}', True, "White", None)

    screen.blit(punteggio, rectpunti)
    if ball.punteggio[1]==5:
        schermatafinale(screen,1)
    elif ball.punteggio[0]==5:
        schermatafinale(screen,2)


    
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

    if k[K_LEFT]:
            car2.move("left", cond2)
    elif k[K_RIGHT]:
            car2.move("right", cond2)

    ball.Draw()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                ball.punteggio=[0,0]
                car1.golcar()
                car1.Draw()
                car2.golcar()
                car2.Draw()
                ball.x=ball.WIDTH//2-(ball.dim/2)
                ball.y=ball.HEIGHT//2-(ball.dim/2)
                ball.pos=(ball.x,ball.y)
                ball.rect=ball.image.get_rect()
                ball.dirx=0
                ball.diry=0
                schermata(screen)


    screen.blit(punteggio, rectpunti)
    fpsclock.tick(fps)
    pygame.display.update()
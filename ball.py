import pygame,math,sys,random

class Ball:
    def __init__(self,WIDTH,HEIGHT,display):
        self.x=WIDTH//2-(270/2)
        self.y=HEIGHT//2-(330/2)
        self.WIDTH=WIDTH
        self.HEIGHT=HEIGHT
        self.pos=(self.x,self.y)

        self.display=display
        
        #self.center=(self.x+self.dimensioni[0],self.y+self.dimensioni[1])
        self.image=pygame.image.load("./immagini/Ball.png")
        self.image=pygame.transform.scale(self.image, (270, 330))
        self.rect=self.image.get_rect()
        #self.dir=(0,0)
        self.dirx=0
        self.diry=0
        self.accgrav=0.2
    def Move(self):

        self.x+=self.dirx
        self.y+=self.diry
        self.pos=(self.x,self.y)

        self.rect.top=self.y
        self.rect.left=self.x

        if self.rect.left < 100 or self.rect.right > 1700:
            self.x = -self.dirx
        if self.rect.top < 30:
            self.diry = -self.diry
        if self.rect.bottom > 900:
            self.rect.bottom = 900                     # <---
            self.y = self.rect.top                               # <---
            self.diry = -self.diry
        self.dirx=self.dirx*0.99
        self.diry=self.diry*0.99+self.accgrav
        '''
        posi=self.pos
        self.x+=self.dir[0]
        self.y+=self.dir[1]+self.grav
        self.pos=(self.x,self.y)
        if !self.collider(car1,car2):  
            self.pos=posi
            self.x=self.pos[0]
            self.y=self.pos[1]
            idir=self.dir
            self.dir=(-idir[0],-idir[1])
        '''
    def Draw(self):
        self.display.blit(self.image,self.rect)
    #def collider(self,car1,car2):
        #roba con r

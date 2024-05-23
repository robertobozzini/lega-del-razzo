import pygame,math,sys,random

class Ball:
    def __init__(self,WIDTH,HEIGHT):
        self.x=WIDTH//2
        self.y=HEIGHT//2
        self.pos=(self.x,self.y)
        self.dimensioni=(x,y)
        self.center=(self.x+self.dimensioni[0],self.y+self.dimensioni[1])
        self.image=pygame.load.image("palla.png")
        self.dir=(0,0)
        self.grav=9
    def Move(self,car1,car2):
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
    def Draw(self):
        self.display.blit(self.image,self.pos)
    def collider(self,car1,car2):
        #roba con r

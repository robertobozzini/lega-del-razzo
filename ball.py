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
        self.punticardinali=[(self.x+270/2,self.y),(self.x,self.y+330/2),(self.x+270/2,self.y+330),(self.x+270,self.y+330/2)]
        self.puntistorti=[(self.x,self.y),(self.x,self.y+330),(self.x+270,self.y+330),(self.x+270,self.y)]
    def Move(self):

        self.x+=self.dirx
        self.y+=self.diry
        self.pos=(self.x,self.y)

        self.rect.top=self.y
        self.rect.left=self.x

        if (self.rect.left < 220 and self.rect.top<300) or (self.rect.left<220 and self.rect.bottom>520) or (self.rect.right>1580 and self.rect.top<300)  or (self.rect.right>1580 and self.rect.bottom>520):
            self.x = -self.dirx
        if self.rect.top < 30:
            self.diry = -self.diry
        if self.rect.bottom > 900:
            self.rect.bottom = 900                     
            self.y = self.rect.top                               
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
    def collide(self,car):
        self.punticardinali=[(self.x+270/2,self.y),(self.x,self.y+330/2),(self.x+270,self.y+330),(self.x+270/2,self.y+330)]
        self.puntistorti=[(self.x,self.y),(self.x,self.y+330),(self.x+270,self.y+330),(self.x+270,self.y)]
        #rect.collidepoint(coordinate)
        cond=False
        for i,punto in enumerate(self.punticardinali):
            if car.rect.collidepoint(punto):
                if i==0:
                    self.diry=abs(self.diry)
                elif i==1:
                    self.dirx=abs(self.dirx)
                elif i==2:
                    self.diry=-abs(self.diry)
                elif i==3:
                    self.dirx=-abs(self.dirx)
                cond=True

        for i,punto in enumerate(self.punticardinali):
            if car.rect.collidepoint(punto):
                if i==0:
                    self.diry=abs(self.diry)
                    self.dirx=abs(self.dirx)
                elif i==1:
                    self.diry=-abs(self.diry)
                    self.dirx=abs(self.dirx)
                elif i==2:
                    self.dirx=-abs(self.dirx)
                    self.diry=-abs(self.diry)
                elif i==3:
                    self.dirx=-abs(self.dirx)
                    self.diry=abs(self.diry)
                cond=True
        return cond
    
    def Draw(self):
        self.display.blit(self.image,self.rect)
    #def collider(self,car1,car2):
        #roba con r

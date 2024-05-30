import pygame,math,sys,random

class Ball:
    def __init__(self,WIDTH,HEIGHT,display):

        self.dim=139

        self.x=WIDTH//2-(self.dim/2)
        self.y=HEIGHT//2-(self.dim/2)
        self.WIDTH=WIDTH
        self.HEIGHT=HEIGHT
        self.pos=(self.x,self.y)
        self.punteggio=[0,0]
        self.display=display
        
     
        self.image=pygame.image.load("./immagini/Ballf.png")
        self.image=pygame.transform.scale(self.image, (self.dim,self.dim))
        self.rect=self.image.get_rect()
        self.rect.topleft=self.pos
        

        self.dirx=0
        self.diry=0
        self.accgrav=0.2
      
        self.speed=10

    def Move(self):

        self.x+=self.dirx
        self.y+=self.diry
        self.pos=(self.x,self.y)

        self.rect.top=self.y
        self.rect.left=self.x

        if (self.rect.left < 220 and self.rect.top<300) or (self.rect.left<220 and self.rect.bottom>520) or (self.rect.right>1580 and self.rect.top<300)  or (self.rect.right>1580 and self.rect.bottom>520):
            self.dirx = -self.dirx
        if self.rect.top < 30:
            self.diry = -self.diry
        if self.rect.bottom > 840:
            self.rect.bottom = 840                  
            self.y = self.rect.top                               
            self.diry = -self.diry
        self.dirx=self.dirx*0.99
        self.diry=self.diry*0.99+self.accgrav

    def collide(self,car):

        cond=False
  
        recc=pygame.Rect(car.x,car.y,car.rect.right,car.rect.bottom)
        if car.angle<180 and car.angle>0:
            if car.angle>90:
                recc.top-=car.width*math.sin(math.radians(car.angle))*(float(car.angle)/180.0)
            else:
                recc.top-=car.width*math.sin(math.radians(car.angle))*(float(car.angle)/90.0)
        self.recc=recc
        if self.rect.colliderect(self.recc):
            if  self.recc.bottom>self.rect.bottom and self.recc.top<self.rect.top:
                pass
            elif self.recc.bottom>self.rect.bottom:
                self.diry=-self.speed
            elif self.recc.top<self.rect.top:
                self.diry=self.speed

            if car.num==1:
                if self.recc.right>=self.x:
                    self.dirx=self.speed
                elif self.recc.left<=self.x+self.dim:
                    self.dirx=-self.speed
            else:
                if self.recc.right>=self.x:
                    self.dirx=-self.speed
                elif self.recc.left<=self.x+self.dim:
                    self.dirx=self.speed
            cond=True
        return cond
    def gol(self):

        if (self.rect.left<=220 and self.rect.top>300 and self.rect.top<520):
            self.punteggio[0]+=1
            self.x=self.WIDTH//2-(self.dim/2)
            self.y=self.HEIGHT//2-(self.dim/2)
            self.pos=(self.x,self.y)
            self.rect=self.image.get_rect()
            self.dirx=0
            self.diry=0
            return True
        if  (self.rect.right>=1580 and self.rect.top>300 and self.rect.top<520):
            self.punteggio[1]+=1
            self.x=self.WIDTH//2-(self.dim/2)
            self.y=self.HEIGHT//2-(self.dim/2)
            self.pos=(self.x,self.y)
            self.rect=self.image.get_rect()
            self.dirx=0
            self.diry=0
            return True          
        return False

    def Draw(self):
        self.display.blit(self.image,self.rect)

        

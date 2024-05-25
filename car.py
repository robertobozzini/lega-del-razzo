import pygame,math,sys,random

# dominus 1280 x 894
# octane 1280 x 894
class Car:
  def __init__(self,display,num,numcar,angle=0):

    listaimmagini=[pygame.image.load("./immagini/octane1.png"),pygame.image.load("./immagini/octane2.png"),
               pygame.image.load("./immagini/octane1r.png"),pygame.image.load("./immagini/octane2r.png"),
               pygame.image.load("./immagini/dominus1.png"),pygame.image.load("./immagini/dominus2.png"),
               pygame.image.load("./immagini/dominus1r.png"),pygame.image.load("./immagini/dominus2r.png")]
    for i,immagine in enumerate(listaimmagini):
      listaimmagini[i]=pygame.transform.scale(immagine,(256,180))


    if num==1:
      self.x=400
      self.y=700
      
      if numcar==1:
        #self.images=(pygame.image.load("./immagini/octane1.png"),pygame.image.load("./immagini/octane2.png"))
        self.images=(listaimmagini[0],listaimmagini[1])
        #self.imager=(pygame.image.load("./immagini/octane1r.png"),pygame.image.load("./immagini/octane2r.png"))
        self.imager=(listaimmagini[2],listaimmagini[3])
      else:
        #self.images=(pygame.image.load("./immagini/dominus1.png"),pygame.image.load("./immagini/dominus2.png"))
        self.images=(listaimmagini[4],listaimmagini[5])
        #self.imager=(pygame.image.load("./immagini/dominus1r.png"),pygame.image.load("./immagini/dominus2r.png"))
        self.imager=(listaimmagini[6],listaimmagini[7])
      self.image=self.images[0]
    else:
      self.x= 1300
      self.y= 700
      if numcar==1:
        #self.images=(pygame.image.load("./immagini/octane1.png"),pygame.image.load("./immagini/octane2.png"))
        self.images=(listaimmagini[0],listaimmagini[1])
        #self.imager=(pygame.image.load("./immagini/octane1r.png"),pygame.image.load("./immagini/octane2r.png"))
        self.imager=(listaimmagini[2],listaimmagini[3])
      else:
        #self.images=(pygame.image.load("./immagini/dominus1.png"),pygame.image.load("./immagini/dominus2.png"))
        self.images=(listaimmagini[4],listaimmagini[5])
        #self.imager=(pygame.image.load("./immagini/dominus1r.png"),pygame.image.load("./immagini/dominus2r.png"))
        self.imager=(listaimmagini[6],listaimmagini[7])
      self.image=self.images[1]
    self.pos=(self.x,self.y)
    self.onground=True
    self.turbo=100
    self.isturbo=0
    #self.turbimage==pygame.load.image(turbimage)
    self.angle=angle
    #pygame.transform.rotate(self.image,angle)
    self.display=display
    self.speed=5
    self.speedx=0
    self.speedy=0

  def move(self,dir):

    if dir=="right" and not self.hit("right"):
      self.speedx= self.speed
    elif dir=="left" and not self.hit("left"):
      self.speedx= -self.speed
    else:
      self.speedx=0
    if dir=="down"  and not self.hit("down"):
      self.speedy= self.speed
    elif dir=="up"  and not self.hit("up"):
      self.speedy= -self.speed
    else:
      self.speedy=0
    self.x+=self.speedx
    self.y+=self.speedy
    self.pos=(self.x,self.y)

    if self.speedx!=0:
      fspeedy,fspeedx=float(self.speedy),float(self.speedx)
      self.angle=math.atan(fspeedy/fspeedx)
  
  def Onground(self):
    
    if self.hit("down"):
      self.onground=True
    elif self.hit("up"):
      self.onground=True
      
    if self.hit("right"):
      self.onground=True

    elif self.hit("left"):
      self.onground=True

    else:
      self.onground=False
  
  def hit(self,dir):
    
    if self.x>= 1500 and dir=="right":
      self.x= 1500
      self.angle=90
      return True
    elif self.x<= 100 and dir=="left":
      self.x= 100
      self.angle=90
      return True
    
    if self.y>= 700 and dir=="down":
      self.y= 700
      self.angle=0
      return True
    elif self.y<= 100 and dir=="up":
      self.y= 100
      self.angle=180
      return True
    else:
      return False
  def Draw(self):
    self.imagetodraw=pygame.transform.rotate(self.image,self.angle)
    self.display.blit(self.imagetodraw,self.pos)

    

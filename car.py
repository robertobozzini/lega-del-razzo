import pygame,math,sys,random


class Car:
  def __init__(self,display,num,numcar,angle=0):

    listaimmagini=[pygame.image.load("./immagini/octane1.png"),pygame.image.load("./immagini/octane2.png"),
               pygame.image.load("./immagini/octane1r.png"),pygame.image.load("./immagini/octane2r.png"),
               pygame.image.load("./immagini/dominus1.png"),pygame.image.load("./immagini/dominus2.png"),
               pygame.image.load("./immagini/dominus1r.png"),pygame.image.load("./immagini/dominus2r.png")]
    for i,immagine in enumerate(listaimmagini):
      listaimmagini[i]=pygame.transform.scale(immagine,(200,100))


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

  def Onground(self):
    if self.y>= 700:
      self.y= 700
      self.onground=True
      self.angle=180
    elif self.y<= 100:
      self.y= 100
      self.onground=True
      self.angle=0
  def Draw(self):
    
    #pygame.transform.rotate(self.image,self.angle)
    self.display.blit(self.image,self.pos)

    

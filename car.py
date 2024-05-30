import pygame,math,sys,random


class Car:
  def __init__(self,display,num,numcar,angle,gravit):

    
    listaimmagini=[pygame.image.load("./immagini/octane1f.png"),pygame.image.load("./immagini/octane2f.png"),
               pygame.image.load("./immagini/octane1rf.png"),pygame.image.load("./immagini/octane2rf.png"),
               pygame.image.load("./immagini/dominus1f.png"),pygame.image.load("./immagini/dominus2.png"),
               pygame.image.load("./immagini/dominus1rf.png"),pygame.image.load("./immagini/dominus2r.png")]
    if numcar==1:
      for i in range(0,len(listaimmagini),2):
        listaimmagini[i]=pygame.transform.scale(listaimmagini[i],(212,98))
        listaimmagini[i+1]=pygame.transform.scale(listaimmagini[i+1],(212,98))
    else:
      for i in range(0,len(listaimmagini),2):
        listaimmagini[i]=pygame.transform.scale(listaimmagini[i],(242,74))
        listaimmagini[i+1]=pygame.transform.scale(listaimmagini[i+1],(242,74))
    self.dove="destra"
    self.num=num
    if num==1:
      self.x=400
      
      
      if numcar==1:

        self.images=(listaimmagini[0],listaimmagini[1])

        self.imager=(listaimmagini[2],listaimmagini[3])
        self.width=212
        self.height=98
      else:

        self.images=(listaimmagini[4],listaimmagini[5])

        self.imager=(listaimmagini[6],listaimmagini[7])
        self.width=242
        self.height=74
      self.image=self.images[0]
    else:
      self.x= 1300
      
      if numcar==1:

        self.images=(listaimmagini[0],listaimmagini[1])

        self.imager=(listaimmagini[2],listaimmagini[3])
        self.width=212
        self.height=98
      else:

        self.images=(listaimmagini[4],listaimmagini[5])

        self.imager=(listaimmagini[6],listaimmagini[7])
        self.width=242
        self.height=74
      self.image=self.imager[0]
    self.y= 850-self.height
    self.pos=(self.x,self.y)
    self.onground=True
    self.turbo=100
    self.isturbo=0

    self.angle=angle

    self.display=display
    self.speed=15
    self.gravit=gravit
    self.tophit=False
    self.dovetop=""


  def inverti(self):
    if self.image==self.images[0]:
      self.image=self.imager[0]
    elif self.image==self.images[1]:
      self.image=self.imager[1]
    elif self.image==self.imager[0]:
      self.image=self.images[0]
    elif self.image==self.imager[1]:
      self.image=self.images[1]
  
  def move(self,dir,cond):
    self.imagetodraw=pygame.transform.rotate(self.image,self.angolo)
    self.rect=self.imagetodraw.get_rect()
    if dir=="right" and not self.hit("right"):
      self.angle-=6
      #self.speedx= self.speed
    elif dir=="left" and not self.hit("left"):
      self.angle+=6
      #self.speedx= -self.speed
    if self.angle>360:
      self.angle-=360
    if self.angle<0:
      self.angle+=360
    if not cond:
      if dir=="up"  and not self.hit("up"):
        self.x+=int(math.cos(math.radians(self.angle))*self.speed)
        self.y-=int(math.sin(math.radians(self.angle))*self.speed)

        if self.dove=="sinistra":
          self.inverti()

          self.dove="destra"

      elif dir=="down"  and not self.hit("down"):
        
        self.x-=int(math.cos(math.radians(self.angle))*self.speed)
        self.y+=int(math.sin(math.radians(self.angle))*self.speed)
        #self.y=self.y*1.1
        if self.dove=="destra":

          self.inverti()

          self.dove="sinistra"
    
    self.pos=(self.x,self.y)
    if not self.hit("left"):
      if self.angle<=90 or self.angle>270:
        if self.image==self.imager[0]:
          self.image=self.images[0]
        elif self.image==self.imager[1]:
          self.image=self.images[1]
        #self.dove="destra"
      elif self.angle>90 and self.angle<=270:
        if self.image==self.images[0]:
          self.image=self.imager[0]
        elif self.image==self.images[1]:
          self.image=self.imager[1]
      #self.dove="sinistra"
    
  def muoviruota(self,conta):
    if conta==4:
      if self.speedx!=0 or self.speedy!=0:
        if self.image==self.images[0]:
          self.image=self.images[1]
        elif self.image==self.imager[0]:
          self.image=self.imager[0]
        elif self.image==self.images[1]:
          self.image=self.images[1]
        elif self.image==self.imager[1]:
          self.image=self.imager[1]
      return True
    return False
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


    self.angolo=self.angle
    if self.angle>90 and self.angle<=270:
      self.angolo-=180

    self.imagetodraw=pygame.transform.rotate(self.image,self.angolo)
    self.rect=self.imagetodraw.get_rect()

    hit=False
    if self.x+self.height> 1700:# and dir=="right":
      self.x= 1700-self.height
      if self.angle<180:
        self.angle=90
      else:
        self.angle=270
      #self.angle=90
      hit=True
    
    elif self.x==1700-self.height:
      if self.angle>=0 and self.angle<90:
        self.angle=90
        hit=True
      elif self.angle>=270 and self.angle<360:
        self.angle=270
        hit=True

    
    elif self.x< 100:# and dir=="left":
      self.x= 100
      if self.angle<180:
        self.angle=91
      else:
        self.angle=271
      hit=True

    elif self.x==100:
      if self.angle>91 and self.angle<180:
        self.angle=91
        hit=True
      elif self.angle>=180 and self.angle<271:
        self.angle=271
        hit=True


    if self.y+self.height> 850:# and dir=="down":

      self.y= 850-self.height
      if self.angle<359 and self.angle>270:
        self.angle=0

      elif self.angle<270 and self.angle>180:
        self.angle=180
      hit=True

    elif self.y+self.height== 850:
      if self.angle<359 and self.angle>270:
        self.angle=0
        hit=True
      elif self.angle<270 and self.angle>180:
        self.angle=180
        hit=True
    

    elif self.y< 30:# and dir=="up":
      self.y= 30
      self.tophit=True
      self.angle=180
      if self.angle<=90 and self.angle>0:
        self.inverti()
        self.dovetop="destra"
      else:
        self.dovetop="sinistra"
      hit=True    

    elif self.y== 30:
      if self.dovetop=="destra" and self.angle>180:
        
        self.angle=180
        hit=True
      elif self.dovetop=="sinistra" and self.angle<180:
        self.angle=180
        hit=True
    
    elif self.tophit==True:
      self.dovetop==""
      self.tophit=False
      self.inverti()

    return hit

  def golcar (self):

    if self.num==1:
      self.x=400
      self.y= 850-self.height
      self.pos=(self.x,self.y)
      if self.angle<=270 and  self.angle>90:
        self.inverti()
      self.angle=0
      self.rect=self.image.get_rect()
    else:
      self.x= 1300
      self.y= 850-self.height
      self.pos=(self.x,self.y)
      if self.angle<=90 or  self.angle>270:
        self.inverti()
      self.angle=180
      self.rect=self.image.get_rect()


  def Draw(self):
    if self.y< 850-self.height:
      self.y+=self.gravit
    
    self.pos=(self.x,self.y)
    self.angolo=self.angle
    if self.angle>90 and self.angle<=270 and not self.tophit:
      self.angolo-=180

    self.imagetodraw=pygame.transform.rotate(self.image,self.angolo)
     
    self.rect1=self.image.get_rect()
    #'''
    if self.angle >180 and self.angle< 360:#270
      ix,iy=self.rect1.topright

    else:
      ix,iy=self.rect1.bottomleft

    #'''
    self.rect=self.imagetodraw.get_rect()
    #'''
    if self.angle >180 and self.angle< 360:#270
      fx,fy=self.rect.topright

    else:
      fx,fy=self.rect.bottomleft

    dx=fx-ix
    dy=fy-iy
    x=self.x-dx
    y=self.y-dy
    pos=(x,y)

    self.display.blit(self.imagetodraw,pos)

    

import pygame,math,sys,random

# dominus 1280 x 894
# octane 1280 x 894
class Car:
  def __init__(self,display,num,numcar,angle=0):
    
    listaimmagini=[pygame.image.load("./immagini/octane1f.png"),pygame.image.load("./immagini/octane2f.png"),
               pygame.image.load("./immagini/octane1rf.png"),pygame.image.load("./immagini/octane2rf.png"),
               pygame.image.load("./immagini/dominus1.png"),pygame.image.load("./immagini/dominus2.png"),
               pygame.image.load("./immagini/dominus1r.png"),pygame.image.load("./immagini/dominus2r.png")]
    for i in range(0,len(listaimmagini),2):
      listaimmagini[i]=pygame.transform.scale(listaimmagini[i],(212,98))
      listaimmagini[i+1]=pygame.transform.scale(listaimmagini[i+1],(212,98))
    self.dove="destra"
    self.num=num
    if num==1:
      self.x=400
      self.y=700
      
      if numcar==1:
        #self.images=(pygame.image.load("./immagini/octane1.png"),pygame.image.load("./immagini/octane2.png"))
        self.images=(listaimmagini[0],listaimmagini[1])
        #self.imager=(pygame.image.load("./immagini/octane1r.png"),pygame.image.load("./immagini/octane2r.png"))
        self.imager=(listaimmagini[2],listaimmagini[3])
        self.width=212
        self.height=98
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


  def inverti(self):
    if self.image==self.images[0]:
      self.image=self.imager[0]
      return
    elif self.image==self.images[1]:
      self.image=self.imager[1]
      return
    elif self.image==self.imager[0]:
      self.image=self.images[0]
      return
    elif self.image==self.imager[1]:
      self.image=self.images[1]
      return
    return
  
  def move(self,dir):

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
    
    if dir=="up"  and not self.hit("up"):
      self.x+=int(math.cos(math.radians(self.angle))*self.speed)
      self.y-=int(math.sin(math.radians(self.angle))*self.speed)

      if self.dove=="sinistra":
        self.inverti()
        '''
        if self.image==self.images[0]:
          self.image=self.imager[0]
        elif self.image==self.images[1]:
          self.image=self.imager[1]
        elif self.image==self.imager[0]:
          self.image=self.images[0]
        elif self.image==self.imager[1]:
          self.image=self.images[1]
        '''
        self.dove="destra"

    elif dir=="down"  and not self.hit("down"):
      
      self.x-=int(math.cos(math.radians(self.angle))*self.speed)
      self.y+=int(math.sin(math.radians(self.angle))*self.speed)

      if self.dove=="destra":

        self.inverti()
        '''
        if self.image==self.images[0]:
          self.image=self.imager[0]
        elif self.image==self.images[1]:
          self.image=self.imager[1]
        elif self.image==self.imager[0]:
          self.image=self.images[0]
        elif self.image==self.imager[1]:
          self.image=self.images[1]
        '''
        self.dove="sinistra"


    self.pos=(self.x,self.y)
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
    if self.x+self.width> 1700:# and dir=="right":
      self.x= 1700-self.width
      self.angle=90
      hit=True
    elif self.x< 100:# and dir=="left":
      self.x= 100
      self.angle=270
      hit=True

    if self.y+self.height> 850:# and dir=="down":
      #if self.rect.bottom+self.y> 900:
      self.angle=0
      self.y= 850-self.height
      
      hit=True

    elif self.y< 30:# and dir=="up":
      self.y= 30
      self.angle=180
      hit=True
    '''
    if (self.dove=="destra" and dir=="right") or (self.dove=="sinistra" and dir=="left"):
      if (self.x==1500 and self.angle==90)or (self.x==100 and self.angle==90) or (self.y==700 and self.angle==0) or (self.y==100 and self.angle==180): 
        hit=True

    '''
    return hit
  #reset macchina
  def golcar (self):
    # nel main con una lista due variabili pos 0 punteggio 1 pos 1 punteggio 2
    if self.num==1:
      self.x=400
      self.y=700
      self.pos=(self.x,self.y)
      self.angle=0
      self.rect=self.image.get_rect()
    else:
      self.x= 1300
      self.y= 700
      self.pos=(self.x,self.y)
      self.angle=0
      self.rect=self.image.get_rect()


  def Draw(self):
    self.angolo=self.angle
    if self.angle>90 and self.angle<=270:
      self.angolo-=180

    self.imagetodraw=pygame.transform.rotate(self.image,self.angolo)
     
    self.rect1=self.image.get_rect()
    #'''
    if self.angle >180 and self.angle< 360:#270
      ix,iy=self.rect1.topright
    #elif self.angle >=270 and self.angle< 360:
      #ix,iy=self.rect1.topleft
    else:
      ix,iy=self.rect1.bottomleft

    #'''
    self.rect=self.imagetodraw.get_rect()
    #'''
    if self.angle >180 and self.angle< 360:#270
      fx,fy=self.rect.topright
    #elif self.angle >=270 and self.angle< 360:
      #fx,fy=self.rect.topleft
    else:
      fx,fy=self.rect.bottomleft
    '''
    if self.angle>=0 and self.angle<=180:
      if self.angle<=90:
        ix,iy=self.rect1.bottomleft
        fx,fy=self.rect.bottomleft
      else:        
        ix,iy=self.rect1.bottomright
        fx,fy=self.rect.bottomright
    else:
      if self.angle>=270:
        ix,iy=self.rect1.topleft
        fx,fy=self.rect.topleft
      else:
        ix,iy=self.rect1.topright
        fx,fy=self.rect.topright
    '''
    dx=fx-ix
    dy=fy-iy
    x=self.x-dx
    y=self.y-dy
    pos=(x,y)
    #self.x-=dx
    #self.y-=dy
    #self.pos=(self.x,self.y)
    #pygame.draw.circle(self.display,(0,0,0),(fx+self.x,fy+self.y),10,0)
    #pygame.draw.circle(self.display,(255,255,255),(ix+self.x,iy+self.y),10,0)
    self.display.blit(self.imagetodraw,pos)

    

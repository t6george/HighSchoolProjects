#Developer: Thomas George
#Date: Thursday January 21, 2016
#Game: Frogger: save a frog into its five homes; game uses lists and object oriented programming

import pygame
pygame.init()
pygame.display.set_caption("Dank Frogger")

import math
from random import randint,randrange

#PARAMETERS OF SCREEN

HEIGHT = 750           
WIDTH  = 700
screen = pygame.display.set_mode((WIDTH,HEIGHT))

###COLORS

WHITE = (255,255,255)     
BLACK = (  0,  0,  0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
ORANGE = (255,174,0)
YELLOW=(255,234,0)
PINK = (255,0,100)
darkGREEN = (0,100,0)
darkRED = (100,0,0)
songs = ["Darude - Dankstorm.mp3","3SPOOKY5ME.mp3","DeTeMiNaTiOn.mp3","Gangsta.mp3","Xx_SKRILLEX_xX.mp3"]

clock = pygame.time.Clock()

#---------------------------------------#
#   CLASSES                             #
#---------------------------------------#

## EXPLOSION SPRITE

class AnimatedSprite(pygame.sprite.Sprite):

    ##INITIAL PARAMETERS OF THE EXPLOSION
    
    def __init__(self, spritesheet, numImages = 1):
        
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        
        self.index = 0
        self.visible = False
        self.numImages = numImages
        
        self.spritesheet = pygame.image.load(spritesheet)
        self.blend_image()
        
        sheetrect = self.spritesheet.get_rect()     
        self.width,self.height = sheetrect.width, sheetrect.height
        self.width = self.width/numImages 
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
        self.update()

    ###SPAWNS SPRITESHEET WHEN THE EXPLOSION HAPPENS
        
    def spawn(self, x, y):

        self.x = x-self.rect.width/2
        self.y = y-self.rect.height/2
        
        self.rect = pygame.Rect(self.x, self.y, self.rect.width, self.rect.height)
        self.visible = True
        
        self.update()

      #DRAWS EACH IMAGE FROM THE SPRITSHEET
        
    def draw(self, surface):
        
        surface.blit(self.image, self.rect)

    ###FLIPS THROUGH THE SPRITE SHEET TO MAKE AN ANIMATION
        
    def loadNextImage(self):
        
        self.index = (self.index + 1)%self.numImages
        self.update()

    ##UPDATES THE IMAGE BEING DISPLAYED ON THE SCREEN
        
    def update(self):

        self.spritesheet.set_clip(self.width*self.index,0, self.width, self.height)
        self.image = self.spritesheet.subsurface(self.spritesheet.get_clip())

    ##BLENDS ALL THE IMAGES TOGETHER
        
    def blend_image(self):

        self.spritesheet = self.spritesheet.convert() 
        colorkey = self.spritesheet.get_at((0,0))  
        self.spritesheet.set_colorkey(colorkey)    


class Meme():

    def __init__(self):
        
        self.col = randrange(37,614,48)
        self.row = randrange(98,291,48)
        
        self.speed_X = randint(-5,5)
        self.speed_Y = randint(-5,5)

        self.change_X = randint(1,11)
        self.change_Y = randint(1,11)
        
        self.meme = pygame.image.load("img/meme.png")
        self.meme = self.meme.convert_alpha()
        self.meme = pygame.transform.scale(self.meme, (60,60))

    def fly(self):

        if self.speed_X == 0:
            self.speed_X = randint(-5,5)
            
        elif self.speed_Y == 0:
            self.speed_Y = randint(-5,5)
            
        self.col += self.speed_X
        self.row += self.speed_Y

        if self.change_X == 5:
            self.speed_X = randint(-5,5)

        if self.change_Y == 5:
            self.speed_Y = randint(-5,5)

        if self.col>615:
            self.col = 615
            self.speed_X *= -1
            
        elif self.col<35:
            self.col = 35
            self.speed_X *= -1
            
        if self.row>250:
            self.row = 250
            self.speed_Y *= -1
            
        elif self.row<100:
            self.row = 100
            self.speed_Y *= -1
            
        self.change_X = randint(1,6)
        self.change_Y = randint(1,6)
                              
###CLASS FOR ALL OBSATCLES THAT KILL FROGGER

        
class Obstacle():

    ##INITIAL PARAMETERS FOR ALL THE VEHICLES
    
    def __init__(self,row = 350,col = 750):

        self.diff = randint(450,500)

        self.col = randint(50,650)
        self.col2 = self.col + self.diff

        self.row = -75

        self.truck_speed = randint(9,12)
        self.car_speed = randint(12,16)
        self.thomas_speed = randint(15,18)
        self.sanic_speed = randint(22,25)
        self.prius_speed = randint (10,14)
        
        self.truck = pygame.image.load("img/truck.png")
        self.truck = self.truck.convert_alpha()
        self.truck = pygame.transform.scale(self.truck, (140,40))
        
        self.car = pygame.image.load("img/car.png")
        self.car = self.car.convert_alpha()
        self.car = pygame.transform.scale(self.car, (70,40))
        
        self.sanic = pygame.image.load("img/sanic.png")
        self.sanic = self.sanic.convert_alpha()
        self.sanic = pygame.transform.scale(self.sanic, (60,40))

        self.thomas = pygame.image.load("img/dankThomas.png")
        self.thomas = self.thomas.convert_alpha()
        self.thomas = pygame.transform.scale(self.thomas, (120,40))

        self.prius = pygame.image.load("img/prius.png")
        self.prius = self.prius.convert_alpha()
        self.prius = pygame.transform.scale(self.prius, (100,40))

    ##FUNCTIONS THAT GIVE THE VEHICLES MOVEMENT
        
    def truck_drive (self):
        
        self.row = 576
        self.col -= self.truck_speed
        self.col2 -= self.truck_speed
        
        if self.col<-125:
            self.col = randint(850,900)
            self.truck_speed = randint(9,12)
 
        elif self.col2<-125:
            self.col2 = self.col + self.diff

    def car_drive (self):
        
        self.row = 528
        self.col += self.car_speed
        self.col2 += self.car_speed

        if self.col>760:
            self.col = randint(-375,-275)
            self.car_speed = randint(12,16)
        
        elif self.col2>760:
            self.col2 = self.col - self.diff

    def thomas_drive (self):
        
        self.row = 480
        self.col -= self.thomas_speed
        self.col2 -= self.thomas_speed
        
        if self.col<-125:
            self.col = randint(850,925)
            self.thomas_speed = randint(15,18)
            
        elif self.col2<-125:
            self.col2 = self.col + self.diff

    def sanic_run (self):
        
        self.row = 432
        self.col += self.sanic_speed
        self.col2 += self.sanic_speed

        if self.col>785:
            self.col = randint(-375,-275)
            self.sanic_speed = randint(24,27)

        elif self.col2>785:
            self.col2 = self.col - self.diff

    def prius_drive (self):
        
        self.row = 384
        self.col -= self.prius_speed
        self.col2 -= self.prius_speed
        
        if self.col<-90:
            self.col = randint(825,875)
            self.prius_speed = randint(10,14)
            
        elif self.col2<-90:
            self.col2 = self.col + self.diff


###PLATFORMS CLASS FOR FROGGER TO LAND ON
class Platforms():

    ###INITIAL PARAMETERS FOR EACH PLATFORM
    
    def __init__(self):
        
        self.diff = 350
        self.col = -125
        
        self.col2 = self.col + self.diff
        self.col3 = self.col2 + self.diff
        
        self.row = 288
        self.row1 = 240
        self.row2 = 192
        self.row3 = 144
        self.row4 = 96
        
        self.big_log_speed = randint(8,13)
        self.dew_log_speed = randint(10,15)
        self.small_log_speed = randint(9,11)
        self.doritos_log_speed = randint(12,14)
        self.tiny_log_speed = randint(9,11)

        self.dew_log = pygame.image.load("img/dewlog.png")
        self.dew_log = self.dew_log.convert_alpha()
        self.dew_log = pygame.transform.scale(self.dew_log, (125,40))
        
        self.big_log = pygame.image.load("img/biglog.png")
        self.big_log = self.big_log.convert_alpha()
        self.big_log = pygame.transform.scale(self.big_log, (175, 40))

        self.small_log = pygame.image.load("img/smal_llog.png")
        self.small_log = self.small_log.convert_alpha()
        self.small_log = pygame.transform.scale(self.small_log, (75, 40))

        self.doritos_log = pygame.image.load("img/doritos_log.png")
        self.doritos_log = self.doritos_log.convert_alpha()
        self.doritos_log = pygame.transform.scale(self.doritos_log, (150, 40))

        self.tiny_log = pygame.image.load("img/tiny_log.png")
        self.tiny_log = self.tiny_log.convert_alpha()
        self.tiny_log = pygame.transform.scale(self.tiny_log, (50, 40))

        #FUNCTIONS THAT ALLOW THE PLATFORMS TO MOVE
        
    def dew_log_float (self):
        
        self.col += self.dew_log_speed
        self.col2 += self.dew_log_speed
        self.col3 += self.dew_log_speed

        if self.col>825:
            self.col = randint(-225,-175)
            self.dew_log_speed = randint(10,15)

        elif self.col2>825:
            self.col2 = self.col - self.diff

        elif self.col3>825:
            self.col3 = self.col2 - self.diff 
            
    def big_log_float (self):
        
        self.col -= self.big_log_speed
        self.col2 -= self.big_log_speed
        self.col3 -= self.big_log_speed

        if self.col<-175:
            self.col = randint(875,925)
            self.big_log_speed = randint(8,13)

        elif self.col2<-175:
            self.col2 = self.col + self.diff

        elif self.col3<-175:
            self.col3 = self.col2 + self.diff

    def small_log_float (self):
        
        self.col += self.small_log_speed
        self.col2 += self.small_log_speed
        self.col3 += self.small_log_speed

        if self.col>775:
            self.col = randint(-225,-175)
            self.small_log_speed = randint(9,11)

        elif self.col2>775:
            self.col2 = self.col - self.diff

        elif self.col3>775:
            self.col3 = self.col2 - self.diff

    def doritos_log_float (self):
        
        self.col -= self.doritos_log_speed
        self.col2 -= self.doritos_log_speed
        self.col3 -= self.doritos_log_speed

        if self.col<-150:
            self.col = randint(875,925)
            self.doritos_log_speed = randint(12,14)

        elif self.col2<-150:
            self.col2 = self.col + self.diff

        elif self.col3<-150:
            self.col3 = self.col2 + self.diff

    def tiny_log_float (self):
        
        self.col += self.tiny_log_speed
        self.col2 += self.tiny_log_speed
        self.col3 += self.tiny_log_speed

        if self.col>750:
            self.col = randint(-250,-150)
            self.tiny_log_speed = randint(11,16)

        elif self.col2>750:
            self.col2 = self.col - self.diff

        elif self.col3>750:
            self.col3 = self.col2 - self.diff 

###CLASS FOR THE USER-CONTROLLED FROGGER
            
class Frogger():

    #INITIAL PARAMETERS FOR FROGGER
    
    def __init__(self,row = 50,col = 50,Sprite = 1):

        self.col = 325
        self.row = 626
        self.Sprite = 1
        
        self.frogger = pygame.image.load("sprites/frogger_up.png")
        self.frogger = self.frogger.convert_alpha()
        self.frogger = pygame.transform.scale(self.frogger, (48,48))
        
        self.frogger1 = pygame.image.load("sprites/frogger_left.png")
        self.frogger1 = self.frogger1.convert_alpha()
        self.frogger1 = pygame.transform.scale(self.frogger1, (48,48))

        self.frogger2 = pygame.image.load("sprites/frogger_down.png")
        self.frogger2 = self.frogger2.convert_alpha()
        self.frogger2 = pygame.transform.scale(self.frogger2, (48,48))

        self.frogger3 = pygame.image.load("sprites/frogger_right.png")
        self.frogger3 = self.frogger3.convert_alpha()
        self.frogger3 = pygame.transform.scale(self.frogger3, (48,48))

        self.frogger4 = pygame.image.load("sprites/jump_up.png")
        self.frogger4 = self.frogger4.convert_alpha()
        self.frogger4 = pygame.transform.scale(self.frogger4, (55,55))
        
        self.frogger5 = pygame.image.load("sprites/jump_left.png")
        self.frogger5 = self.frogger5.convert_alpha()
        self.frogger5 = pygame.transform.scale(self.frogger5, (55,55))

        self.frogger6 = pygame.image.load("sprites/jump_down.png")
        self.frogger6 = self.frogger6.convert_alpha()
        self.frogger6 = pygame.transform.scale(self.frogger6, (55,55))

        self.frogger7 = pygame.image.load("sprites/jump_right.png")
        self.frogger7 = self.frogger7.convert_alpha()
        self.frogger7 = pygame.transform.scale(self.frogger7, (55,55))
        
        self.frog = pygame.image.load("img/pepe.png")
        self.frog = self.frog.convert_alpha()
        self.frog = pygame.transform.scale(self.frog, (55,55))
        self.saved = []

    ###ADDS FROGGER TO A SAVED LIST ONE HE REACHES HIS HOME
        
    def safe(self):
        
        if self.row == 50:
            for i in range (37,614,144):
                
                if 75>=(self.col-i)>=-75:
                    self.saved.append(i)
                    return True

        return False 

    ##KEEPS FROGGER ON THE SCREEN
    
    def collides_Wall(self):
        
        if self.col < -15 or self.col > 700 or self.row > 626 or self.row < 48:
            return True
        else:
            return False

    ###CHECKS IF FROGGER COLLIDES WITH THE WATER OR ANY OBSTACLE AND RETURNS TRUE
        
    def collides_Obstacle(self,other):
        
        if (168 > self.col > 100 and self.row < 91) or (185+96 > self.col > 168+48 and self.row < 91) or (178+266 > self.col > 45+314 and self.row < 91) or (178+399 > self.col > 45+447 and self.row < 91):
            return True

        if other == truck:
            
            if self.row-2 == other.row and -125 <= (other.col - self.col)<=33:
                return True
            elif self.row-2 == other.row and -125 <= (other.col2 - self.col)<=33:
                return True

        elif other == car:
            
            if self.row-2 == other.row and -55 <= (other.col - self.col)<=33:
                return True
            elif self.row-2 == other.row and -55 <= (other.col2 - self.col)<=33:
                return True
            
        elif other == sanic:
            
            if self.row-2 == other.row and -40 <= (other.col - self.col)<=33:
                return True
            elif self.row-2 == other.row and -40 <= (other.col2 - self.col)<=33:
                return True
            
        elif other == thomas:
            
            if self.row-2 == other.row and -95 <= (other.col - self.col)<=31:
                return True
            elif self.row-2 == other.row and -95 <= (other.col2 - self.col)<=31:
                return True
            
        elif other == prius:
            
            if self.row-2 == other.row and -75 <= (other.col - self.col)<=33:
                return True
            elif self.row-2 == other.row and -75 <= (other.col2 - self.col)<=33:
                return True

        return False

    #CHECKS IF FROGGER LANDS ON ANY PLATFORMS ON THE WATER AND RETURNS TRUE
    
    def lands_on(self,other):

        if other == dew_log:
            
            if self.row-2 == other.row and -110 <= (other.col - self.col)<=33:
                return True
            
            elif self.row-2 == other.row and -110 <= (other.col2 - self.col)<=33:
                return True
            
            elif self.row-2 == other.row and -110 <= (other.col3 - self.col)<=33:
                return True
            
            else:
                return False
            
        elif other == big_log:
            
            if self.row-2 == other.row1 and -160 <= (other.col - self.col)<=33:
                return True
            elif self.row-2 == other.row1 and -160 <= (other.col2 - self.col)<=33:
                return True
            elif self.row-2 == other.row1 and -160 <= (other.col3 - self.col)<=33:
                return True        
            else:
                return False

        elif other == small_log:
            
            if self.row-2 == other.row2 and -60 <= (other.col - self.col)<=33:
                return True
            elif self.row-2 == other.row2 and -60 <= (other.col2 - self.col)<=33:
                return True
            elif self.row-2 == other.row2 and -60 <= (other.col3 - self.col)<=33:
                return True        
            else:
                return False

        elif other == doritos_log:
            
            if self.row-2 == other.row3 and -140 <= (other.col - self.col)<=33:
                return True
            elif self.row-2 == other.row3 and -140 <= (other.col2 - self.col)<=33:
                return True
            elif self.row-2 == other.row3 and -140 <= (other.col3 - self.col)<=33:
                return True        
            else:
                return False

        elif other == tiny_log:
            
            if self.row-2 == other.row4 and -40 <= (other.col - self.col)<=33:
                return True
            elif self.row-2 == other.row4 and -40 <= (other.col2 - self.col)<=33:
                return True
            elif self.row-2 == other.row4 and -40 <= (other.col3 - self.col)<=33:
                return True        
            else:
                return False

        if other == meme:
            
            if -33 <= (other.row - self.row)<=33 and -33 <= (other.col - self.col)<=33:
                return True        
            else:
                return False

#VARIABLES THAT DO NOT NEED TO BE REFRESHED IF PLAYING AGAIN

##OBJECTS FROM THE CLASSES
            
player = Frogger()

truck = Obstacle ()
car = Obstacle ()
thomas = Obstacle ()
sanic = Obstacle ()
prius = Obstacle ()

big_log = Platforms()
dew_log = Platforms()
small_log = Platforms()
doritos_log = Platforms()
tiny_log = Platforms()

meme = Meme()

##SOUND EFFECTS

explosion = AnimatedSprite("sprites/explosion_spritesheet.bmp",24)
boom = pygame.mixer.Sound("sfx/explosion.ogg")
boom1 = pygame.mixer.Sound("sfx/explosion2.ogg")
yum = pygame.mixer.Sound("sfx/yum.ogg")


timer = 0
FPS = 20
jointX = 765

R = 255
G = 255
B = 0

r = 0
g = 0
b = 0

#IMAGES

introBG = pygame.image.load("img/intro screen.png")
introBG = introBG.convert_alpha()
introBG = pygame.transform.scale(introBG, (WIDTH-30,HEIGHT-30))

wallpaper = pygame.image.load("img/Frogger Background.png")
wallpaper = wallpaper.convert_alpha()
wallpaper = pygame.transform.scale(wallpaper, (WIDTH-30,HEIGHT-30))

swamp = pygame.image.load("img/Swamp.png")
swamp = swamp.convert_alpha()
swamp = pygame.transform.scale(swamp, (WIDTH,HEIGHT))

icon = pygame.image.load("img/Frogger_icon.png")
icon = icon.convert_alpha()
icon = pygame.transform.scale(icon, (50,50))

shrek = pygame.image.load("img/shrek.png")
shrek = shrek.convert_alpha()
shrek = pygame.transform.scale(shrek, (500,400))

sBubble = pygame.image.load("img/speech_bubble.png")
sBubble = sBubble.convert_alpha()
sBubble = pygame.transform.scale(sBubble, (735,600))

cursor = pygame.image.load("img/Illuminati_triangle_eye.png")
cursor = cursor.convert_alpha()
cursor = pygame.transform.scale(cursor, (45,60))
cursor = pygame.transform.rotate(cursor,25)

gameover_wallpaper = pygame.image.load("img/gameover.jpg")
gameover_wallpaper = gameover_wallpaper.convert_alpha()
gameover_wallpaper = pygame.transform.scale(gameover_wallpaper, (WIDTH-30,HEIGHT-30))

bush = pygame.image.load("img/picture1.jpg")
bush = bush.convert_alpha()
bush = pygame.transform.scale(bush, (WIDTH,HEIGHT))

##FONTS

font =  pygame.font.Font("fonts/Digital_tech.otf",25)
font1 = pygame.font.Font("fonts/Digital_tech.otf",40)
font2 = pygame.font.SysFont("Comic Sans MS",70)
font3 = pygame.font.Font("fonts/PressStart2P.ttf",28)
font4 = pygame.font.Font("fonts/PressStart2P.ttf",18)
font5 = pygame.font.SysFont("Arial Narrow",33)
font6 = pygame.font.Font("fonts/PressStart2P.ttf",14)


sunX = 319
sunY = 50

#---------------------------------------#
#  FUNCTIONS                            #
#---------------------------------------#


def intro_screen():
    
    global angle,sunY,jointX

    #PICTURES
    
    r = randint (205,255)
    g = randint (0,50)
    b = randint (0,50)
    
    screen.fill((r,g,b))
    screen.blit(introBG,(15,15))
    
    name = font.render("Thomas George", 1, GREEN)
    playText = font1.render("PLAY", 1, BLACK)
    goText = font1.render("PLAY", 1, WHITE)
    
    quitText = font1.render("QUIT", 1, BLACK)
    exitText = font1.render("QUIT", 1, WHITE)
    
    companyTxt = font1.render("Illuminated Enterprises 2016",1,(r,g,b))
    mlg = font2.render("DANK", 1, (randint(0,255),randint(0,255),0))
    mlg = pygame.transform.rotate(mlg,25)
    screen.blit(name,(260,230))
    
    screen.blit(companyTxt,(88,30))
    screen.blit(mlg,(10,45))
    
    frogger = pygame.image.load("sprites/jump_up.png")
    frogger = frogger.convert_alpha()
    frogger = pygame.transform.scale(frogger, (100,125))
    
    screen.blit(frogger,(300,575))

    glasses = pygame.image.load("img/Mlg_glasses.png")
    glasses = glasses.convert_alpha()
    glasses = pygame.transform.scale(glasses, (60,40))
    
    screen.blit(glasses,(sunX,sunY))

    joint = pygame.image.load("img/joint.png")
    joint = joint.convert_alpha()
    joint = pygame.transform.scale(joint, (65,65))

    screen.blit(joint,(jointX,540))

    if sunY<=590:
        sunY+=4        

    if jointX>=353:
        jointX-=3
        
    mtndew = pygame.image.load("img/mountaindew.png")
    mtndew = mtndew.convert_alpha()
    mtndew = pygame.transform.scale(mtndew, (60,80))
    mtndew = pygame.transform.rotate(mtndew,angle)

    doritos = pygame.image.load("img/doritos.png")
    doritos = doritos.convert_alpha()
    doritos = pygame.transform.scale(doritos, (60,80))
    doritos = pygame.transform.rotate(doritos,-angle)
    
    screen.blit(mtndew,(150,200))
    screen.blit(doritos,(488,200))
    
    angle+=35
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    #CHECKS IF PLAY OR QUIT BUTTON IS PRESSED
    
    if 75<=mouse[0]<=250 and 625<=mouse[1]<=700:
        pygame.draw.rect (screen, darkGREEN, (80, 628, 160, 65 ))
        screen.blit(goText,(115,640))
        
        if click[0]==1:
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.stop()
            pygame.mixer.music.load("sfx/AIRHORN.mp3")             #plays an intro song
            pygame.mixer.music.play(0)
            
            global intro,getText
            intro = False
            getText = True

    else:
        
        pygame.draw.rect (screen, GREEN, (75, 625, 170, 75 ))
        screen.blit(playText,(115,640))
        
    if 455<=mouse[0]<=625 and 625<=mouse[1]<=700:
        pygame.draw.rect (screen, darkRED, (460, 628, 160,65 ))
        screen.blit(exitText,(505,640))
        
        if click[0]==1:
            pygame.quit()
            quit()

    else:
        
        pygame.draw.rect (screen, RED, (455, 625, 170, 75 ))
        screen.blit(quitText,(505,640))
    
        
    pygame.mouse.set_visible(False)
    screen.blit(cursor,(mouse[0]-35,mouse[1]-40))
    pygame.display.update()

#FUNCTION FOR SCREEN WHERE USER INPUTS THEIR NAME
    
def get_text():

    global selected
    
    screen.blit(swamp,(0,0))
    enterUser = font4.render("What do they call you on the streets?", 1, RED)
    screen.blit(enterUser,(22,80))
    
    song = font3.render("Song name?", 1, RED)
    screen.blit(song,(215,240))
    
    pygame.draw.rect (screen, BLACK, (94,150, 512, 65 ))
    pygame.draw.rect (screen, WHITE, (94,150, 512, 65 ),5)
    pygame.draw.rect (screen, BLUE, (94,410, 512, 85 ))
    pygame.draw.rect (screen, GREEN, (94,410, 512, 85 ),5)

    for event in pygame.event.get():    # check for any events
        if event.type == pygame.QUIT:       # If user clicked close
            pygame.quit()
            quit()
            
        ##RECOGNIZES KEYBOARD INPUT AND DISPLAYS LETTER ON SCREEN
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                word.append(" ")
                
            elif event.key == pygame.K_RETURN:
                new_word = ""
                
                for i in word:
                    new_word = new_word + i
                new_word = new_word.replace("space", "")

                return new_word

            ##REMOVES LAST TYPED LETTER
            
            elif event.key == pygame.K_BACKSPACE:
                
                try:
                    word.pop(-1)
                except:
                    word.append("")
                    word.pop(-1)

            elif len(word)==9:
                    word.append("")
                    word.pop(-1)
            
            else:
                key = pygame.key.name(event.key)
                
                ##ENSURES VALID LETTER OR NUMBER IS ENTERED
                
                try:
                    if 0 <= ord(key)<= 126:
                        word.append(key)
                        
                except:
                    word.append("")
                    word.pop(-1)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    ##CHECKS IF BUTTONS ARE PRESSED FOR SONG CHANGE

    if 290<=mouse[0]<=410 and 490<=mouse[1]<=610:
        pygame.draw.polygon(screen, BLUE, [[350,600],[400,550],[300,550]])

        #CYCLES THROUGH LIST OF MUSIC
        
        if click[0]==1:
            pygame.time.delay(150)
            if selected == 4:
                selected = 0
            
            else:
                selected += 1

    else:
        pygame.draw.polygon(screen, WHITE, [[350,600],[400,550],[300,550]])

    if 290<=mouse[0]<=420 and 250<=mouse[1]<=360:
        pygame.draw.polygon(screen, BLUE, [[350,300],[400,350],[300,350]])

        #CYCLES THROUGH LIST OF MUSIC
        
        if click[0]==1:
            pygame.time.delay(150)
            if selected == 0:
                selected = 4
            
            else:
                selected -= 1

    else:
        pygame.draw.polygon(screen, WHITE, [[350,300],[400,350],[300,350]])


    #CHECKS IF CONTINUE BUTTON WAS PRESSED
    
    if 240<=mouse[0]<=435 and 660<=mouse[1]<=735:
        pygame.draw.rect (screen, WHITE, (270, 675, 160, 50 ))
        done = font4.render("DONE", 1, BLUE)
        screen.blit(done,(315,690))
        
        if click[0]==1 and len(word)>0:
            pygame.mixer.music.stop()
            global getText,missionText
            getText = False
            missionText = True

    else:
        pygame.draw.rect (screen, BLUE, (265, 675, 170, 60 ))
        done = font4.render("DONE", 1, WHITE)
        screen.blit(done,(315,695))

      #DISPLAYS INPUTTED LETTERS
        
    userName = font1.render(str(word), 1, GREEN)
    screen.blit(userName,(94,162))

    #DISPLAYS SONG NAME ON SCREEN
    
    songName = font.render(str(songs[selected].replace(".mp3","")), 1, WHITE)
    screen.blit(songName,(115,440))

    #DRAWS CURSOR ON TOP OF EVERYTHING
    
    screen.blit(cursor,(mouse[0],mouse[1]))

##FUNCTION FOR INSTRUCTIONS SCREEN
    
def mission_text():
    
    global missionText,inPlay

    R = randint(0,255)
    G = randint(0,255)
    B = randint(0,255)
    
    line1 = font5.render("Hello there "+"".join(word)+" I am Xxx_Shrek_xxX", 1,(R,G,B))
    line2 = font5.render("and I will be instructing your mission", 1,(R,G,B))
    line3 = font5.render("today. You must infiltrate FaZe Clan in ", 1,(R,G,B))
    line4 = font5.render("order to defeat the Illuminati. Watch", 1,(R,G,B))
    line5 = font5.render("for the incoming trucks containing", 1,(R,G,B))
    line6 = font5.render("government secrets. The world is counting on you.", 1,(R,G,B))
    line7 = font5.render("YOLO.", 1,(R,G,B))
    
    startGame = font3.render("PRESS SPACE", 1,GREEN)
    
    screen.blit(swamp,(0,0))
    screen.blit(shrek,(220,410))
    screen.blit(sBubble,(0,0))
    
    screen.blit(line1,(100,100))
    screen.blit(line2,(150,130))
    screen.blit(line3,(145,160))
    screen.blit(line4,(150,190))
    screen.blit(line5,(155,220))
    screen.blit(line6,(88,250))
    screen.blit(line7,(325,280))
    
    screen.blit(startGame,(200,600))

##FUNCTION FOR MAIN GAME SCREEN
    
def redraw_screen():
    
    global B,G,CLR,time_width,wait
    
    B += 5
    if B == 255:
        B -=255
    G -= 5
    if G == 0:
        G +=255

    clr = (R,G,B)
    screen.fill(clr)
    screen.blit(wallpaper,(15,15))

    ##DRAWS PLATFORMS
    
    screen.blit(dew_log.dew_log, (dew_log.col,dew_log.row))
    screen.blit(dew_log.dew_log, (dew_log.col2,dew_log.row))
    screen.blit(dew_log.dew_log, (dew_log.col3,dew_log.row))
    
    screen.blit(big_log.big_log, (big_log.col,big_log.row1))
    screen.blit(big_log.big_log, (big_log.col2,big_log.row1))
    screen.blit(big_log.big_log, (big_log.col3,big_log.row1))

    screen.blit(small_log.small_log, (small_log.col,small_log.row2))
    screen.blit(small_log.small_log, (small_log.col2,small_log.row2))
    screen.blit(small_log.small_log, (small_log.col3,small_log.row2))

    screen.blit(doritos_log.doritos_log, (doritos_log.col,doritos_log.row3))
    screen.blit(doritos_log.doritos_log, (doritos_log.col2,doritos_log.row3))
    screen.blit(doritos_log.doritos_log, (doritos_log.col3,doritos_log.row3))
    
    screen.blit(tiny_log.tiny_log, (tiny_log.col,tiny_log.row4))
    screen.blit(tiny_log.tiny_log, (tiny_log.col2,tiny_log.row4))
    screen.blit(tiny_log.tiny_log, (tiny_log.col3,tiny_log.row4))

    level = font4.render("Level:" + str(lvl), 1,BLUE)
    screen.blit(level,(295,10))
    
    if int(timer)>10 and int(timer)<=15:
        CLR = ORANGE
    elif int(timer)>15:
        CLR = RED

        #DRAWS TIME BAR
        
    pygame.draw.rect (screen, CLR, (500,630, time_width-int(timer)*9, 25 ))
    pygame.draw.rect (screen, BLACK, (500,630, 180, 25 ),3)

    if CLR == RED:
        time = font6.render("Time:"+str(20-int(timer)), 1,YELLOW)

    elif CLR == ORANGE:
        time = font6.render("Time:"+str(20-int(timer)), 1,BLUE)
        
    elif CLR == GREEN:
        time = font6.render("Time:"+str(20-int(timer)), 1,BLACK)

    screen.blit(time,(505,637))

    #SPRITE DRAWING: WHENEVER ARROWKEYS ARE PRESSED, FROGGER IS DRAWN JUMPING (PLAYER.SPRITE = 5-8) AND THEN DRAWN STANDING WHEN STATIONARY (PLAYER.SPRITE = 1-4)

    if player.Sprite == 1:   
        screen.blit(player.frogger,(player.col,player.row))

    elif player.Sprite  == 2:
        screen.blit(player.frogger1,(player.col,player.row))

    elif player.Sprite  == 3:
        screen.blit(player.frogger2,(player.col,player.row))

    elif player.Sprite  == 4:
        screen.blit(player.frogger3,(player.col,player.row))


    if player.Sprite == 5:   
        screen.blit(player.frogger4,(player.col-7,player.row))
        player.Sprite = 1
        
    elif player.Sprite  == 6:
        screen.blit(player.frogger5,(player.col,player.row-7))
        player.Sprite = 2

    elif player.Sprite  == 7:
        screen.blit(player.frogger6,(player.col-7,player.row))
        player.Sprite = 3

    elif player.Sprite  == 8:
        screen.blit(player.frogger7,(player.col,player.row-7))
        player.Sprite = 4

        ##DRAWS OBSTACLES
        
    screen.blit(truck.truck,(truck.col,truck.row))
    screen.blit(truck.truck,(truck.col2,truck.row))
    
    screen.blit(car.car,(car.col,car.row))
    screen.blit(car.car,(car.col2,car.row))
    
    screen.blit(thomas.thomas,(thomas.col,thomas.row))
    screen.blit(thomas.thomas,(thomas.col2,thomas.row))
    
    screen.blit(sanic.sanic, (sanic.col,sanic.row))
    screen.blit(sanic.sanic, (sanic.col2,sanic.row))
    
    screen.blit(prius.prius, (prius.col,prius.row))
    screen.blit(prius.prius, (prius.col2,prius.row))

    if visible:
        screen.blit(meme.meme, (meme.col,meme.row))
    
    #IGNORES DRAW STATEMENT IF NO FROGS WERE SAVED YET
    
    for i in range(-1,5):
        try:
            screen.blit(player.frog, (player.saved[i],41))
        except:
            pass

    liveNum = font4.render("Lives:", 1,YELLOW)
    screen.blit(liveNum,(25,685))

    score = font4.render("Score:"+str(points), 1,YELLOW)
    screen.blit(score,(500,685))

    ##DRAWS ICONS FOR NUMBER OF LIVES LEFT
    
    for i in range(lives):
        icon_x = 135+i*55
        icon_y = 675
        screen.blit(icon, (icon_x,icon_y))

    ##DRAWS EXPLOSION
        
    if explosion.visible:
        explosion.draw(screen)
        explosion.loadNextImage()
        
        if explosion.index == 0:
            explosion.visible = False
            
    pygame.display.update()


#FUNCTION THAT DRAWS THE GAMEOVER SCREEN


def gameover_screen():
    
    global angle_eye,eye_x,eye_y,eye_Y,eye_X,sanic_x,sanic_y,angleSanic

    #DRAWS PICTURES AND TEXT
    
    playText = font1.render("PLAY", 1, BLACK)
    goText = font1.render("AGAIN", 1, WHITE)
    
    quitText = font1.render("QUIT", 1, BLACK)
    exitText = font1.render("QUIT", 1, WHITE)
    
    sanicSpeedX = randint(20,40)
    screen.fill((randint(0,255),randint(0,255),randint(0,255)))
    screen.blit(gameover_wallpaper,(15,15))
    
    g_overText = font2.render("GAME OVER...", 1,RED)
    g_overText1 = font2.render("The Illuminati Can't", 1,YELLOW)
    g_overText2 = font2.render("Be Defeated...", 1,YELLOW)
    
    eye = pygame.image.load("img/Illuminati-Logo.png")
    eye = eye.convert_alpha()
    eye = pygame.transform.scale(eye, (eye_x,eye_y))
    eye = pygame.transform.rotate(eye,angle_eye)

    sanic = pygame.image.load("img/sanic.png")
    sanic = sanic.convert_alpha()
    sanic = pygame.transform.scale(sanic, (150,215))
    sanic = pygame.transform.rotate(sanic,angleSanic)

    if sanic_x>800:
        sanic_x = -150

    angle_eye += 0.5
    angleSanic += 17

    if angleSanic == 34:
        angleSanic = -34

    if eye_X>-400:
        eye_X -= 3
        eye_Y -= 3
    else:
        eye_X -= 0
        eye_Y -= 0
        
    sanic_x += sanicSpeedX
    
    screen.blit(sanic,(sanic_x,sanic_y))
    screen.blit(sanic,(sanic_x,sanic_y+150))
    screen.blit(sanic,(sanic_x,sanic_y+300))
    screen.blit(sanic,(sanic_x,sanic_y+450))
    
    screen.blit(eye,(eye_X,eye_Y))
    screen.blit(g_overText,(100,150))
    screen.blit(g_overText1,(25,300))
    screen.blit(g_overText2,(25,450))
    
    if eye_x>1000:
        eye_x += 0
        eye_y += 0
    else:
        eye_x += 5
        eye_y += 5

    #CHECKS IF PLAY AGAIN OR QUIT BUTTON WAS PRESSED
        
    if 75<=mouse[0]<=250 and 625<=mouse[1]<=700:
        pygame.draw.rect (screen, darkGREEN, (80, 628, 160, 65 ))
        screen.blit(goText,(115,640))
        
        if click[0]==1:
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.stop()
            pygame.mixer.music.load("sfx/AIRHORN.mp3")            
            pygame.mixer.music.play(0)
            
            global gameover,get_text,playagain
            gameover = False
            getText = True
            playagain = True

    else:
        pygame.draw.rect (screen, GREEN, (75, 625, 170, 75 ))
        screen.blit(playText,(115,640))
        
    if 455<=mouse[0]<=625 and 625<=mouse[1]<=700:
        pygame.draw.rect (screen, darkRED, (460, 628, 160,65 ))
        screen.blit(exitText,(505,640))
        
        if click[0]==1:
            pygame.quit()
            quit()

    else:
        pygame.draw.rect (screen, RED, (455, 625, 170, 75 ))
        screen.blit(quitText,(505,640))
    
    pygame.mouse.set_visible(False)
    screen.blit(cursor,(mouse[0]-35,mouse[1]-40))

    pygame.display.update()

##PLAYS INTRO SONG
    
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.load("music/Dre.mp3")             
pygame.mixer.music.play(-1)

#---------------------------------------#
#  MAIN LOOP                            #
#---------------------------------------#

while True:

    ##BOOLEANS THAT ALLOW THE USER TO TRANSITION FROM ONE SCREEN TO THE NEXT
    
    intro = True
    gameover = False
    getText = False
    inPlay = False
    missionText = False
    overlap = False
    respawn = False
    playagain = False
    score = False
    visible = True

    ##LISTS
    
    word = []
    player.saved  = []

    ##GAMEOVER SCREEN SFX AND PICTURE MOVEMENTS
    
    angle = 0
    lives = 3
    points = 0
    selected = 0
    delay = 75
    CLR = GREEN
    time_width = 180
    frogs_saved = 0
    
    lvl = 1
    point = 0
    wait = 0
    angle_eye = 0
    eye_x,eye_y = 5,5
    angleSanic = 0
    eye_X, eye_Y = 280,550
    sanic_x,sanic_y = 50,20

    ##INTRO SCREEN LOOP

    
    while intro and not playagain:
        
        for event in pygame.event.get():    # check for any events
            if event.type == pygame.QUIT:       # If user clicked close
                pygame.quit()
                quit()

        intro_screen()
        pygame.time.delay(10)

    #LOOP FOR SCREEN THAT GETS USERNAME
        
    while getText:
        get_text()
        pygame.display.update()
        pygame.time.delay(10)

    #PLAYS THE INSTRUCTIONS AUDIO
        
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.load("sfx/speech.mp3")             
    pygame.mixer.music.play(0)

    ##LOOP FOR INSTRUCTIONS SCREEN
    
    while missionText:
        
        for event in pygame.event.get():    # check for any events
            if event.type == pygame.QUIT:       # If user clicked close
                pygame.quit()
                quit()

                #CHECKS IF SPACE WAS PRESSED TO ADVANCE
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.stop()
                    missionText = False
                    inPlay = True

        mission_text()       
        pygame.display.update()
        pygame.time.delay(10)

######PLAYS MAIN GAME MUSIC FROM THE LIST
        
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.load('music/' + songs[selected])             
    pygame.mixer.music.play(-1)

#####MAIN GAME LOOP
    
    while inPlay:
        
        timer += delay/1000
        for event in pygame.event.get():    # check for any events
            if event.type == pygame.QUIT:       # If user clicked close
                pygame.quit()
                quit()
                
            if (event.type == pygame.KEYDOWN):

                #DETECTS WHICH ARROW KEYS WERE PRESSED AND ASSIGNS THE SPRITE NUMBER
                #MOVES FROGGER BACK IF HE COLLIDES WITH A WALL TO KEEP HIM ON SCREEN
                
                if (event.key == pygame.K_LEFT):
                    player.Sprite = 6
                    player.col -= 48
                    
                    if player.collides_Wall():
                        player.col += 48

                elif (event.key == pygame.K_RIGHT):
                    player.Sprite = 8
                    player.col += 48
                    
                    if player.collides_Wall():
                        player.col -= 48

                elif (event.key == pygame.K_UP):
                    player.Sprite = 5
                    player.row-=48
                    points+=10
                    point += 10
                    
                    if player.collides_Wall():
                        player.row += 48
                        points-=10
                        point -=10

                elif (event.key == pygame.K_DOWN):
                    player.Sprite = 7
                    player.row += 48
                    points-=10
                    point -= 10
                    
                    if player.collides_Wall():
                        player.row -= 48
                        points+=10
                        point+=10


          #CALLS FUNCTIONS TO ALLOW PLATFORMS AND OBSTACLES TO MOVE ON SCREEN          
        truck.truck_drive()
        car.car_drive()
        thomas.thomas_drive()
        sanic.sanic_run()
        prius.prius_drive()
        
        big_log.big_log_float()
        dew_log.dew_log_float()
        small_log.small_log_float()
        doritos_log.doritos_log_float()
        tiny_log.tiny_log_float()

        meme.fly()
        
        ##ANIMATION TIMER

        clock.tick(FPS)
            
        #CHECKS IF FROGGER COLLIDED WITH AN OBSTACLE AND KILLS HIM IF TRUE
        
        if player.collides_Obstacle(truck) or player.collides_Obstacle(car) or player.collides_Obstacle(sanic) or player.collides_Obstacle(thomas) or player.collides_Obstacle(prius):
            pygame.time.delay(69)
            respawn = True

        ###CHECKS IF USER COLLIDES WITH EVERY PLATFORM AND KILLS FROGGER IF FALSE
            
        elif player.lands_on(dew_log):
            player.col+=dew_log.dew_log_speed
            if player.collides_Wall():
                respawn = True
                
        elif player.lands_on(dew_log) == False and player.row==290:
            respawn = True
            
        elif player.lands_on(big_log):
            player.col-=big_log.big_log_speed
            if player.collides_Wall():
                respawn = True
        
        elif player.lands_on(big_log) == False and player.row==242:
            respawn = True

        elif player.lands_on(small_log):
            player.col+=small_log.small_log_speed
            if player.collides_Wall():
                respawn = True
        
        elif player.lands_on(small_log) == False and player.row==194:
            respawn = True
            
        elif player.lands_on(doritos_log):
            player.col-=doritos_log.doritos_log_speed
            if player.collides_Wall():
                respawn = True
        
        elif player.lands_on(doritos_log) == False and player.row==146:
            respawn = True

        elif player.lands_on(tiny_log):
            player.col+=tiny_log.tiny_log_speed

            if player.collides_Wall():
                respawn = True
        
        elif player.lands_on(tiny_log) == False and player.row==98:
            respawn = True

        if player.lands_on(meme) and visible:

            yum.play()
            point+=500
            points+=500
            visible = False
            
        ##KILLS FROGGER IF TIME RUNS OUT
            
        elif int(timer) == 20:
            respawn = True

        #KILLS FROGGER IF HE STRIES TO JUMP INTO AN ALREADY-OCCUPPIED HOME
            
        elif len(player.saved)-1 == len(set(player.saved)):
            player.saved.pop(-1)
            explosion.spawn(player.col,50)
            
            overlap = True
            respawn = True


        ##RESETS TIMER AND FROGGERS POSITION AND TAKES AWAY A LIFE
            
        if respawn:
            
            timer = 0
            CLR = GREEN
            
            if overlap == False:
                explosion.spawn(player.col,player.row)

            else:
                overlap = False
                
            boom.play()
            player.col,player.row = 325,626
            lives -= 1
            
            player.Sprite = 1
            pygame.time.delay(50)
            respawn = False

        ##IF FROGGER WAS SAVED HE IS REDRAWN IN HIS STARTING POSITION AND TIME IS RESET WITH NO LIVES LOST
            
        elif player.safe():
            
            points+= (20 - int(timer))*10
            point += (20 - int(timer))*10
            timer = 0
            points += 50
            
            CLR = GREEN
            boom1.play()

            player.col,player.row = 325,626
            player.Sprite = 1

            visible = True
            
            pygame.time.delay(50)


        ##SENDS USER TO GAMEOVER SCREEN ONCE ALL THE LIVES ARE GONE
            
        if lives == -1:
            inPlay = False
            score = True

            #1-UP
            
        elif point>=2500:
            lives+=1
            point = 0
            
        #NEW LEVEL
            
        if len(player.saved) == 5:
            
            points+=1000
            point +=1000
            delay-=5
            player.saved = []
            lvl += 1

        redraw_screen()
        pygame.time.delay(delay)

        #DISPLAYS SCORE AND NAME AT THE END FOR A FEW SECONDS
        
        if score:

             #LOADS SOUND EFFECT
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.load("sfx/tactical nuke.mp3")             
            pygame.mixer.music.play(0)
            screen.blit(bush,(0,0))

            #FINAL SCORE AND NAME DECLARED AND DISPLAYED
            
            score_final = font1.render("Nice Try"+str(word), 1,BLUE)
            score_final1 = font1.render("Your score was:"+str(points)+", ye scrub",1,RED)
            
            screen.blit(score_final,(95,150))
            screen.blit(score_final1,(100,600))
            
            pygame.display.update()
            pygame.time.delay(9000)

            #STARTS GAMEOVER SONG
            
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.load("music/The Official Illuminati Theme Song.mp3")             
            pygame.mixer.music.play(-1)
            
            gameover = True
            
    #DRAWING GAMEOVER SCREEN FUNCTION
        
    while gameover:
        
        for event in pygame.event.get():    # check for any events
            if event.type == pygame.QUIT:       # If user clicked close
                pygame.quit()
                quit()
                
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        gameover_screen()
        
        pygame.time.delay(5)

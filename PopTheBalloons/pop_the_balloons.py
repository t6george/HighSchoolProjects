import pygame
pygame.init()

from math import sqrt                   
from random import randint,choice
import time

HEIGHT = 600
WIDTH  = 800
game_window=pygame.display.set_mode((WIDTH,HEIGHT))

WHITE = (255,255,255)                   
BLACK = (  0,  0,  0)                   
outline=0
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
ORANGE=(255,157,0)
PINK=(255,61,249)
YELLOW=(255,238,0)
CLR=[RED,GREEN,BLUE,ORANGE,PINK,YELLOW]
dark_green=(0,195,0)
dark_red=(195,0,0)

text_X = 5                              
text_Y = 0
text_X2 = 675                              
text_Y2 = 0
counter=0
message=counter
size=25

font = pygame.font.SysFont("Arial Black",size)
font2 = pygame.font.SysFont("Arial Black",size-3)
font3 = pygame.font.SysFont("Digital tech",size+20)

clock=0
sanicx=0
sanicy=240
sanicspeed=65
angle=0

#---------------------------------------#
# function that calculates distance     #
# between two points in coordinate system
#---------------------------------------#
def distance(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)    

#---------------------------------------#
# function that redraws all objects     #
#---------------------------------------#
def redraw_game_window():
    game_window.blit(background,(backgroundx,backgroundy))
    score=int((counter/20)*100)
    
    for i in range(20):
        if balloonvisible[i]==True:
            pygame.draw.circle(game_window, balloonCLR[i], (balloonX[i], balloonY[i]), balloonR[i], outline)
            
    game_window.blit(back1,(backgroundx,backgroundy))
    game_window.blit(back1,(660,backgroundy))
    mouse=pygame.mouse.get_pos()
    game_window.blit(cursor,(mouse[0],mouse[1]))
    text = font.render("Score: "+str(counter), 1, RED)
    game_window.blit(text,(text_X,text_Y))
    text2 = font2.render("Time: "+str(clock),1,RED)
    game_window.blit(text2,(text_X2,text_Y2))
    
    if True not in balloonvisible:
        if counter>15:
            pygame.mixer.music.load("sfx/sanic.mp3")
            pygame.mixer.music.play(-1)
            pygame.mixer.find_channel(1)
            
            for i in range (0,256,5):
                while True:
                    pygame.time.delay(50)
                    R,G,B=randint(0,255),randint(0,255),randint(0,255)

                    pygame.draw.rect (game_window, (R,G,B), (0, 50, 800, 550 ))
                    pygame.draw.rect (game_window, (B,R,G), (0, 50, 800, 550 ),8)
                    
                    global sanicx,sannicy,sanicspeed,angle
                    
                    sanic = pygame.image.load("img/sanic.png")
                    sanic = sanic.convert_alpha()
                    sanic = pygame.transform.scale(sanic, (150,215))
                    
                    if angle >= 17:
                        angle = -34
                    angle=angle+17
                    
                    sanic = pygame.transform.rotate(sanic,angle)
                    game_window.blit(sanic,(sanicx,sanicy))
                    sanicx+=sanicspeed

                    if sanicx>800:
                        sanicx=0
                        
                    gameover = font3.render("Ur a Quickscoper", 1, (i,255-i,i))
                    game_window.blit(gameover,(235,150))
                    scorefinal=font2.render(str(score)+"% of the balloons were popped! R u in FaZe?", 1, (i,255-i,i))
                    game_window.blit(scorefinal,(50,500))
                    pygame.display.update()

    
        pygame.mixer.music.load("sfx/2SED4AIRHORN.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.find_channel(1)
        
        for i in range (0,256,5):
            pygame.time.delay(100)
            pygame.draw.rect (game_window, (i,i,255-i), (0, 50, 800, 550 ))
            pygame.draw.rect (game_window, (255-i,i,i), (0, 50, 800, 550 ),8)
            
            gameover = font3.render("GAME OVER", 1, (i,255-i,i))
            game_window.blit(gameover,(295,150))
            scorefinal=font2.render(str(score)+"% of the balloons were popped!", 1, (i,255-i,i))
            
            game_window.blit(scorefinal,(50,500))
            game_window.blit(back2,(50,220))
            pygame.display.update()
            
            if i==255:
                break
            
        for i in range (255,0,-5):
            pygame.time.delay(100)
            pygame.draw.rect (game_window, (i,i,255-i), (0, 50, 800, 550 ))
            pygame.draw.rect (game_window, (255-i,i,i), (0, 50, 800, 550 ),8)
            gameover = font3.render("GAME OVER", 1, (i,255-i,i))
            game_window.blit(gameover,(295,150))
            scorefinal=font2.render(str(score)+"% of the balloons were popped!", 1, (i,255-i,i))
            
            game_window.blit(scorefinal,(50,500))
            game_window.blit(back2,(50,220))
            pygame.display.update()
            
            if i==0:
                break
            
    pygame.display.update()
    
       

#---------------------------------------#
exit_flag = False                       

balloonR = [0]*20                       
balloonX = [0]*20                       
balloonY = [0]*20                       
balloonSPEED = [0]*20
balloonCLR =[(0,0,0)]*20
balloonvisible = [True]*20

background = pygame.image.load("img/wallpaper.jpg")
background = background.convert_alpha()
background = pygame.transform.scale(background, (WIDTH,HEIGHT))

back1 = pygame.image.load("img/Black-Honeycomb-Pattern.jpg")
back1 = back1.convert_alpha()
back1 = pygame.transform.scale(back1, (140,40))

back2 = pygame.image.load("img/maxresdefault.jpg")
back2 = back2.convert_alpha()
back2 = pygame.transform.scale(back2, (700,260))

cursor = pygame.image.load("img/hitmarker.jpg")
cursor = cursor.convert_alpha()
cursor = pygame.transform.scale(cursor, (25,25))

pygame.mouse.set_visible(False)
backgroundx=0
backgroundy=0
sanicx=0
sanicy=220

for i in range(20):
    balloonX[i] = randint(0, WIDTH)     
    balloonY[i] = randint(HEIGHT/2, HEIGHT)
    balloonR[i] = randint(25,40)
    balloonSPEED[i] = randint(2,4)
    balloonCLR[i]=choice(CLR)

        
while not exit_flag:
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:   
            exit_flag = True
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mixer.music.load("sfx/intervention 420.mp3")
            pygame.mixer.music.play(0)
            pygame.mixer.find_channel(2)

            for i in range(20):
                if balloonvisible[i]==True:
                    mouse=pygame.mouse.get_pos()
                    
                    if distance (mouse[0], mouse[1], balloonX[i], balloonY[i])< balloonR[i]:
                        
                        pygame.mixer.music.load("sfx/wow.mp3")
                        pygame.mixer.music.play(0)
                        pygame.mixer.find_channel(3)
                        
                        balloonvisible[i] = False
                        counter=counter+1
                        print (counter)

                 
    for i in range(20):
        balloonY[i] = balloonY[i] - balloonSPEED[i]
        if (balloonY[i]+balloonR[i])<0:
               balloonvisible[i]=False

    while True in balloonvisible:
        clock = (int(pygame.time.get_ticks()/1000))
        break

    redraw_game_window()
    pygame.time.delay(50)
    
pygame.quit()                          

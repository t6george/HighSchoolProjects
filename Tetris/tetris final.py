#########################################
# Programmer: Thomas George
# Date: 21/11/2015
# File Name: tetris_template3.py
# Description: This program is a template for a Tetris game.
#########################################
from tetris_classes3 import *
from random import randint
import pygame
pygame.init()

#############Display Parameters#################
HEIGHT = 600
WIDTH  = 800
GRIDSIZE = HEIGHT//24
screen=pygame.display.set_mode((WIDTH,HEIGHT))
GREY = (192,192,192)
ORANGE = (255,180,0)
darkGREEN = (0,150,0)
darkRED = (150,0,0)
tetraDouble = False
global score
global clock
intro = True
inPlay = False
gameover = False
playAgain = False
darkGREEN = (0,150,0)
angle = 0

##############Grid Parameters###################
#---------------------------------------#
COLUMNS = 14                            #
ROWS = 22                               # 
LEFT = 9                                # 
RIGHT = LEFT + COLUMNS                  # 
MIDDLE = LEFT + COLUMNS//2              #
TOP = 1                                 #
BOTTOM = TOP + ROWS                     #
#---------------------------------------#

#############Images and Fonts#####################
intro_wallpaper = pygame.image.load("img/introWallpaper.jpg")
intro_wallpaper = intro_wallpaper.convert_alpha()
intro_wallpaper = pygame.transform.scale(intro_wallpaper, (WIDTH-30,HEIGHT-30))

cursor = pygame.image.load("img/cursor.jpg")
cursor = cursor.convert_alpha()
cursor = pygame.transform.scale(cursor, (45,60))
cursor = pygame.transform.rotate(cursor,25)

wallpaper = pygame.image.load("img/wallpaper.png")
wallpaper = wallpaper.convert_alpha()
wallpaper = pygame.transform.scale(wallpaper, (WIDTH-30,HEIGHT-30))

tetra_wallpaper = pygame.image.load("img/tetraWallpaper.jpg")
tetra_wallpaper = tetra_wallpaper.convert_alpha()
tetra_wallpaper = pygame.transform.scale(tetra_wallpaper, (350,575))

spikes = pygame.image.load("img/spikes.png")
spikes = spikes.convert_alpha()
spikes = pygame.transform.scale(spikes, (350,25))

troll = pygame.image.load("img/troll.png")
troll = troll.convert_alpha()
troll = pygame.transform.scale(troll, (300,300))

upcomingPiece = pygame.image.load("img/next.png")
upcomingPiece = upcomingPiece.convert_alpha()
upcomingPiece = pygame.transform.scale(upcomingPiece, (150,100))

font = pygame.font.SysFont("Comic Sans MS",35)
font1 = pygame.font.SysFont("Wide Latin",100)
font2 = pygame.font.SysFont("Comic Sans MS",25)
font3 = pygame.font.SysFont("Cooper Black",50)

#---------------------------------------#
#   functions                           #
#-------------tetr--------------------------#

###########Intro Screen Function including button detection and colorful effects############################
def intro_screen ():
    screen.fill(((randint(100,255)),(randint(100,255)),(randint(0,50))))
    screen.blit(intro_wallpaper,(15,15))
    playText = font.render("PLAY", 1, BLACK)
    goText = font.render("PLAY", 1, WHITE)
    quitText = font.render("QUIT", 1, BLACK)
    exitText = font.render("QUIT", 1, WHITE)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    title = font1.render("TETRIS", 1, ((randint(0,255)),(randint(0,255)),(randint(0,255))))
    screen.blit(title,(35,100))
    if 75<=mouse[0]<=250 and 450<=mouse[1]<=515:
        pygame.draw.rect (screen, darkGREEN, (80, 455, 160, 65 ))
        screen.blit(goText,(115,460))
        if click[0]==1:                                   ###Check if button is pressed
            screen.blit(troll,(247,125))
            pygame.mixer.music.stop()
            pygame.mixer.music.load("music/DEDOTADED WAM.mp3")             #play song
            pygame.mixer.music.play(0)
            global intro      ####boolean expression that causes the main loop to go to the redraw screen loop and enter the game
            intro = False

    else:
        pygame.draw.rect (screen, GREEN, (75, 450, 170, 75 ))
        screen.blit(playText,(115,460))
        
    if 555<=mouse[0]<=725 and 450<=mouse[1]<=515:
        pygame.draw.rect (screen, darkRED, (560, 455, 160, 65 ))        ###Check if button is pressed
        screen.blit(exitText,(587,460))
        if click[0]==1:
            pygame.quit()
            quit()

    else:
        pygame.draw.rect (screen, RED, (555, 450, 170, 75 ))
        screen.blit(quitText,(587,460))
    
        
    pygame.mouse.set_visible(False)
    screen.blit(cursor,(mouse[0],mouse[1]))
    pygame.display.update()

############################Redraw Screen Function################################
def redraw_screen():
    
    screen.fill(((randint(0,255)),(randint(0,255)),(randint(0,255))))
    screen.blit(wallpaper,(15,15))
    screen.blit(tetra_wallpaper,(225,0))
    screen.blit(spikes,(225,0))
    screen.blit(upcomingPiece,(38,400))
    pygame.draw.rect(screen,(((randint(0,255)),(randint(0,255)),(randint(0,255)))),(38,400,150,100),5)
    score_text = font.render("Score: "+str(score), 1, GREEN)        #######Score and time are drawn
    timer = font.render("Time: "+str(int(clock)), 1, YELLOW)
    next_text = font.render("Next:", 1, ((randint(0,255)),(randint(0,255)),(randint(0,255))))
    screen.blit(score_text,(25,100))
    screen.blit(timer,(610,100))
    screen.blit(next_text,(63,330))
    nextTetra.draw(screen, GRIDSIZE)
    shadow.draw(screen,GRIDSIZE)
    
    for x in range (225,GRIDSIZE*14+226,GRIDSIZE):                      ###grid is drawn
        pygame.draw.line (screen,ORANGE,(x,25),(x,GRIDSIZE*22+25),1)
    for y in range (25,GRIDSIZE*23+26,GRIDSIZE):
        pygame.draw.line(screen,ORANGE,(225,y),(GRIDSIZE*14+226,y),1)
        
    tetra.draw(screen, GRIDSIZE)
    obstacle.draw(screen,GRIDSIZE)
    pygame.display.update()

##########Game Over Function with colorful effects and buttons to quit or play again#####################
    
def gameover_screen():
    global angle
    global playAgain
    screen.fill(BLUE)
    pygame.draw.rect (screen, (YELLOW), (0,0, WIDTH,HEIGHT),25)
    playText = font2.render("PLAY AGAIN", 1, BLACK)
    goText = font2.render("PLAYAGAIN", 1, WHITE)
    quitText = font.render("QUIT", 1, BLACK)
    exitText = font.render("QUIT", 1, WHITE)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    gameoverTxt = pygame.image.load("img/rip.jpg")
    gameoverTxt = gameoverTxt.convert_alpha()
    gameoverTxt = pygame.transform.scale(gameoverTxt, (400,400))
    gameoverTxt = pygame.transform.rotate(gameoverTxt,angle)
    screen.blit(gameoverTxt,(150,50))
    angle += 0.5
    timer = font3.render("Time: "+str(int(clock)), 1, YELLOW)
    score_text = font3.render("Score: "+str(score), 1, GREEN)
    screen.blit(score_text,(25,100))
    screen.blit(timer,(555,100))
    
    if 75<=mouse[0]<=250 and 450<=mouse[1]<=515:
        pygame.draw.rect (screen, darkGREEN, (80, 455, 160, 65 ))     ###Check if button is pressed
        screen.blit(goText,(85,468))
        if click[0]==1:
            global gameover       ##boolean expressions that cause the game to return to the redraw loop and play again
            global inPlay
            gameover = False
            playAgain = True
            inPlay = True

    else:
        pygame.draw.rect (screen, GREEN, (75, 450, 170, 75 ))
        screen.blit(playText,(85,468))
        
    if 555<=mouse[0]<=725 and 450<=mouse[1]<=515:
        pygame.draw.rect (screen, darkRED, (560, 455, 160, 65 ))
        screen.blit(exitText,(587,460))
        if click[0]==1:        ###Check if button is pressed
            pygame.quit()
            quit()

    else:
        pygame.draw.rect (screen, RED, (555, 450, 170, 75 ))
        screen.blit(quitText,(587,460))
    
        
    pygame.mouse.set_visible(False)
    screen.blit(cursor,(mouse[0],mouse[1]))
    pygame.display.update()
#---------------------------------------#
#   main program                        #
#---------------------------------------#    
while True:         ###Play again loop
    score = 0
    clock = 0
    delay = 150
    sfx = pygame.mixer.Sound("sfx/remove_row.ogg")
    pygame.mixer.music.load("music/Tupac- Ambitionz Az a Ridah.mp3")             #plays an intro song
    pygame.mixer.music.play(-1)
    while intro:        ####intro screen loop
        for event in pygame.event.get():    # check for any events
            if event.type == pygame.QUIT:       # If user clicked close
                pygame.quit()
                quit()
        intro_screen()
        pygame.time.delay(50)
        
    shapeNo = randint(1,7)               #Generate objects
    next_shapeNo = randint(1,7)
    tetra = Shape(MIDDLE,TOP,shapeNo)
    nextTetra = Shape(LEFT-5,BOTTOM-5,next_shapeNo)
    shadow = Shape (MIDDLE,BOTTOM-1,shapeNo)
    bottom = Floor(LEFT,BOTTOM,COLUMNS)
    topWall = Floor(LEFT,TOP,COLUMNS)
    leftWall = Wall(LEFT-1, TOP, ROWS)
    rightWall = Wall(RIGHT, TOP, ROWS)
    obstacle = Obstacles (LEFT,BOTTOM)
    if not playAgain:
        pygame.time.delay(5500)
    inPlay = True
    pygame.mixer.music.stop()
    (pygame.mixer.music.load("music/Tetris Airhorn Song.mp3"))             #plays an intro song
    pygame.mixer.music.play(-1)
    
###########################################MAIN GAME##################
    while inPlay:
        obstacle_rows = []
        obstacle_cols = []
        for block in obstacle.blocks:
            obstacle_rows.append(block.row)
        for block in obstacle.blocks:
            obstacle_cols.append(block.col)
            
        shadow_rows = []
        shadow_cols = []
        for block in shadow.blocks:
            shadow_rows.append(block.row)
        for block in shadow.blocks:
            shadow_cols.append(block.col)
            
        tetra_rows = []
        tetra_cols = []
        for block in tetra.blocks:
            tetra_rows.append(tetra.row)
        for block in tetra.blocks:
            tetra_cols.append(tetra.col)
            
        if len(obstacle_rows) >= 4:
            for i in range (len(obstacle_rows)):     ####Causes shadow to be drawn only right above obstacles
                for j in range(4):
                    if shadow_cols[j] == obstacle_cols[i]:
                        if tetra_rows[j] < obstacle_rows[i] and shadow_rows[j] > obstacle_rows[i]:
                            shadow.row = tetra.row
                        while not (shadow.collides(bottom) or shadow.collides(obstacle)):
                            shadow.move_down()
                        while shadow.collides(bottom) or shadow.collides(obstacle):
                            shadow.move_up()

        shadow.render_shadow()      ###Draws shadow

        while not (shadow.collides(bottom) or shadow.collides(obstacle)):  # Moves the shadow while the tetra is going dowm
            shadow.move_down()
        while shadow.collides(bottom) or shadow.collides(obstacle):
            shadow.move_up()

        tetra.move_down()

        if tetra.collides(bottom)or tetra.collides(obstacle):
            tetra.move_up()
            obstacle.append(tetra)
            shapeNo=next_shapeNo
            shadow = Shape(MIDDLE,BOTTOM-1,shapeNo)
            shadow.render_shadow()
            fullRows = obstacle.findFullRows(TOP, BOTTOM, COLUMNS)
            obstacle.removeFullRows(fullRows)
            if len(fullRows)==1:                ### Determines the score
                sfx.play()
                score+=100
                delay-=15
                tetraDouble = False
            elif len(fullRows)==2:
                sfx.play()
                score+=200
                delay-=30
                tetraDouble = False
            elif len(fullRows)==3:
                sfx.play()
                score+=300
                delay-=45
                tetraDouble = False
            elif len(fullRows)==4 and tetra == False:
                sfx.play()
                score+=800
                delay-=60
                tetraDouble = True
            elif len(fullRows)==4 and tetra == True:
                sfx.play()
                score+=1200
                delay-=60
                tetraDouble = False
            next_shapeNo = randint(1,7)     ##Generates new shape
            tetra = Shape(MIDDLE,TOP,shapeNo)
            nextTetra = Shape(LEFT-5,BOTTOM-5,next_shapeNo)
            
        if obstacle.collides(topWall):
            pygame.mixer.music.stop() ###boolean that brings while loop to leave the redraw screen loop and enter gameover loop
            inPlay = False

########BUTTON CONTROL
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:         
                pygame.quit()
                quit()            

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:

                    tetra.rotate_clkwise()
                    shadow.rotate_shadow(tetra)
                    if tetra.collides(leftWall) or tetra.collides(rightWall) or tetra.collides(bottom) or tetra.collides(obstacle):
                        tetra.rotate_cntclkwise()
                        shadow.rotate_cntclkwise()
                                      
                if event.key == pygame.K_LEFT:
                    tetra.move_left()
                    shadow.move_left()
                    if tetra.collides(leftWall) or tetra.collides(obstacle):
                        tetra.move_right()
                        shadow.move_right()
                                      
                if event.key == pygame.K_RIGHT:
                    tetra.move_right()
                    shadow.move_right()        
                    if tetra.collides(rightWall)or tetra.collides(obstacle):
                        tetra.move_left()
                        shadow.move_left()
                                      
                if event.key == pygame.K_DOWN:
                    tetra.move_down()
                    if tetra.collides(bottom)or tetra.collides(obstacle):
                        tetra.move_up()
                        obstacle.append(tetra)
                        shapeNo = next_shapeNo
                        fullRows = obstacle.findFullRows(TOP, BOTTOM, COLUMNS) # finds the full rows and removes their blocks from the obstacles                
                            
                        if len(fullRows)==1: #Determines score
                            sfx.play()
                            score+=100
                            delay-=15
                            tetraDouble = False
                        elif len(fullRows)==2:
                            sfx.play()
                            score+=200
                            delay-=30
                            tetraDouble = False
                        elif len(fullRows)==3:
                            sfx.play()
                            score+=300
                            delay-=45
                            tetraDouble = False
                        elif len(fullRows)==4 and tetra == False:
                            sfx.play()
                            score+=800
                            delay-=60
                            tetraDouble = True
                        elif len(fullRows)==4 and tetra == True:
                            sfx.play()
                            score+=1200
                            delay-=60
                            tetraDouble = False
                            
                        obstacle.removeFullRows(fullRows)
                        next_shapeNo = randint(1,7)     
                        tetra = Shape(MIDDLE,TOP,shapeNo)
                        nextTetra = Shape(LEFT-5,BOTTOM-5,next_shapeNo)
                
                if event.key == pygame.K_SPACE:
                    fall = True
                    while fall:
                        tetra.move_down()
                        if tetra.collides(bottom)or tetra.collides(obstacle):
                            tetra.move_up()
                            obstacle.append(tetra)
                            fullRows = obstacle.findFullRows(TOP, BOTTOM, COLUMNS) 

                            if len(fullRows)==1:      ##Determines score
                                sfx.play()
                                score+=100
                                delay-=15
                                tetraDouble = False
                            elif len(fullRows)==2:
                                sfx.play()
                                score+=200
                                delay-=30
                                tetraDouble = False
                            elif len(fullRows)==3:
                                sfx.play()
                                score+=300
                                delay-=45
                                tetraDouble = False
                            elif len(fullRows)==4 and tetra == False:
                                sfx.play()
                                score+=800
                                delay-=60
                                tetraDouble = True
                            elif len(fullRows)==4 and tetra == True:
                                sfx.play()
                                score+=1200
                                delay-=60
                                tetraDouble = False
                            shapeNo = next_shapeNo                     
                            obstacle.removeFullRows(fullRows)
                            shadow = Shape (MIDDLE,BOTTOM-1,shapeNo)
                            while not (shadow.collides(bottom) or shadow.collides(obstacle)):
                                shadow.move_down()
                            shadow.render_shadow()
                            next_shapeNo = randint(1,7)     
                            tetra = Shape(MIDDLE,TOP,shapeNo)
                            nextTetra = Shape(LEFT-5,BOTTOM-5,next_shapeNo) # finds the full rows and removes their blocks from the obstacles 
                            while shadow.collides(bottom) or shadow.collides(obstacle):
                                shadow.move_up()
                                

                            fall = False                  

        clock += delay/1000    #In game timer
        redraw_screen()
        pygame.time.delay(delay)

    gameover = True
    pygame.mixer.music.load("music/RIP.mp3")             #plays an intro song
    pygame.mixer.music.play(-1)
    while gameover:
        for event in pygame.event.get():    # check for any events
            if event.type == pygame.QUIT:       # If user clicked close
                pygame.quit()
                quit()
                
        gameover_screen()
        pygame.time.delay(10)
    

    
    

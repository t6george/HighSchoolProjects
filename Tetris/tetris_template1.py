#########################################
# Programmer: Thomas George
# Date: December 8, 2015
# File Name: tetris_template1.py
# Description: This program is a template for a Tetris game.
#########################################
from tetris_classes1 import *
from random import randint
import pygame
pygame.init()

HEIGHT = 600
WIDTH  = 800
GRIDSIZE = HEIGHT//24
horizshift = (WIDTH-GRIDSIZE)//2
screen=pygame.display.set_mode((WIDTH,HEIGHT))

#---------------------------------------#
#   functions                           #
#---------------------------------------#
def intro_screen():
    if intro==True:
        screen.fill(ORANGE)
        print("why")
    

def redraw_screen():
    screen.fill(BLACK)
    draw_grid()
    tetra.draw(screen, GRIDSIZE)
    pygame.display.update() 


def draw_grid():
    """ Draw horisontal and vertical lines on the entire game window.
        Space between the lines is GRIDSIZE.
    """
    for i in range (25,GRIDSIZE*14+26,GRIDSIZE):
        pygame.draw.line (screen,RED,(i,25),(i,GRIDSIZE*22+25),1)
    for j in range (25,GRIDSIZE*23+26,GRIDSIZE):
        pygame.draw.line(screen,RED,(25,j),(GRIDSIZE*14+25,j),1)
            
#---------------------------------------#
#   main program                        #
#---------------------------------------#
intro=True
intro_screen()
shapeNo = randint(1,7)      
tetra = Shape(1,1,shapeNo)
inPlay = True
while inPlay:
    #tetra.row+=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:         
            inPlay = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                tetra.rot = (tetra.rot + 1)%4
                tetra.move_up()
                #tetra.rotate()
            if event.key == pygame.K_LEFT:
                tetra.move_left()
            if event.key == pygame.K_RIGHT:
                tetra.move_right()
            if event.key == pygame.K_DOWN:
                tetra.move_down()                
            if event.key == pygame.K_SPACE:
                tetra.clr = tetra.clr + 1   # change the shape/clr by adding one line
                if tetra.clr > 7:           # after the seventh shape start from the beginning
                    tetra.clr = 1
               
                tetra.rotate()              # after chaging the shape/clr the tetra must be rotated and updated: 

# update the screen
    redraw_screen()
    pygame.time.delay(30)
    
pygame.quit()
    
    

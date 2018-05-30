###########################################################
# Programmer: Thomas George
# Date: December 8, 2015
# File Name: tetris_template2.py
# Description: This program is a template for a Tetris game.
############################################################
from tetris_classes2 import *
from random import randint
import pygame
pygame.init()

HEIGHT = 600
WIDTH  = 800
GRIDSIZE = HEIGHT//24
screen=pygame.display.set_mode((WIDTH,HEIGHT))

#---------------------------------------#
COLUMNS = 14                            #
ROWS = 22                               #
LEFT = 9                                #
TOP = 1                                 #
MIDDLE = LEFT + COLUMNS/2               # 
RIGHT = LEFT + COLUMNS                  #
BOTTOM = TOP + ROWS                     #
#---------------------------------------#

#---------------------------------------#
#   functions                           #
#---------------------------------------#
def redraw_screen():               
    screen.fill(BLACK)
    tetra.draw(screen, GRIDSIZE)
    leftWall.draw(screen,GRIDSIZE)
    rightWall.draw(screen,GRIDSIZE)
    bottom.draw(screen, GRIDSIZE)
    pygame.display.update()
    
def draw_grid():
    """ Draw horisontal and vertical lines on the entire game window.
        Space between the lines is GRIDSIZE.
    """

#---------------------------------------#
#   main program                        #
#---------------------------------------#    
shapeNo = randint(1,7)
tetra = Shape(MIDDLE,TOP,shapeNo)      
bottom = Floor(LEFT,BOTTOM,COLUMNS)
leftWall = Wall((LEFT-1),TOP,ROWS)
rightWall = Wall(RIGHT,TOP,ROWS)

inPlay = True                                         

while inPlay:               

    for event in pygame.event.get():
        if event.type == pygame.QUIT:         
            inPlay = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                tetra.rot = (tetra.rot + 1)%4
                tetra.rotate()
                
                if tetra.collides(leftWall) or tetra.collides(rightWall) or tetra.collides(bottom):
                    tetra.rot = (tetra.rot - 1)%4
                    tetra.rotate()



#This is the code I made for collisions before reading the instructions haha
                    
##                if tetra.blocksXoffset[0]+tetra.col<=LEFT-1:
##                    print(tetra.blocksXoffset[0])
##                    tetra.rot = (tetra.rot - 1)%4
##                    tetra.rotate()
##
##                if tetra.blocksXoffset[3]+tetra.col<=LEFT-1:
##                    print(tetra.blocksXoffset[3])
##                    tetra.rot = (tetra.rot - 1)%4
##                    tetra.rotate()
##
##                if abs(tetra.blocksYoffset[0])+tetra.row==BOTTOM-1 or abs(tetra.blocksYoffset[1])+tetra.row==BOTTOM-1 or abs(tetra.blocksYoffset[2])+tetra.row==BOTTOM-1 or abs(tetra.blocksYoffset[3])+tetra.row==BOTTOM-1:
##                    print (tetra.blocksYoffset)
##                    tetra.rot = (tetra.rot - 1)%4
##                    tetra.rotate()
            

            if event.key == pygame.K_LEFT:
                tetra.move_left()
                if tetra.collides(leftWall):
                    tetra.move_right()
                    
            if event.key == pygame.K_RIGHT:
                tetra.move_right()
                if tetra.collides(rightWall):
                    tetra.move_left()
                    
            if event.key == pygame.K_DOWN:
                tetra.move_down()
                if tetra.collides(bottom):
                    tetra.move_up()        

            if event.key == pygame.K_SPACE:
                tetra.clr = tetra.clr + 1
                if tetra.clr > 7:
                    tetra.clr = 1
                tetra.rotate()

# update the screen
    redraw_screen()
    pygame.time.delay(30)
    
pygame.quit()
    
    

#Name: Thomas George
#Date: April 20, 2017
#Title: maze_functions
#Description: Functions to solve a randomly generated maze from a text file, including loading, printing, animating and solving functions


#---------------------Pygame Initialized---------------------#

import pygame
from random import randint
pygame.init()
pygame.display.set_caption("Maze")


#------------------------Colors------------------------#

WHITE = (255,255,255)     
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
ORANGE = (255,140,0)
YELLOW = (255,234,0)
INDIGO = (75,0,130)


#------------------------------------Functions-----------------------------------#

def load_maze(file_name):
    '''
    (str) --> (list)
    Text file name string is inputted and a 2D matrix of the maze from that file is returned.
    '''
    
    maze_matrix = []                                                                        #List to be filled with characters which comprise the maze.txt file
    maze_file = open(file_name,'r')                                                         #Text file containing maze
    
    for row in maze_file:
        maze_matrix.append(list(row[:-1]))                                                  #Populates list with a list of each row excluding the newline character, making a 2D array
        
    maze_file.close()
    return maze_matrix


def print_maze(maze_matrix):
    '''
    (list) -- > (none)
    2D Maze Matrix is inputted and prints a rectangular matrix in the shell, returning nothing.
    '''
    
    for i in range(len(maze_matrix)):       
        for j in range(len(maze_matrix[i])):
            print(str(maze_matrix[i][j]).center(1),end='')       
        print('')

        
def Random_coordinates_generator(maze_matrix):
    '''
    (list) --> (tuple)
    2D Maze Matrix is inputted and coordinates for the start and end points are returned in a tuple.
    '''
    
    start_coords = (randint(0,len(maze_matrix)-1),randint(0,len(maze_matrix[0])-1))         #Generates random coordinates within the dimensions of the maze for the start and finish points
    end_coords = (randint(0,len(maze_matrix)-1),randint(0,len(maze_matrix[0])-1))
    
    while maze_matrix[start_coords[0]][start_coords[1]] == '#':                             #Keeps regenerating random start coordinates until they do not lie on a maze wall, 
        start_coords = (randint(0,len(maze_matrix)-1),randint(0,len(maze_matrix[0])-1))     #if the initial coordinates were not placed in a legal position
    while maze_matrix[end_coords[0]][end_coords[1]] == '#' or (abs(start_coords[0]-end_coords[0]) < 4 and abs(start_coords[0]-end_coords[0]) < 4): 
        end_coords = (randint(0,len(maze_matrix)-1),randint(0,len(maze_matrix[0])-1))       #Keeps generating end coordinates until they are not on a wall, or very near the start point

    return start_coords[0],start_coords[1],end_coords[0],end_coords[1]

    
def maze_solver(maze_matrix,x,y):
    '''
    (list,int,int) --> (bool)
    2D Maze Matrix is inputted and True if the goal is reached and False if the attemped move is blocked.
    If a dead end is reached, recursions backtracks.
    '''
    
    #_____________Base Cases_____________#
    if maze_matrix[x][y] == '#':                                                            #Returns False if the path enters into a wall
       return False
    elif maze_matrix[x][y] == 'G':                                                          #Returns True when goal location is attained
       return True
    elif maze_matrix[x][y] not in ' S':                                                     #Returns False if the location of the attempted motion has been already passed through
       return False

    maze_matrix[x][y] = '+'                                                                 #If no base cases are satisfied, the position becomes part of the path, thus marked with "+"
    draw_maze(maze_matrix)                                                                  #Pygame image updated

    #_____________Recursive Cases_____________#
    if maze_solver(maze_matrix,x+1,y):                                                      #Recursive call checks whether a move in each direction is valid  
        return True
    elif maze_solver(maze_matrix,x,y+1):  
        return True   
    elif maze_solver(maze_matrix,x-1,y):  
        return True   
    elif maze_solver(maze_matrix,x,y-1):  
        return True
    
    maze_matrix[x][y] = 'X'                                                                  #If no recursive cases are satisfied, path backtracks (marked by "X") from the dead end
    return False


def draw_maze(matrix):
    '''
    (list) --> (none)
    2D Maze Matrix is inputted and animates the maze as it is being solved, returning nothing.
    '''
    
    HEIGHT = len(matrix)*40                                                                 #Scales dimensions of pygame window according to dimensions of maze selected by user
    WIDTH  = len(matrix[0])*40
    screen = pygame.display.set_mode((WIDTH,HEIGHT))                                        
    screen.fill(INDIGO)                                                                     #Gives window background color

    #_____________Images_____________#
    
    minecraft = pygame.image.load('img/mc.png')
    minecraft = minecraft.convert_alpha()
    minecraft = pygame.transform.scale(minecraft,(40,40))

    head = pygame.image.load('img/carl.png')
    head = head.convert_alpha()
    head = pygame.transform.scale(head,(40,40))

    start = pygame.image.load('img/start.jpg')
    start = start.convert_alpha()
    start = pygame.transform.scale(start,(40,40))

    end = pygame.image.load('img/croissant.jpg')
    end = end.convert_alpha()
    end = pygame.transform.scale(end,(40,40))
                 
    for i in range(len(matrix)):                                                            #The maze matrix, updated by the find path function, is read 
        for j in range(len(matrix[0])):                                                     #and pictures representing each character are drawn accordingly
            if matrix[i][j] == 'S':
                screen.blit(start,(j*40,i*40))
            elif matrix[i][j] == '#':
                screen.blit(minecraft,(j*40,i*40))
            elif matrix[i][j] == 'G':
                screen.blit(end,(j*40,i*40))
            elif matrix[i][j] == '+':
                screen.blit(head,(j*40,i*40))

    pygame.time.delay(30)
    pygame.display.update()

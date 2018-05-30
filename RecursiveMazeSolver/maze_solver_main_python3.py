import random
from maze_functions import*

#---------------------------------------#        
# main program                          #
#---------------------------------------#

while True:
    try:
        num = int(input('Enter the maze number: '))
        maze = load_maze('Mazes/maze'+str(num)+'.txt')
        break
    except:
        print('\nEnter an integer from 1-5, there are only 5 files.\n')


#generate random start and goal locations
Sx,Sy,Gx,Gy = Random_coordinates_generator(maze)
maze[Sx][Sy] = 'S'
maze[Gx][Gy] = 'G'
print ('\nHere is the maze with start and goal locations:')
print_maze(maze)

#now, find the path from S to G
maze_solver(maze,Sx,Sy)
print ('\nHere is the maze with the path from start to goal:\n')
maze[Sx][Sy] = 'S'
draw_maze(maze)
print_maze(maze)





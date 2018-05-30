#####################################################################
# Programmer: Thomas George
# Date: December 8, 2015
# File Name: tetris_classes2.py
# Description: These classes are templates for writing a Tetris game.
#####################################################################
import pygame

BLACK     = (  0,  0,  0)                       
RED       = (255,  0,  0)                     
GREEN     = (  0,255,  0)                     
BLUE      = (  0,  0,255)                     
ORANGE    = (255,127,  0)               
CYAN      = (  0,183,235)                   
MAGENTA   = (255,  0,255)                   
YELLOW    = (255,255,  0)
WHITE     = (255,255,255) 
COLOURS   = [ BLACK,  RED,  GREEN,  BLUE,  ORANGE,  CYAN,  MAGENTA,  YELLOW,  WHITE ]
CLR_names = ['black','red','green','blue','orange','cyan','magenta','yellow','white']
figures   = [  None , 'Z' ,  'S'  ,  'J' ,  'L'   ,  'I' ,   'T'   ,   'O'  , None  ]

class Block(object):                    
    """ A square - basic building block
        data:               behaviour:
            col - column           move left/right/up/down
            row - row              draw
            clr - colour
    """
    def __init__(self, col = 1, row = 1, clr = 1):
        self.col = col                  
        self.row = row                  
        self.clr = clr

    def __str__(self):                  
        return '('+str(self.col)+','+str(self.row)+') '+CLR_names[self.clr]

    def __eq__(self, other):
        if self.row==other.row and self.col==other.col:
            return True
        else:
            return False
        

    def draw(self, surface, gridsize=20):                     
        x = self.col * gridsize        
        y = self.row * gridsize
        CLR = COLOURS[self.clr]
        pygame.draw.rect(surface,CLR,(x,y,gridsize,gridsize), 0)
        pygame.draw.rect(surface, WHITE,(x,y,gridsize+1,gridsize+1), 1)
        
    def move_left(self):                
        self.col = self.col - 1    
        
    def move_right(self):               
        self.col = self.col + 1   
        
    def move_down(self):                
        self.row = self.row + 1   
        
    def move_up(self):                  
        self.row = self.row - 1  

#---------------------------------------#
class Cluster(object):
    """ Collection of blocks
        data:
            col - column where the anchor(reference) block is located
            row - row where the anchor(reference) block is located
            blocksNo - number of blocks
        auxiliary data:
            blocksXoffset - list of horizontal offsets for each block, in reference to the anchor block
            blocksYoffset - list of vertical offsets for each block, in reference to the anchor block
    """
    def __init__(self, col = 1, row = 1, blocksNo = 1):     # completely new init method
        self.col = col      # the column number of the anchor(reference) block                  
        self.row = row      # the row number of the anchor(reference) block                
        self.clr = 0        # this is an abstract class, so the colour is not important (invisible)
        self.blocks = [Block()]*blocksNo    #LEARN HOW TO...create clusters with different length  
        self.blocksXoffset = [0]*blocksNo
        self.blocksYoffset = [0]*blocksNo

    def update(self):
        for i in range(len(self.blocks)):
            blockCOL = self.col+self.blocksXoffset[i]  #LEARN HOW TO...calculate the coodinates of each block in a cluster
            blockROW = self.row+self.blocksYoffset[i]
            blockCLR = self.clr
            self.blocks[i]= Block(blockCOL, blockROW, blockCLR) #LEARN HOW TO...generate new block objects to form a cluster

    def draw(self, surface, gridsize):                     
        for block in self.blocks:
            block.draw(surface, gridsize)

           
    def collides(self, other):
        """ Compare each block from a cluster to all blocks from another cluster.
            Return True only if there is a location conflict.
        """

        for block in self.blocks:
            for obstacle in other.blocks:
                if block==obstacle:
                    return True
        return False            

#---------------------------------------#
class Shape(Cluster):                     
    """ A tetrominoe in one of the shapes: Z,S,J,L,I,T,O; consists of 4 x Block() objects
        data:               behaviour:
            col - column        move left/right/up/down
            row - row           draw
            clr - colour        rotate
                * figure/shape is defined by the colour
            rot - rotation             
        auxiliary data:
            blocksXoffset - list of horizontal offsets for each block, in reference to the anchor block
            blocksYoffset - list of vertical offsets for each block, in reference to the anchor block
    """
    def __init__(self, col = 1, row = 1, clr = 1):
        Cluster.__init__(self, col, row, 4)   # invoke the perenal class init method and change its parameters
        self.clr = clr    
        self.rot = 1                          # by default generates Z shape  (RED color)  
        self.blocksXoffset = [-1, 0, 0, 1]    # default rotation offsets
        self.blocksYoffset = [-1,-1, 0, 0] 
        self.rotate()
        
    def __str__(self):                  
        return figures[self.clr]+' ('+str(self.col)+','+str(self.row)+') '+CLR_names[self.clr]
    
    def rotate(self):
        """ offsets are assigned starting from the farthest (most distant) block in reference to the anchor block """
        if self.clr == 1:    #           (default rotation)    
                             #   o             o o                o              
                             # o x               x o            x o          o x
                             # o                                o              o o
            blocksXoffset = [[-1,-1, 0, 0], [-1, 0, 0, 1], [ 1, 1, 0, 0], [ 1, 0, 0,-1]]
            blocksYoffset = [[ 1, 0, 0,-1], [-1,-1, 0, 0], [-1, 0, 0, 1], [ 1, 1, 0, 0]]        
        elif self.clr == 2:  #
                             # o                 o o           o              
                             # o x             o x             x o             x o
                             #   o                               o           o o
            blocksXoffset = [[-1,-1, 0, 0], [ 1, 0, 0,-1], [ 1, 1, 0, 0], [-1, 0, 0, 1]]
            blocksYoffset = [[-1, 0, 0, 1], [-1,-1, 0, 0], [ 1, 0, 0,-1], [ 1, 1, 0, 0]]
        elif self.clr == 3:  # 
                             #   o             o                o o              
                             #   x             o x o            x           o x o
                             # o o                              o               o
            blocksXoffset = [[-1, 0, 0, 0], [-1,-1, 0, 1], [ 1, 0, 0, 0], [ 1, 1, 0,-1]]
            blocksYoffset = [[ 1, 1, 0,-1], [-1, 0, 0, 0], [-1,-1, 0, 1], [ 1, 0, 0, 0]]            
        elif self.clr == 4:  #  
                             # o o                o             o              
                             #   x            o x o             x           o x o
                             #   o                              o o         o
            blocksXoffset = [[-1, 0, 0, 0], [1, 1, 0,-1], [1, 0, 0, 0], [-1,-1, 0, 1]]
            blocksYoffset = [[-1,-1, 0, 1], [1, 0, 0, 0], [1, 1, 0,-1], [-1, 0, 0, 0]]

        elif self.clr == 5:  #   o                              o
                             #   o                              x              
                             #   x            o x o o           o          o o x o
                             #   o                              o              
            blocksXoffset = [[ 0, 0, 0, 0], [ 2, 1, 0,-1], [ 0, 0, 0, 0], [-2,-1, 0, 1]]
            blocksYoffset = [[-2,-1, 0, 1], [ 0, 0, 0, 0], [ 2, 1, 0,-1], [ 0, 0, 0, 0]]            
        elif self.clr == 6:  #
                             #   o              o                o              
                             # o x            o x o              x o         o x o
                             #   o                               o             o 
            blocksXoffset = [[ 0,-1, 0, 0], [-1, 0, 0, 1], [ 0, 1, 0, 0], [ 1, 0, 0,-1]]
            blocksYoffset = [[ 1, 0, 0,-1], [ 0,-1, 0, 0], [-1, 0, 0, 1], [ 0, 1, 0, 0]]
        elif self.clr == 7:  # 
                             # o o            o o               o o          o o
                             # o x            o x               o x          o x
                             # 
            blocksXoffset = [[-1,-1, 0, 0], [-1,-1, 0, 0], [-1,-1, 0, 0], [-1,-1, 0, 0]]
            blocksYoffset = [[ 0,-1, 0,-1], [ 0,-1, 0,-1], [ 0,-1, 0,-1], [ 0,-1, 0,-1]]
        self.blocksXoffset = blocksXoffset[self.rot]
        self.blocksYoffset = blocksYoffset[self.rot]
        self.update()

    def move_left(self):                
        self.col = self.col - 1                   
        self.update()
        
    def move_right(self):               
        self.col = self.col + 1                   
        self.update()
        
    def move_down(self):                
        self.row = self.row + 1                   
        self.update()
        
    def move_up(self):                  
        self.row = self.row - 1                   
        self.update()
                                      
#---------------------------------------#
class Floor(Cluster):
    """ Horizontal line of blocks
        data:
            col - column where the anchor block is located
            row - row where the anchor block is located
            blocksNo - number of blocks 
        auxiliary data:
            blocksXoffset - list of horizontal offsets for each block, in reference to the anchor block
    """
    def __init__(self, col = 1, row = 1, blocksNo = 1): 
        Cluster.__init__(self, col, row, blocksNo)
        for i in range(blocksNo):
            self.blocksXoffset[i] = i
        self.update()           
            
#---------------------------------------#
class Wall(Cluster):
    """ Vertical line of blocks
        data:
            col - column where the anchor block is located
            row - row where the anchor block is located
            blocksNo - number of blocks 
        auxiliary data:
            blocksYoffset - list of vertical offsets for each block, in reference to the anchor block
    """
    def __init__(self, col = 1, row = 1, blocksNo = 1): 
        Cluster.__init__(self, col, row, blocksNo)
        for i in range(blocksNo):
            self.blocksYoffset[i] = i
        self.update()  

#Name: Thomas George
#Date: March 29,2017
#Title: Tower of Hanoi
#Description: A program that illustrates how to solve the Tower of Hanoi puzzle using iteration


#######################################################Stack Class#######################################################

class Stack:                                 #Stack class is used to restrict the program from only popping the top disk
     def __init__(self,name = 'first'):
         self.items = []                     
         self.name = name                    

     def __str__(self):
          return self.name                   #Automatically returns the pole number to help with verbal instructions on how to solve the puzzle

     def isEmpty(self):
         return self.items == []             #Checks if the stack contains no discs

     def push(self, item):
         self.items.append(item)             #Adds a disk on top of the other discs previously in the stack

     def pop(self):
         return self.items.pop()             #Removes the top disc from the stack

     def peek(self):
         return self.items[len(self.items)-1]     #Checks the size of the disc at the top of the stack

     def size(self):
         return len(self.items)         #Returns how many discs are in the stack
     
     def print_(self):
          return self.items             #Print method returns a list of the disks for efficient printing


#######################################################Functions#######################################################
     
def setup(number,A,B,C):
     
     for i in range(number+1,1,-1):          #Adds the discs to the first stack in proper, descending order (largest at bottom, smallest on top)
          A.push('='*(i*2+3))
          
     if number%2 == 1:                       #Function checks if the number of discs inputted is even or odd, then returns the appropriate algorithm in a 2D matrix
         return [[A,C],[A,B],[B,C]]
     else:
         return [[A,B],[A,C],[B,C]]


def hanoi_move(sequence):

     if not sequence[1].isEmpty() and (sequence[0].isEmpty() or len(sequence[0].peek()) > len(sequence[1].peek())):     #Checks if a legal move can be made; as long as "Pole A" has a disc 
          sequence[0].push(sequence[1].pop())                                                                           #to move and "Pole B" is empty or "Pole B's" top disc is smaller than
          return sequence[1],sequence[0]                                                                                #"Pole A's", the transfer is made and the order (initial pole and 
                                                                                                                        #destination pole) returned for verbal instructions 
     elif not sequence[0].isEmpty() and(sequence[1].isEmpty() or len(sequence[1].peek()) > len(sequence[0].peek())):
          sequence[1].push(sequence[0].pop())
          return sequence[0],sequence[1]   

def draw(pos1,pos2,pos3,height):
     poles = [['|' for i in range(height-stack.size())]+stack.print_()[::-1] for stack in [pos1,pos2,pos3]]             #A 2D list containing the number of "|"s above the discs for each pole
                                                                                                                        #concatenated with the discs from the stack in descending order 
     for j in range(height):
          print(str(poles[0][j]).center(height*4),str(poles[1][j]).center(height*4),str(poles[2][j]).center(height*4))       #Centers and prints the three poles, level by level
          
     print('#'*height*12)                    #Prints ground to distinguish each of the steps' visuals


#######################################################MAIN#######################################################


print('Welcome to the Tower of Hanoi Tutorial!\n')

while True:                                                                          #Ensures user enters an integer for the number of discs
     
     try:
          count = int(input('Enter the number of disks on your tower, and then follow the steps to solve: '))
          break
     
     except:
          print('Enter an integer...\n')

     
stack_A,stack_B,stack_C = Stack(),Stack('second'),Stack('third')      #The three poles: instances of the Stack class with unique names

order = setup(count,stack_A,stack_B,stack_C)      #setup function called to output the order that the legal moves should be made

for i in range(2**count-1):             
          
     initial,final = hanoi_move(order[i%3])      #Move function called to update and return the two poles involved in the disc transfer
     
     print('\n< Move '+str(i+1)+' >\n')
     
     draw(stack_A,stack_B,stack_C,count)          #Draw function called for visual element of instructions
     
     print('Move the top disc of the '+str(initial)+' pole to the '+str(final)+' pole.')     #Verbal instructions using the names of the two poles involved in the disc transfer

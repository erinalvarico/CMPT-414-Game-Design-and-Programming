# [Name] Erin Alvarico
# [Class] CMPT 414N - Game & Programming I
# [Lab 05] OO Graphics - 9/26/2020

"""[ NOTES ] I learned a lot of new things I can utilize with random, such as
 randomizing colors and positioning. This can particularly help with game dev
 if I desire to create a randomized dungeon crawler! I enjoyed this one a lot!"""

import pygame
import random

# Variables
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# [ CLASS ] Rectangle
class Rectangle:
    def __init__(self):
        self.x = random.randint(0, 700)             # X-coordinate for Rectangle class
        self.y = random.randint(0, 500)             # Y-coordinate for Rectangle class

        self.length = random.randint(20, 70)        # Length of Rectangle class
        self.height = random.randint(20, 70)        # Height of Rectangle class

        self.change_x = random.randint(-3, 3)       # Difference in X-coord change
        self.change_y = random.randint(-3, 3)       # Difference in Y-coord change

        self.color = (random.randint(0, 255),
                      random.randint(0, 255),
                      random.randint(0, 255))       # Color of  Rectangle class

    # [ METHOD ] DRAW : creates graphic for object
    def draw(self, scr):
        # [ Green Rectangle ] Draws a green rect at rectangle's (x,y)
        pygame.draw.rect(scr, self.color, [self.x, self.y, self.length, self.height])

    # [ METHOD ] MOVE : moves drawn object to new (x,y) difference
    def move(self):
        self.x += self.change_x         # Add difference to X-coord to move original X-coord
        self.y += self.change_y         # Add difference to Y-coord to move original Y-coord


# [ CLASS ] Ellipse (Inherits Rectangle attributes)
class Ellipse(Rectangle):
    # [ METHOD ] DRAW
    def draw(self, scr):
        # [ Green Ellipse ] Draws a green ellipse at rectangle's (x,y)
        pygame.draw.ellipse(scr, self.color, [self.x, self.y, self.length, self.height])


pygame.init()   # Setup PyGame

# [ SET WINDOW/SCREEN ]
# Set the width & height of game screen [width, height]
size = (700, 500)                               # Same dimensions as template
screen = pygame.display.set_mode(size)          # Set screen size for window
pygame.display.set_caption("OO Graphics")       # Screen title displays "OO Graphics"

# [ RUNNING ]
close = False                    # Loop bool until user clicks close button
clock = pygame.time.Clock()     # Manages how fast screen updates

# [ OBJECTS ]
my_list = []                    # Create an empty list named my_list

# Loop through iteration 10 times
for i in range(1000):
    my_object = Rectangle()     # Create a Rectangle
    my_list.append(my_object)   # Push created Rectangle into list

for m in range(1000):
    my_o = Ellipse()            # Create an Ellipse
    my_list.append(my_o)        # Push created Ellipse into list

'''[ GAME START ]'''
while not close:
    # [ USER INTERACTION ]
    for event in pygame.event.get():        # User did something
        if event.type == pygame.QUIT:       # If user clicked close
            close = True                    # Flag that we are done so we exit this loop

    screen.fill(BLACK)                      # Fill screen to BLACK

    '''[ LOGIC ] '''
    # For every object in the list the loop runs
    for obj in my_list:
        obj.move()                  # Call to move method in Rectangle() class
        obj.draw(screen)            # Call to draw method in Rectangle() class

    pygame.display.flip()           # Update screen: Flip buffers
    clock.tick(60)                  # 60 frames per second

# IDLE Friendly
pygame.quit()
# [ END GAME ]

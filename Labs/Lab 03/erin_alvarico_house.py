# [Name] Erin Alvarico
# [Class] CMPT 414N - Game & Programming I
# [Lab 03] PyGame Graphics Primitives - 9/11/2020

'''[ NOTES ] I decided not to change any colors around for the house and focus on math and accuracy'''

import pygame

# Variables
# Defining Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

insetx = 100        # 100px off of the x-coord. Used to shift house right
insety = 100        # 100px off of the y-coord. Used to shift house down

# Added variables to define all drawn shapes width and heights
# Excludes roof, as it is a polygon
chimneyWidth = 20
chimneyHeight = 30
mainWidth = 200
mainHeight = 200
windowWidth = 10
windowHeight = 30
doorWidth = 20
doorHeight = 50

pygame.init()

# [ SET WINDOW/SCREEN ]
# Set the width and height of the screen [width, height]
size = (700, 500)                                   # Same screen size as template
screen = pygame.display.set_mode(size)              # Set screen size for window
pygame.display.set_caption("Welcome to My Home")    # Set name/title of screen

# [ RUNNING ]
close = False                               # Loop bool until user clicks close button
clock = pygame.time.Clock()                 # Manages how fast screen updates

'''[ GAME START ]'''
# While bool close is not true, keep running the game
while not close:
    # [ USER INTERACTION ]
    for event in pygame.event.get():        # User did something
        if event.type == pygame.QUIT:       # If user clicked close
            close = True                    # Flag that we are done so we exit this loop

    '''[ LOGIC ]'''
    # Insert code/programming logic here
    # None so far, no animation required for lab

    '''[ GRAPHICS ]'''
    # [ SCREEN ]
    # Wipe screen background to white (clear buffer)
    screen.fill(WHITE)

    # [ CHIMNEY ]
    # Utilizing a filled Rect, covered by a Polygon Roof
    pygame.draw.rect(screen, BLACK, [20 + insetx, 50 + insety, chimneyWidth, chimneyHeight], 0)

    # [ ROOF ] Two roofs drawn
    # Vertex 1: Top of house, Vertex 2: Left, Vertex 3: Right, Width Of Outline: 5px
    # Roof 1: White Fill
    pygame.draw.polygon(screen, WHITE, [[100 + insetx, insety], [insetx, 100 + insety], [200 + insetx, 100 + insety]], 0)
    # Roof 2: Black Outline
    pygame.draw.polygon(screen, BLACK, [[100 + insetx, insety], [insetx, 100 + insety], [200 + insetx, 100 + insety]], 5)

    # [ MAIN HOUSE ]
    # Value 1: x-coord, Value 2: y-coord, Value 3: Width of Rect, Value 4: Height of Rect, Width of Outline: Fill-in (0)
    pygame.draw.rect(screen, RED, [insetx, 100 + insety, mainWidth, mainHeight], 0)

    # [ WINDOWS ]
    # every step in loop (50) create a 30x10 window (4 in total)
    # Hard-coded x-coord (20) to add padding to house & y-coord (150) for roof and top padding
    for windowSeparation in range(0, 200, 50):
        pygame.draw.rect(screen, GREEN, [(20 + windowSeparation) + insetx, (150 + insety), windowWidth, windowHeight], 0)

    # [ DOOR ]
    # Utilized some math to determine middle of house
    pygame.draw.rect(screen, BLUE, [int((100 + insetx) - doorWidth/2), int(300 + insety) - doorHeight, doorWidth, doorHeight], 0)

    pygame.display.flip()   # Update screen: Flip buffers
    clock.tick(60)          # 60 Frames per second

# IDLE Friendly
pygame.quit()
# [ END GAME ]


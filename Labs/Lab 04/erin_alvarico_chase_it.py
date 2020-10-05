# [Name] Erin Alvarico
# [Class] CMPT 414N - Game & Programming I
# [Lab 04] PyGame Interactive Graphics - 9/19/2020

"""[ NOTES ] Overall had a lot of fun with this lab! Inconsistent issue: noticed when moving
cursor around (more specifically along y-coordinate) Stick will slide with cursor instead
of chasing. Not quite sure if this is a design, mathematical, or other error to fix."""

import pygame
import math

# Variables
# Defining colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize positions & speed
x_coord = 10
y_coord = 10
X_SPEED = 3
Y_SPEED = 3


# [ FUNCTION ] Draw Stick Figure
# Create stick man image on screen with designated colors
def draw_stick_figure(scr, x_mouse, y_mouse):
    # [ Head ] Colored white
    pygame.draw.ellipse(scr, WHITE, [int(1 + x_mouse), int(y_mouse), 10, 10], 0)

    # [ Legs ] Colored white
    pygame.draw.line(scr, WHITE, [int(5 + x_mouse), int(17 + y_mouse)], [int(10 + x_mouse), int(27 + y_mouse)], 2)
    pygame.draw.line(scr, WHITE, [int(5 + x_mouse), int(17 + y_mouse)], [int(x_mouse), int(27 + y_mouse)], 2)

    # [ Body ] Colored green
    pygame.draw.line(scr, GREEN, [int(5 + x_mouse), int(17 + y_mouse)], [int(5 + x_mouse), int(7 + y_mouse)], 2)

    # [ Arms ] Colored blue
    pygame.draw.line(scr, BLUE, [int(5 + x_mouse), int(7 + y_mouse)], [int(9 + x_mouse), int(17 + y_mouse)], 2)
    pygame.draw.line(scr, BLUE, [int(5 + x_mouse), int(7 + y_mouse)], [int(1 + x_mouse), int(17 + y_mouse)], 2)


# [ FUNCTION ] Stick is at Cursor's x,y: Display Text
# If the Stick successfully catches up to cursor, display text to top right of Stick
def stick_tag(scr, msg, x_stick, y_stick, x_mouse, y_mouse):
    if x_stick == x_mouse and y_stick == y_mouse:
        scr.blit(msg, [(x_mouse + 10), (y_mouse - 25)])   # Render text on screen at x + 1, y - 1 (top right of Stick)


pygame.init()  # Setup PyGame

# [ SET WINDOW/SCREEN ]
# Set the width & height of game screen [width, height]
size = [700, 500]                           # Same dimensions as template
screen = pygame.display.set_mode(size)      # Set screen size for window
pygame.display.set_caption("Chase IT!")     # Screen title displays "Chase IT!"

# [ RUNNING ]
close = False                   # Loop bool until user clicks close button
clock = pygame.time.Clock()     # Manages how fast the screen updates
pygame.mouse.set_visible(0)     # Hide mouse cursor from Player

'''[ GAME START ]'''
# While bool close is not true, keeping running the game
while not close:
    # [ USER INTERACTION ]
    for event in pygame.event.get():    # User did something
        if event.type == pygame.QUIT:   # If user clicked close
            close = True                # Flag that we are done so we exit this loop

    '''[ LOGIC ]'''
    # Fetch x and y out of list:
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]

    # [ MOVEMENT ]
    # Takes distance of Stick from cursor and updates Stick to move towards it
    sx = x - x_coord        # Distance calculated from mouse to Stick man (x)
    sy = y - y_coord        # Distance calculated from mouse to Stick man (y)

    angle = math.atan2(sx, sy)   # Calculate via arc tan to create fastest/diagonal path

    dx = X_SPEED * math.sin(angle)   # Multiply by speed for x coord
    dy = Y_SPEED * math.cos(angle)   # Multiply by speed for y coord

    x_coord += dx   # Update Stick man (x) coord
    y_coord += dy   # Update Stick man (y) coord

    # [ SNAP TO CURSOR ]
    # If x,y is within 3 units of the cursor's x,y: snap to cursor coords
    if ((x - X_SPEED) <= x_coord <= x) or ((y - Y_SPEED) <= y_coord <= y):
        x_coord = x
        y_coord = y

    '''[ GRAPHICS ]'''
    screen.fill(BLACK)                              # Fill background to black
    draw_stick_figure(screen, x_coord, y_coord)     # Call to draw_stick_figure function to draw object

    # [ FONT:TEXT ]
    # Text appears once Stick has successfully touched the mouse/cursor
    font = pygame.font.SysFont('Calibri', 25, True, False)  # Select font, size, bold and italics
    text = font.render("You're IT!", True, WHITE)           # Render text in white, not on screen yet

    stick_tag(screen, text, x_coord, y_coord, x, y)    # Call to stack_tag function to display text if cursor caught

    pygame.display.flip()       # Update screen: Flip buffers

    # I prefer 60 fps as it looks better for the Stick to chase the cursor
    # However 'move_mouse' says to limit by 20 fps. I kept it at 60
    clock.tick(60)              # 20 frames per second

# IDLE Friendly
pygame.quit()
# [ END GAME ]

# [Name] Erin Alvarico
# [Class] CMPT 414N - Game & Programming I
# [Lab 06] Refactoring OO Design - 10/3/2020

"""[ NOTES ] It was a bit challenging incorporating the subclass but overall had
no issues with the code. Fixing the bug was a nice addition to the lab as it
helped me experiment with a couple of options."""

import pygame
import random

# Variables
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)      # Blue color added

# Screen Dimensions
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400


# [ CLASS ] Block
class Block(pygame.sprite.Sprite):
    # Class members
    Width = 20          # Width of block = 20 px
    Height = 15         # Height of block = 15 px

    def __init__(self, color):
        super().__init__()                                          # Call to parent class (Sprite) constructor

        self.image = pygame.Surface([Block.Width, Block.Height])    # Create block image to block Width x Height
        self.image.fill(color)                                      # Fill created image with color

        self.rect = self.image.get_rect()                           # Fetch rect obj & update pos of rect.x & rect.y

        # Set random location for block
        self.rect.x = random.randrange(SCREEN_WIDTH - 20)           # Screen width - 20 to prevent block cutting off
        self.rect.y = random.randrange(SCREEN_HEIGHT - 20)          # Screen height - 20 to prevent block cutting off


# [ SUBCLASS ] Blue Block
class BlueBlock(Block):
    def __init__(self, blk):
        super().__init__(BLUE)      # Call to parent class (Block) + color parameter

        self.rect.x = blk.rect.x    # Set location of blue block coord-x to block
        self.rect.y = blk.rect.y    # Set location of blue block coord-y to block


pygame.init()                       # Initialize Pygame

# [ SET WINDOW/SCREEN ]
# Set the height & width of the screen [width, height]
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])     # Set Screen size for window
pygame.display.set_caption("Blue Sprite Collector")                 # Screen title displays "Blue Sprite Collector"

# [ LISTS ]
block_list = pygame.sprite.Group()              # List of sprites: managed by class Group
all_sprites_list = pygame.sprite.Group()        # List of every sprite: Blocks & Player

# [ BLACK BLOCK CREATION ]
# Creating 50 randomly placed black blocks
for i in range(50):
    block = Block(BLACK)                        # Create black block

    block_list.add(block)                       # Sprite List: Add block to the list of obj
    all_sprites_list.add(block)                 # Add block to list of obj

# [ PLAYER CREATION ]
# Create a RED player block
player = Block(RED)                             # Create red player block
all_sprites_list.add(player)                    # Add block to list of obj

# [ RUNNING ]
done = False                        # Loop bool till user clicks close button
clock = pygame.time.Clock()         # Manages how fast the Screen updates

score = 0                           # Score to keep count of blocks collected

'''[ GAME START ]'''
while not done:
    # [ USER INTERACTION ]
    for event in pygame.event.get():        # User did something
        if event.type == pygame.QUIT:       # If user clicks close
            done = True                     # Flag that we are done & exits loop

    screen.fill(WHITE)                      # Clear the Screen

    '''[ LOGIC ]'''
    pos = pygame.mouse.get_pos()            # Current mouse position: List of two nums

    # [ PLAYER MOVEMENT ]
    # Fetch the x and y out of the list,
    # just like we'd fetch letters out of a string.
    # Set the player object to the mouse location
    player.rect.x = pos[0]
    player.rect.y = pos[1]

    # [ CHECK COLLISION ]
    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)

    # [ UPDATE SCORE & CREATE BLUE BLOCK ]
# Check the list of collisions
    for block in blocks_hit_list:
        CollideBlock = BlueBlock(block)         # Create a blue block after collision
        all_sprites_list.add(CollideBlock)      # Add blue block to list of obj

        score += 1                              # Add 1 point to score for collision detected
        print(score)                            # Print updated score to console

    '''[ GRAPHICS ]'''
    all_sprites_list.draw(screen)       # Draw all sprites on screen

    pygame.display.flip()               # Update Screen: Flip buffers
    clock.tick(60)                      # 60 frames per second

# IDLE Friendly
pygame.quit()
# [ END GAME ]

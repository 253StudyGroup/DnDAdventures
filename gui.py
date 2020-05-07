######do-the-gui-baby.py
import pygame
from pygame.locals import *
from random import randint
import time
#######VARIABLE INIT#########
size = 1200, 900 #Sets Window Size
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)

BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
SILVER = (192,192,192)
LIGHTGRAY = (211,211,211)
WHITE = (255, 255, 255)

dir = {K_LEFT: (-5, 0), K_RIGHT: (5, 0), K_UP: (0, -5), K_DOWN: (0, 5)}

width, height = size


#class Text(Node):
"""Create a text object which knows how to draw itself."""
#    fontname = None
#    fontsize = 36
#    fontcolor = Color('BLACK')
#    background = None
#    italic = False
#    bold = False
#    underline = False




############################


pygame.init() #Begins the program.

##SETUP STUFF


screen = pygame.display.set_mode(size) #Brings up a Display
#variableName = Rect(X, Y, W, H)
nameBox = Rect(0, 0, 400, 15)
healthBar = Rect(0, 15, 400, 15)
horizontalBottomBar = Rect(0, 700, 1200, 3)
horizontalTopBar = Rect(0, 30, 1200, 3)
verticalBottomBarLeft = Rect(400, 700, 3, 200)
verticalBottomBarRight = Rect(800, 700, 3, 200)
verticalTopBarLeft = Rect(400,0,3,30)
verticalTopBarRight = Rect(800,0,3,30)
"""print(f'x={nameBox.x}, y={nameBox.y}, width={nameBox.w}, height={nameBox.h}')
print(f'leftBound={nameBox.left}, topBound={nameBox.top}, rightBound={nameBox.right}, bottomBound={nameBox.bottom}')
print(f'centerLocation={nameBox.center}')"""




running = True #ENSURES THE GAME RUNS

while running: #NECESSARY TO START THE PROGRAM
    for event in pygame.event.get():
        if event.type == QUIT: #LOOP ALLOWS EXIT TO HAPPEN (otherwise you have to force close)
            running = False

    screen.fill(LIGHTGRAY)
    pygame.draw.rect(screen, BLACK, nameBox)
    pygame.draw.rect(screen, RED, healthBar)
    pygame.draw.rect(screen, SILVER, horizontalBottomBar)
    pygame.draw.rect(screen, SILVER, horizontalTopBar)
    pygame.draw.rect(screen, SILVER, verticalBottomBarLeft)
    pygame.draw.rect(screen, SILVER, verticalBottomBarRight)
    pygame.draw.rect(screen, SILVER, verticalTopBarRight)
    pygame.draw.rect(screen, SILVER, verticalTopBarLeft)
    pygame.display.flip()




    pygame.display.update()
pygame.quit()
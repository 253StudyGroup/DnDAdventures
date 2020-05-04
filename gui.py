######do-the-gui-baby.py
import pygame
from pygame.locals import *

import time
#######VARIABLE INIT#########
size = 1200, 900 #Sets Window Size
RED = (255,0,0)
GRAY = (150,150,150)
BLACK = (0,0,0)

width, height = size

############################


pygame.init() #Begins the program.

##SETUP STUFF


screen = pygame.display.set_mode(size) #Brings up a Display
#variableName = Rect(X, Y, W, H)
nameBox = Rect(1, 1, 300, 15)
healthBar = Rect(1, 16, 300, 15)
print(f'x={nameBox.x}, y={nameBox.y}, width={nameBox.w}, height={nameBox.h}')
print(f'leftBound={nameBox.left}, topBound={nameBox.top}, rightBound={nameBox.right}, bottomBound={nameBox.bottom}')
print(f'centerLocation={nameBox.center}')




running = True #ENSURES THE GAME RUNS

while running: #NECESSARY TO START THE PROGRAM
    for event in pygame.event.get():
        if event.type == QUIT: #LOOP ALLOWS EXIT TO HAPPEN (otherwise you have to force close)
            running = False

    screen.fill(GRAY)
    pygame.draw.rect(screen, BLACK, nameBox)
    pygame.draw.rect(screen, RED, healthBar)
    pygame.display.flip()




    pygame.display.update()
pygame.quit()
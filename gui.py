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
WHITE = (255, 255, 255)

dir = {K_LEFT: (-5, 0), K_RIGHT: (5, 0), K_UP: (0, -5), K_DOWN: (0, 5)}

width, height = size

############################


pygame.init() #Begins the program.

##SETUP STUFF


screen = pygame.display.set_mode(size) #Brings up a Display
#variableName = Rect(X, Y, W, H)
nameBox = Rect(0, 0, 300, 15)
healthBar = Rect(0, 15, 300, 15)
seperatorLine = Rect(0, 700, 1200, 5)
seperatorLine2 = Rect(400, 700, 5, 200)
seperatorLine3 = Rect(800, 700, 5, 200)
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
    pygame.draw.rect(screen, BLACK, seperatorLine)
    pygame.draw.rect(screen, BLACK, seperatorLine2)
    pygame.draw.rect(screen, BLACK, seperatorLine3)
    pygame.display.flip()




    pygame.display.update()
pygame.quit()
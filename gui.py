######do-the-gui-baby.py
import pygame
from pygame.locals import *

import time
#######VARIABLE INIT#########
size = 1200, 900 #Sets Window Size
RED = (255,0,0)
GRAY = (150,150,150)

width, height = size

############################


pygame.init() #Begins the program.

##SETUP STUFF


screen = pygame.display.set_mode(size) #Brings up a Display
#variableName = Rect(X, Y, W, H)
nameBox = Rect(0,0,300,25)



running = True #ENSURES THE GAME RUNS

while running: #NECESSARY TO START THE PROGRAM
    for event in pygame.event.get():
        if event.type == QUIT: #LOOP ALLOWS EXIT TO HAPPEN (otherwise you have to force close)
            running = False
	screen.fill(GRAY)
	pygame.draw.rect(screen, RED, rect)





    pygame.display.update()
pygame.quit()
#dnd_game
import DnD_Character_v1 #as character_class

import os
import pygame
import pygame.freetype
import math
import time

pygame.init()
pygame.freetype.init()


size = [800, 640]
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

strong = 1
fast = 2
tough = 3
wise = 4
smart = 5
charasmatic = 6
commoner = 0

screen = pygame.display.set_mode(size)
screen.fill(GREEN)





player1 = DnD_Character_v1.Character_Class()
character_weight = player1.character_weight()
total_weight = player1.total_weight()

print ("character_weight")
print ( character_weight )
print ("total_weight")
print ( total_weight )

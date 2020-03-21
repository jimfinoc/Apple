import pygame
pygame.joystick.init()
connected = pygame.joystick.get_count()
print "you have", connected, "connected controllers"

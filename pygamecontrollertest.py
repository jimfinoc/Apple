import pygame
import time
pygame.init()
pygame.joystick.init()
connected = pygame.joystick.get_count()
print "you have", connected, "connected controllers"

xAxisNum = 0
yAxisNum = 1


joystick = []
for each in range(connected):
    joystick.append( pygame.joystick.Joystick(each) )
    joystick[each].init()
    axes = joystick[each].get_numaxes()
    buttons = joystick[each].get_numbuttons()
    print "axes"
    print (axes)
    print "buttons"
    print (buttons)


while True:
    time.sleep(.1)
    for each in range(connected):

        print "Joystick", each ,":"
        # print joystick[each].get_axis(xAxisNum)
        # print joystick[each].get_axis(yAxisNum)
        for eachbutton in range(buttons):
            print eachbutton, "each",joystick[each].get_button(each),
        print ""

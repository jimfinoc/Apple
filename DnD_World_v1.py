import os
import pygame
import pygame.freetype
import math
import time
import random

pygame.init()
pygame.freetype.init()


size = [800, 640]
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)


class World_Terrain(object):
    def __init__(self,screen=None, color=GREEN, center= [0,0], location=(0,0), direction = [0]):
    # def circle_man(screen, color=WHITE, center = [0,0], direction = [0]):
        _circle_radius = 75
        _thickness = 3
        horizontal_center = center[0]
        verticle_center = center[1]
        left_pos = center[0]-_circle_radius*2/3
        small_left_pos = center[0]-_circle_radius*1/2
        top_pos = center[1]-_circle_radius*1/2
        small_top_pos = center[1]-_circle_radius*1/3
        right = _circle_radius*4/3
        small_right = _circle_radius*2/2
        bottom = _circle_radius*2/2
        small_bottom = _circle_radius*2/3
        right_pos = center[0] +_circle_radius*2/3
        bottom_pos = center[1] +_circle_radius*1/2

        # screen = pygame.display.set_mode((600, 400))
        # rect = screen.get_rect()
        # pygame.font.init()
        # font = pygame.font.Font(pygame.font.get_default_font(),30)
        # fontfile = pygame.freetype.get_default_font()
        # fontfile = pygame.freetype.SysFont()
        fontfile = pygame.freetype.get_default_font()

        size = 3
        size=0
        font_index=0
        resolution=0

        # font = pygame.font.SysFont("comicsansms", 72)
        # text = font.render("Hello, World", False, color)
        # screen.blit(text, (800//2 - text.get_width() // 2, 640//2 - text.get_height() // 2))
        # font = pygame.font.SysFont("comicsansms", 72)
        font = pygame.font.SysFont("arial", 30)
        # font = pygame.font.SysFont("timesnewroman", 30)
        text = {}
        text[strong] = font.render("strong", False, color)
        text[fast] = font.render("fast", False, color)
        text[tough] = font.render("tough", False, color)
        text[wise] = font.render("wise", False, color)
        text[smart] = font.render("smart", False, color)
        text[charasmatic] = font.render("charasmatic", False, color)
        text[commoner] = font.render("commoner", False, color)
        # print ("")
        # print (text)
        # print ("")

        if (screen != None):
            pygame.draw.rect(screen,  color, [left_pos , top_pos , right , bottom ], _thickness)
            # pygame.draw.arc(screen, color, [center[0]-_circle_radius   , center[1]-_circle_radius   , _circle_radius*2    , _circle_radius*2]     ,direction-math.pi/ 8,direction+math.pi/ 8)
            if (direction!=None):
                pygame.draw.arc(screen, color, [center[0]-_circle_radius-2 , center[1]-_circle_radius-2 , _circle_radius*2+ 4 , _circle_radius*2+ 4 ] ,direction-math.pi/ 8,direction+math.pi/ 8)
                pygame.draw.arc(screen, color, [center[0]-_circle_radius-4 , center[1]-_circle_radius-4 , _circle_radius*2+ 8 , _circle_radius*2+ 8  ] ,direction-math.pi/32,direction+math.pi/32)
                pygame.draw.arc(screen, color, [center[0]-_circle_radius-6 , center[1]-_circle_radius-6 , _circle_radius*2+12 , _circle_radius*2+12 ] ,direction-math.pi/64,direction+math.pi/64)
            else:
                pass
            if (True):
            # if character_type == strong:
            #     pygame.draw.line(screen, color, [left_pos, top_pos ],[right_pos, bottom_pos], _thickness)
            #     pygame.draw.line(screen, color, [left_pos, bottom_pos ],[right_pos,top_pos], _thickness)
            #     screen.blit(text[strong], (center[0] - text[strong].get_width() // 2, center[1] + _circle_radius*2//3 - text[strong].get_height() // 2))
            #     # screen.blit(text[strong], (800//2 - text[strong].get_width() // 2, 640//2 - text[strong].get_height() // 2))
            #     # screen.blit(text[strong], (center[0] - text.get_width() // 2, center[1] - text.get_height() // 2))
            # elif character_type == fast:
            #     pygame.draw.line(screen, color, [left_pos, bottom_pos ],[right_pos, top_pos ], _thickness)
            #     screen.blit(text[fast], (center[0] - text[fast].get_width() // 2, center[1] + _circle_radius*2//3 - text[fast].get_height() // 2))
            #     # pygame.draw.line(screen, color, [left_pos, bottom_pos ],[right_pos,top_pos], _thickness)
            # elif character_type == tough:
            #     pass
            #     pygame.draw.ellipse(screen, color, [small_left_pos, small_top_pos, small_right,small_bottom], _thickness)
            #     screen.blit(text[tough], (center[0] - text[tough].get_width() // 2, center[1] + _circle_radius*2//3 - text[tough].get_height() // 2))
            #
            #     # pygame.draw.line(screen, color, [left_pos, top_pos ],[right_pos, bottom_pos], _thickness)
            #     # pygame.draw.line(screen, color, [left_pos, bottom_pos ],[right_pos,top_pos], _thickness)
            # elif character_type == wise:
            #     pygame.draw.line(screen, color, [horizontal_center, top_pos ],[horizontal_center, bottom_pos], _thickness)
            #     pygame.draw.line(screen, color, [left_pos, verticle_center ],[right_pos,verticle_center], _thickness)
            #     screen.blit(text[wise], (center[0] - text[wise].get_width() // 2, center[1] + _circle_radius*2//3 - text[wise].get_height() // 2))
            # elif character_type == smart:
            #     pygame.draw.line(screen, color, [left_pos, verticle_center + _circle_radius/4],[right_pos,verticle_center +_circle_radius/4], _thickness)
            #     screen.blit(text[smart], (center[0] - text[smart].get_width() // 2, center[1] + _circle_radius*2//3 - text[smart].get_height() // 2))
            #     # pygame.draw.line(screen, color, [left_pos, bottom_pos ],[right_pos,top_pos], _thickness)
            # elif character_type == charasmatic:
            #     pass
            #     pygame.draw.line(screen, color, [left_pos, top_pos ],[horizontal_center, verticle_center + _circle_radius/4], _thickness)
            #     pygame.draw.line(screen, color, [horizontal_center, verticle_center + _circle_radius/4],[horizontal_center, verticle_center - _circle_radius/4], _thickness)
            #     pygame.draw.line(screen, color, [horizontal_center, verticle_center - _circle_radius/4],[right_pos, bottom_pos], _thickness)
            #     # pygame.draw.circle(screen, color, center, _circle_radius/6, 11)
            #     screen.blit(text[charasmatic], (center[0] - text[charasmatic].get_width() // 2, center[1] + _circle_radius*2//3 - text[charasmatic].get_height() // 2))
            #
            # else:
                screen.blit(text[commoner], (center[0] - text[commoner].get_width() // 2, center[1] + _circle_radius*2//3 - text[commoner].get_height() // 2))
                # location = (0,0)
                location_text = font.render(str((location)), False, color)
                screen.blit(location_text, (center[0] - location_text.get_width() // 2, center[1] + _circle_radius*2//3 - location_text.get_height() // 2 + 100))

        else:
            pass


prior_key_states = pygame.key.get_pressed()

if __name__ == '__main__':  # single underscore
    location = (0,0)
    strong = 1
    fast = 2
    tough = 3
    wise = 4
    smart = 5
    charasmatic = 6
    commoner = 0
    pygame.display.set_caption("Presenting the World")
    done = False
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(size)

    angle = 0
    while not done:
        screen.fill(GREEN)
        clock.tick(10)
        pygame.joystick.init()
        joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        joystick_count = pygame.joystick.get_count()
        print joystick_count

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # pygame.draw.circle(screen, WHITE, [80, 80], 75, 1)
        # World_Terrain(screen,BLUE,[250,200],-math.pi/3)
        # angle += 5
        keys = pygame.key.get_pressed()

        if keys[pygame.K_q] and not prior_key_states[pygame.K_q]:
            done = True
        if keys[pygame.K_LEFT] and not prior_key_states[pygame.K_LEFT]:
            # location = (location[0] -1 ,location[1] +0)
            change_x = -1
            # print location
        elif keys[pygame.K_RIGHT] and not prior_key_states[pygame.K_RIGHT]:
            # location = (location[0] +1 ,location[1] +0)
            change_x = 1
            # print location
        else:
            change_x = 0
        if keys[pygame.K_UP] and not prior_key_states[pygame.K_UP]:
            change_y = 1
            # location = (location[0] +0 ,location[1] +1)
            # print location
        elif keys[pygame.K_DOWN] and not prior_key_states[pygame.K_DOWN]:
            change_y = -1
            # location = (location[0] +0 ,location[1] -1)
            # print location
        else:
            change_y = 0

        if joysticks:
            for i in range(joystick_count):
                joystick = pygame.joystick.Joystick(i)
                joystick.init()
                # axes = joystick.get_numaxes()
                # # print ("Number of axes: {}".format(axes))
                # for i in range(axes):
                #     axis = joystick.get_axis(i)
                #     # print ("Axis {} value: {:>6.3f}".format(i, round(axis)))
                # buttons = joystick.get_numbuttons()
                # # print ("Number of buttons: {}".format(buttons))
                # for i in range(buttons):
                #     button = joystick.get_button(i)
                    # print ("Button {:>2} value: {}".format(i, button))
            if change_x == 0:
                change_x = int(round(joystick.get_axis(3)))
            if change_y == 0:
                change_y = -int(round(joystick.get_axis(4)))
            location = (location[0] + change_x , location[1])
            location = (location[0]            , location[1] + change_y )



        if (change_x | change_y):
            angle = math.atan2(change_y,change_x)
            print "Moving"
        else:
            print "Not Moving"
            mouse = pygame.mouse.get_pos()
            # print mouse
            centered_mouse = (mouse[0]-400,mouse[1]-320)
            # print centered_mouse
            buttons = pygame.mouse.get_pressed()
            if (buttons[0]):
                angle = math.atan2(-centered_mouse[1],centered_mouse[0])
                change_x = int(2*math.cos(angle))
                change_y = int(2*math.sin(angle))
            else:
                angle = None



        print "direction", change_x, change_y, "angle", angle

        location = (location[0]+change_x,location[1]+change_y)
        World_Terrain(screen,BLACK,[400,320],location, angle) #*math.pi/180)
        pygame.display.update()
        # pygame.display.flip()
    pygame.quit()
else:
    pass

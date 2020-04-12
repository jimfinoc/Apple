#
import os
import pygame
import pygame.freetype
import math
import time

pygame.init()
pygame.freetype.init()
print time.time()

size = [1600, 1280]
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

screen = pygame.display.set_mode(size)
screen.fill(GREEN)

class CharacterGraphic(object):
    def __init__(self,screen, color=WHITE, center= [0,0], direction = [0],character_type = 1):
    # def circle_man(screen, color=WHITE, center = [0,0], direction = [0]):
        _circle_radius = 75
        _thickness = 3
        # pygame.draw.circle(screen, color, center, _circle_radius, 1)
        #
        # # right arm
        # _line_start = [center[0]+_circle_radius*math.cos(direction+math.pi/2) ,center[1]+_circle_radius*math.sin(direction+math.pi/2) ]
        # _line_end = [center[0]+(_circle_radius+10)*math.cos(direction+math.pi/2) ,center[1]+(_circle_radius+10)*math.sin(direction+math.pi/2) ]
        # pygame.draw.line(screen, color, _line_start,_line_end, _thickness)
        # pass
        #
        # # left arm
        # _line_start = [center[0]+_circle_radius*math.cos(direction-math.pi/2) ,center[1]+_circle_radius*math.sin(direction-math.pi/2) ]
        # _line_end = [center[0]+(_circle_radius+10)*math.cos(direction-math.pi/2) ,center[1]+(_circle_radius+10)*math.sin(direction-math.pi/2) ]
        # # _line_end = [center[0]+(_circle_radius+10)*math.cos(direction) ,center[1]+(_circle_radius+10)*math.sin(direction) ]
        # # _line_end = [800,640]
        # pygame.draw.line(screen, color, _line_start,_line_end, _thickness)
        # pass
        strong = 1
        fast = 2
        tough = 3
        wise = 4
        smart = 5
        charasmatic = 6
        commoner = 0
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
        # text = font.render("Hello, World", False, (0, 0, 0))
        # screen.blit(text, (800//2 - text.get_width() // 2, 640//2 - text.get_height() // 2))
        print 1,time.time()
        # font = pygame.font.SysFont("comicsansms", 72)
        font = pygame.font.SysFont("arial", 30)
        # font = pygame.font.SysFont("timesnewroman", 30)
        text = {}
        print 2,time.time()
        text[strong] = font.render("strong", False, (0, 0, 0))
        text[fast] = font.render("fast", False, (0, 0, 0))
        text[tough] = font.render("tough", False, (0, 0, 0))
        text[wise] = font.render("wise", False, (0, 0, 0))
        text[smart] = font.render("smart", False, (0, 0, 0))
        text[charasmatic] = font.render("charasmatic", False, (0, 0, 0))
        text[commoner] = font.render("commoner", False, (0, 0, 0))
        # print ("")
        # print (text)
        # print ("")


        pygame.draw.rect(screen,  color, [left_pos , top_pos , right , bottom ], _thickness)
        if character_type == strong:
            pygame.draw.line(screen, color, [left_pos, top_pos ],[right_pos, bottom_pos], _thickness)
            pygame.draw.line(screen, color, [left_pos, bottom_pos ],[right_pos,top_pos], _thickness)
            screen.blit(text[strong], (center[0] - text[strong].get_width() // 2, center[1] + _circle_radius*2//3 - text[strong].get_height() // 2))
            # screen.blit(text[strong], (800//2 - text[strong].get_width() // 2, 640//2 - text[strong].get_height() // 2))
            # screen.blit(text[strong], (center[0] - text.get_width() // 2, center[1] - text.get_height() // 2))
        elif character_type == fast:
            pygame.draw.line(screen, color, [left_pos, bottom_pos ],[right_pos, top_pos ], _thickness)
            screen.blit(text[fast], (center[0] - text[fast].get_width() // 2, center[1] + _circle_radius*2//3 - text[fast].get_height() // 2))
            # pygame.draw.line(screen, color, [left_pos, bottom_pos ],[right_pos,top_pos], _thickness)
        elif character_type == tough:
            pass
            pygame.draw.ellipse(screen, color, [small_left_pos, small_top_pos, small_right,small_bottom], _thickness)
            screen.blit(text[tough], (center[0] - text[tough].get_width() // 2, center[1] + _circle_radius*2//3 - text[tough].get_height() // 2))

            # pygame.draw.line(screen, color, [left_pos, top_pos ],[right_pos, bottom_pos], _thickness)
            # pygame.draw.line(screen, color, [left_pos, bottom_pos ],[right_pos,top_pos], _thickness)
        elif character_type == wise:
            pygame.draw.line(screen, color, [horizontal_center, top_pos ],[horizontal_center, bottom_pos], _thickness)
            pygame.draw.line(screen, color, [left_pos, verticle_center ],[right_pos,verticle_center], _thickness)
            screen.blit(text[wise], (center[0] - text[wise].get_width() // 2, center[1] + _circle_radius*2//3 - text[wise].get_height() // 2))
        elif character_type == smart:
            pygame.draw.line(screen, color, [left_pos, verticle_center + _circle_radius/4],[right_pos,verticle_center +_circle_radius/4], _thickness)
            screen.blit(text[smart], (center[0] - text[smart].get_width() // 2, center[1] + _circle_radius*2//3 - text[smart].get_height() // 2))
            # pygame.draw.line(screen, color, [left_pos, bottom_pos ],[right_pos,top_pos], _thickness)
        elif character_type == charasmatic:
            pass
            pygame.draw.line(screen, color, [left_pos, top_pos ],[horizontal_center, verticle_center + _circle_radius/4], _thickness)
            pygame.draw.line(screen, color, [horizontal_center, verticle_center + _circle_radius/4],[horizontal_center, verticle_center - _circle_radius/4], _thickness)
            pygame.draw.line(screen, color, [horizontal_center, verticle_center - _circle_radius/4],[right_pos, bottom_pos], _thickness)
            # pygame.draw.circle(screen, color, center, _circle_radius/6, 11)
            screen.blit(text[charasmatic], (center[0] - text[charasmatic].get_width() // 2, center[1] + _circle_radius*2//3 - text[charasmatic].get_height() // 2))

        else:
            screen.blit(text[commoner], (center[0] - text[commoner].get_width() // 2, center[1] + _circle_radius*2//3 - text[commoner].get_height() // 2))



if __name__ == '__main__':  # single underscore
    pygame.display.set_caption("Drawing a circle man")
    done = False
    clock = pygame.time.Clock()
    print time.time()
    while not done:
        print time.time()
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # pygame.draw.circle(screen, WHITE, [80, 80], 75, 1)
        print "loading first character",time.time()
        CharacterGraphic(screen,BLACK,[400,200],-math.pi/3,1)
        CharacterGraphic(screen,RED,[250,320],math.pi/8,2)
        CharacterGraphic(screen,BLUE,[550,320],math.pi/8,3)
        CharacterGraphic(screen,BLACK,[400,440],-math.pi/3,4)
        CharacterGraphic(screen,RED,[250,440],math.pi/8,5)
        CharacterGraphic(screen,BLUE,[550,440],math.pi/8,6)
        CharacterGraphic(screen,WHITE,[400,560],math.pi/8,0)
        pygame.display.update()
        pygame.display.flip()

    # this line exits the program
    pygame.quit()

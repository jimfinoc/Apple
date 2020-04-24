#
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
            pygame.draw.arc(screen, color, [center[0]-_circle_radius,center[1]-_circle_radius,_circle_radius*2,_circle_radius*2],direction-math.pi/16,direction+math.pi/16)
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
        else:
            pass



if __name__ == '__main__':  # single underscore
    strong = 1
    fast = 2
    tough = 3
    wise = 4
    smart = 5
    charasmatic = 6
    commoner = 0
    pygame.display.set_caption("Drawing a circle man")
    done = False
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode(size)
    screen.fill(GREEN)


    while not done:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # pygame.draw.circle(screen, WHITE, [80, 80], 75, 1)
        CharacterGraphic(screen,BLUE,[250,200],-math.pi/3,strong)
        CharacterGraphic(screen,BLUE,[250,320],math.pi/8,fast)
        CharacterGraphic(screen,BLUE,[250,440],math.pi/8,charasmatic)

        CharacterGraphic(screen,RED,[550,320],math.pi,tough)
        CharacterGraphic(screen,RED,[550,440],math.pi,wise)
        CharacterGraphic(screen,RED,[550,200],math.pi,smart)
        CharacterGraphic(screen,WHITE,[400,560],math.pi/2,commoner)
        pygame.display.update()
        pygame.display.flip()
    pygame.quit()
else:
    pass

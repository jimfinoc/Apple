#
import pygame
import math
pygame.init()

size = [800, 640]
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

screen = pygame.display.set_mode(size)
screen.fill(GREEN)

def circle_man(screen, color=WHITE, center = [0,0], direction = [0]):
    _circle_radius = 75
    _thickness = 3
    pygame.draw.circle(screen, color, center, _circle_radius, _thickness)

    # right arm
    _line_start = [center[0]+_circle_radius*math.cos(direction+math.pi/2) ,center[1]+_circle_radius*math.sin(direction+math.pi/2) ]
    _line_end = [center[0]+(_circle_radius+10)*math.cos(direction+math.pi/2) ,center[1]+(_circle_radius+10)*math.sin(direction+math.pi/2) ]
    pygame.draw.line(screen, color, _line_start,_line_end, _thickness)
    pass

    # left arm
    _line_start = [center[0]+_circle_radius*math.cos(direction-math.pi/2) ,center[1]+_circle_radius*math.sin(direction-math.pi/2) ]
    _line_end = [center[0]+(_circle_radius+10)*math.cos(direction-math.pi/2) ,center[1]+(_circle_radius+10)*math.sin(direction-math.pi/2) ]
    # _line_end = [center[0]+(_circle_radius+10)*math.cos(direction) ,center[1]+(_circle_radius+10)*math.sin(direction) ]
    # _line_end = [800,640]
    pygame.draw.line(screen, color, _line_start,_line_end, _thickness)
    pass

pygame.display.set_caption("Drawing a circle man")
done = False
clock = pygame.time.Clock()


if __name__ == '__main__':  # single underscore
    while not done:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pygame.draw.circle(screen, WHITE, [80, 80], 75, 1)
        circle_man(screen,BLACK,[400,320],-math.pi/3)
        circle_man(screen,RED,[300,320],math.pi/8)
        pygame.display.flip()

    # this line exits the program
    pygame.quit()

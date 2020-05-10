#
import pygame
import math
import pygame.locals
import csv
import random

pygame.init()
size = [720, 320]
# size = [800, 640]
# size = [1600, 1280]
# size = [1920, 1200]
# size = [2880, 1800]
# size = [3440, 1440]
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)


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

def load_tile_table(filename, width, height):
    image = pygame.image.load(filename).convert_alpha()
    image_width, image_height = image.get_size()
    tile_table = []
    for tile_x in range(0, image_width/width):
        line = []
        tile_table.append(line)
        for tile_y in range(0, image_height/height):
            rect = (tile_x*width, tile_y*height, width, height)
            line.append(image.subsurface(rect))
    return tile_table

pygame.display.set_caption("Drawing a circle man")
done = False
clock = pygame.time.Clock()


if __name__ == '__main__':  # single underscore
    world = {}
    csv_filename = "world2.csv"
    # with open(csv_filename) as csvfile:
    csvfile = open(csv_filename, 'r')
    reader = csvfile.read()
    csvfile.close()
    # reader = csv.DictReader(csvfile,  delimiter=',', quotechar='|')
    # rows = reader.split("/n")
    rows = reader.splitlines()

    row_y = 0
    for row in rows:
        # print row_y, row
        row_y += 1
        column_x = 0
        for column in row.split(","):
            # print column_x,column
            column_x += 1
            world[column_x,row_y] = int(column)
    # print world


    print pygame.display.Info()
    # screen = pygame.display.set_mode(size)
    screen = pygame.display.set_mode(size,
    # screen = pygame.display.set_mode((width, height),
                        # pygame.DOUBLEBUF | pygame.RESIZABLE)
                        pygame.FULLSCREEN |
                        pygame.DOUBLEBUF )
                        # pygame.OPENGL | pygame.DOUBLEBUF | pygame.RESIZABLE)

    z = pygame.display.get_surface().get_size()
    print "screen and sprite size"
    print z
    print "/16"
    print (z[0]/16,z[1]/16)

    land_tiles = load_tile_table("land_tiles.png", 16, 16)
    graphic_memory = {}
    for x, row in enumerate(land_tiles):
        for y, tile in enumerate(row):
            graphic_memory[y*30+x] = tile
    print "graphic_memory loaded", len(graphic_memory), "sprites."

    font_tiles = load_tile_table("font_tiles.png",8,8)
    font_memory = {}
    for x, row in enumerate(font_tiles):
        for y, tile in enumerate(row):
            font_memory[y*8+x] = tile
    print "font_memory loaded", len(font_memory), "sprites."

    character_tiles = load_tile_table("character_tiles.png",16,16)
    character_memory = {}
    for x, row in enumerate(character_tiles):
        for y, tile in enumerate(row):
            character_memory[y*8+x] = tile
    print "character_memory loaded", len(character_memory), "sprites."

    small_font_tiles = load_tile_table("small_font_tiles.png",16,16)
    small_font_memory = {}
    for x, row in enumerate(small_font_tiles):
        for y, tile in enumerate(row):
            small_font_memory[y*8+x] = tile
    print "character_memory loaded", len(character_memory), "sprites."


    step = 50
    half_step = step / 2
    h_steps = pygame.display.get_surface().get_size()[0] /step
    v_steps = pygame.display.get_surface().get_size()[1] / step
    print ""
    print "step", step
    print "half_step", half_step
    print "h_steps", h_steps
    print "v_steps", v_steps
    print ""
    # screen = pygame.display.set_mode(size,pygame.FULLSCREEN)
    screen.fill(GREEN)
    screen.fill(BLACK)
    timer = 0
    keys = pygame.key.get_pressed()
    game_location = (random.randint(0,3),random.randint(0,3))
    game_location = (3,3)

    while not done:
        # done = True
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        prior_key_states = keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q] and not prior_key_states[pygame.K_q]:
            done = True

        # pygame.dr
        xi = 0
        yi = 0

        my_location_x, my_location_y = (10,10)
        bad_guy_location_x, bad_guy_location_y = (8,12)

        center_x = pygame.display.get_surface().get_size()[0]/2
        center_y = pygame.display.get_surface().get_size()[1]/2

        screen.blit(graphic_memory[7], (-8, -8)) # 0

        vision = 10
        for x in range(-vision,vision+1):
            for y in range(-vision,vision+1):
                try:
                    location = (game_location[0] + x,game_location[1] + y)
                    print "location",location, world[location]
                    image = graphic_memory[world[location]]
                except:
                    image = graphic_memory[30*14+7]
                screen.blit(image, (center_x - 8+16 *  x, center_y-8+16 *  y))

        # screen.blit(graphic_memory[7], (center_x - 8+16 * -2, center_y-8+16 *  -1))
        # screen.blit(graphic_memory[7], (center_x - 8+16 * -1, center_y-8+16 *  -1))
        # screen.blit(graphic_memory[7], (center_x - 8+16 *  0, center_y-8+16 *  -1))
        # screen.blit(graphic_memory[7], (center_x - 8+16 *  1, center_y-8+16 *  -1))
        # screen.blit(graphic_memory[7], (center_x - 8+16 *  2, center_y-8+16 *  -1))
        #
        # screen.blit(graphic_memory[7], (center_x - 8+16 * -2, center_y-8+16 *   0))
        # screen.blit(graphic_memory[7], (center_x - 8+16 * -1, center_y-8+16 *   0))
        # screen.blit(graphic_memory[7], (center_x - 8+16 *  0, center_y-8+16 *   0))
        # screen.blit(graphic_memory[7], (center_x - 8+16 *  1, center_y-8+16 *   0))
        # screen.blit(graphic_memory[7], (center_x - 8+16 *  2, center_y-8+16 *   0))
        #
        # screen.blit(graphic_memory[7], (center_x - 8+16 * -2, center_y-8+16 *   1))
        # screen.blit(graphic_memory[7], (center_x - 8+16 * -1, center_y-8+16 *   1))
        # screen.blit(graphic_memory[7], (center_x - 8+16 *  0, center_y-8+16 *   1))
        # screen.blit(graphic_memory[7], (center_x - 8+16 *  1, center_y-8+16 *   1))
        # screen.blit(graphic_memory[7], (center_x - 8+16 *  2, center_y-8+16 *   1))

        # screen.blit(character_memory[0], (center_x - 8+16 *  -2, center_y-8+16 *   0))
        # screen.blit(character_memory[0], (center_x - 8+16 *  -3, center_y-8+16 *   0))
        # screen.blit(character_memory[0], (center_x - 8+16 *  -1, center_y-8+16 *   0))
        screen.blit(character_memory[0], (center_x - 8+16 *   0, center_y-8+16 *   0))
        # screen.blit(character_memory[2], (center_x - 8+16 *   0, center_y-8+16 *   -1))
        # screen.blit(character_memory[3], (center_x - 8+16 *   1, center_y-8+16 *   0))
        # screen.blit(character_memory[4], (center_x - 8+16 *   2, center_y-8+16 *   0))
        # screen.blit(character_memory[5], (center_x - 8+16 *   3, center_y-8+16 *   0))
        # screen.blit(character_memory[0], (center_x - 8+16 *   4, center_y-8+16 *   0))
        #
        # screen.blit(character_memory[8], (center_x - 8+16 *  -2, center_y-8+16 *   1))
        # screen.blit(character_memory[9], (center_x - 8+16 *  -1, center_y-8+16 *   1))

        # screen.blit(character_memory[1], (center_x - 8, center_y-8)) # 0
        # screen.blit(font_memory[0], (center_x - 4, center_y-4)) # 0
        # screen.blit(small_font_memory[30], (center_x - 8+16 *  -1, center_y - 8+16 *  0)) # 0
        # screen.blit(small_font_memory[13], (center_x - 8+16 *  -3, center_y - 8+16 *  0)) # 0
        # screen.blit(small_font_memory[10], (center_x - 8+16 *  -2, center_y - 8+16 *  1)) # 0
        # screen.blit(small_font_memory[22], (center_x - 8+16 *   4, center_y - 8+16 *  0)) # 0
        screen.blit(small_font_memory[19], (center_x - 8+16 *  0, center_y - 8+16 *  0)) # 0
        # screen.blit(small_font_memory[21], (center_x - 8+16 *  0, center_y - 8+16 *  -1)) # 0
        # screen.blit(small_font_memory[20], (center_x - 8+16 *  -1, center_y - 8+16 *  1)) # 0

        # pygame.draw.circle(screen, WHITE, [center_x, center_y], half_step - 3, 1)
        # pygame.draw.circle(screen, RED, [center_x, center_y], half_step - 1, 1)

        for xi in range (h_steps):
            for yi in range (h_steps):
                pass
                # pygame.draw.circle(screen, WHITE, [half_step+step*xi, half_step+step*yi], half_step - 1, 1)
        # pygame.draw.circle(screen, WHITE, [80+160*1, 80+160*1], 75, 1)
        # pygame.draw.circle(screen, WHITE, [80+160*21, 80+160*9  ], 75, 1)
        # pygame.draw.circle(screen, WHITE, [80+160*1, 80+160*8  ], 75, 1)
        # pygame.draw.circle(screen, WHITE, [160, 160], 75, 1)
        # circle_man(screen,BLACK,[400,320],-math.pi/3)
        # circle_man(screen,RED,[300,320],math.pi/8)
        # timer += 1
        # print timer % 100
        # if (timer % 100) == 0:
        #     print "______________"
        #     # pygame.display.toggle_fullscreen()
        #     screen = pygame.display.set_mode(size)
        # if (timer % 100) == 50:
        #     print "______________"
        #     screen = pygame.display.set_mode(size,pygame.FULLSCREEN)


        pygame.display.flip()

    # this line exits the program
    pygame.quit()

if __name__ == '__main__':
    quit()
    pygame.init()
    # screen = pygame.display.set_mode((1024, 784),pygame.FULLSCREEN)
    screen = pygame.display.set_mode((128, 32))
    screen.fill((255, 255, 255))
    table = load_tile_table("Font.png", 8, 8)
    # table = load_tile_table("land_tiles.png", 16, 16)
    # table = load_tile_table("Overworld.png", 17, 17)
    # table = load_tile_table("Zelda_Overworld.png", 8, 9)
    graphic_memory = {}
    for x, row in enumerate(table):
        for y, tile in enumerate(row):
            # screen.blit(tile, (x*33, y*33))
            graphic_memory[y*16+x] = tile
            # screen.blit(tile, (x*33, y*33))
    # for x, row in enumerate(table):
        # for y, tile in enumerate(row):
    screen.blit(graphic_memory[0], (0, 0)) # 0
    screen.blit(graphic_memory[16], (8, 0)) # 1
    screen.blit(graphic_memory[1], (16, 0)) # 2
    screen.blit(graphic_memory[17], (24, 0)) # 3
    screen.blit(graphic_memory[2], (32, 0)) # 4
    screen.blit(graphic_memory[18], (40, 0)) # 5
    screen.blit(graphic_memory[3], (48, 0)) # 6
    screen.blit(graphic_memory[19], (56, 0)) # 7
    screen.blit(graphic_memory[4], (64, 0)) # 8
    screen.blit(graphic_memory[20], (72, 0)) # 9
    screen.blit(graphic_memory[5], (80, 0)) # A
    screen.blit(graphic_memory[21], (88, 0)) # B
    screen.blit(graphic_memory[6], (96, 0)) # C
    screen.blit(graphic_memory[22], (104, 0)) # D
    screen.blit(graphic_memory[7], (112, 0)) # E
    screen.blit(graphic_memory[23], (120, 0)) # F
    screen.blit(graphic_memory[8], (0, 8)) # G
    screen.blit(graphic_memory[24], (8, 8)) # H
    screen.blit(graphic_memory[9], (16, 8)) # I
    screen.blit(graphic_memory[25], (24, 8)) # J
    screen.blit(graphic_memory[10], (32, 8)) # K
    screen.blit(graphic_memory[26], (40, 8)) # L
    screen.blit(graphic_memory[11], (48, 8)) # M
    screen.blit(graphic_memory[27], (56, 8)) # N
    screen.blit(graphic_memory[12], (64, 8)) # O
    screen.blit(graphic_memory[28], (72, 8)) # P
    screen.blit(graphic_memory[13], (80, 8)) # Q
    screen.blit(graphic_memory[29], (88, 8)) # R
    screen.blit(graphic_memory[14], (96, 8)) # S
    screen.blit(graphic_memory[30], (104, 8)) # T
    screen.blit(graphic_memory[15], (112, 8)) # U
    screen.blit(graphic_memory[31], (120, 8)) # V

    screen.blit(graphic_memory[32], (0, 16)) # W
    screen.blit(graphic_memory[33], (16, 16)) # X
    screen.blit(graphic_memory[48], (8, 16)) # Y
    screen.blit(graphic_memory[49], (24, 16)) # Z
    screen.blit(graphic_memory[52], (32, 16)) # ,
    screen.blit(graphic_memory[53], (40, 16)) # '
    screen.blit(graphic_memory[54], (48, 16)) # "
    screen.blit(graphic_memory[55], (56, 16)) # '
    screen.blit(graphic_memory[56], (64, 16)) #
    screen.blit(graphic_memory[36], (72, 16)) # ,
    screen.blit(graphic_memory[37], (80, 16)) # ,
    screen.blit(graphic_memory[38], (88, 16)) # ,
    screen.blit(graphic_memory[39], (96, 16)) # ,
    screen.blit(graphic_memory[40], (104, 16)) # ,

    pygame.display.flip()
    pygame.image.save(screen,"font_tiles.png")
    while pygame.event.wait().type != pygame.locals.QUIT:
        pass

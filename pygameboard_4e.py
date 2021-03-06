#
import pygame
import math
import pygame.locals
import csv
import random
import sqlite3



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


done = False
clock = pygame.time.Clock()


if __name__ == '__main__':  # single underscore
    # from Database --------------------------------------------------------------------------------------------------------------------------------------------
    conn = sqlite3.connect('dnd_game_4e.sqlite')
    c = conn.cursor()
    world = {}
    c.execute('''CREATE TABLE IF NOT EXISTS map
                 (
                 coordinates text UNIQUE,
                 description text
                 )''')


    # print ("")
    # print ("everything in the table")
    c.execute('SELECT * FROM map')
    conn.commit()
    rows = c.fetchall()
    # print (rows)
    # print ("")



    print pygame.display.Info()
    screen = pygame.display.set_mode(size,
                        # pygame.FULLSCREEN |
                        pygame.DOUBLEBUF
                        )
    print ""
    for location,data in rows:
        # print "location, data",
        x = int(location.split(",")[0])
        y = int(location.split(",")[1])
        # print x,
        # print y,
        # print int(data)
        world[x,y] = int(data)

    # print "world after database", world
    # from CSV --------------------------------------------------------------------------------------------------------------------------------------------
    # csv_filename = "world2.csv"
    # csvfile = open(csv_filename, 'r')
    # reader = csvfile.read()
    # csvfile.close()
    #
    # rows = reader.splitlines()
    #
    # # world = {}
    # row_y = 0
    # for row in rows:
    #     # print row_y, row
    #     row_y += 1
    #     column_x = 0
    #     for column in row.split(","):
    #         # print column_x,column
    #         column_x += 1
    #         world[column_x,row_y] = int(column)
    #         position = (str(column_x)+","+str(row_y),)
    #         terrain = (column,)
    #         c.execute("REPLACE INTO map VALUES (?,?)", (position[0],terrain[0],) )
    #         conn.commit()
    #
    #

    # load visuals  --------------------------------------------------------------------------------------------------------------------------------------------

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
    print "small_font_memory loaded", len(small_font_memory), "sprites."


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
    screen.fill(GREEN)
    screen.fill(BLACK)
    timer = 0
    keys = pygame.key.get_pressed()
    game_location = (random.randint(0,3),random.randint(0,3))
    game_location = (1,4)

    # print "world after csv", world

    # visualize  --------------------------------------------------------------------------------------------------------------------------------------------
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
        if keys[pygame.K_UP] and not prior_key_states[pygame.K_UP]:
            game_location = (game_location[0] , game_location[1]-1)
        if keys[pygame.K_DOWN] and not prior_key_states[pygame.K_DOWN]:
            game_location = (game_location[0] , game_location[1]+1)
        if keys[pygame.K_LEFT] and not prior_key_states[pygame.K_LEFT]:
            game_location = (game_location[0] -1, game_location[1])
        if keys[pygame.K_RIGHT] and not prior_key_states[pygame.K_RIGHT]:
            game_location = (game_location[0] +1, game_location[1])
        if keys[pygame.K_d] and not prior_key_states[pygame.K_d]:
            position = (str(game_location[0])+","+str(game_location[1]),)
            print position
            c.execute("DELETE FROM map WHERE coordinates=?", position)
            try:
                del world[game_location]
            except:
                pass
            conn.commit()
        if keys[pygame.K_SPACE] and not prior_key_states[pygame.K_SPACE]:
            position = (str(game_location[0])+","+str(game_location[1]),)
            if keys[pygame.K_RSHIFT] or keys[pygame.K_LSHIFT]:
                try:
                    world[game_location] -= 1
                except:
                    world[game_location] = 196
            else:
                try:
                    world[game_location] += 1
                except:
                    world[game_location] = 196
            terrain = (world[game_location],)
            print position
            c.execute("REPLACE INTO map VALUES (?,?)", (position[0],terrain[0],) )
            conn.commit()

        xi = 0
        yi = 0
        # my_location_x, my_location_y = (10,10)
        # bad_guy_location_x, bad_guy_location_y = (8,12)
        center_x = pygame.display.get_surface().get_size()[0]/2
        center_y = pygame.display.get_surface().get_size()[1]/2
        screen.blit(graphic_memory[7], (-8, -8)) # 0
        vision = 10
        for x in range(-vision,vision+1):
            for y in range(-vision,vision+1):
                try:
                    location = (game_location[0] + x,game_location[1] + y)
                    # print "location",location, world[location]
                    image = graphic_memory[world[location]]
                except:
                    image = graphic_memory[30*14+7]
                screen.blit(image, (center_x - 8+16 *  x, center_y-8+16 *  y))

        screen.blit(character_memory[6], (center_x - 8+16 *   0, center_y-8+16 *   0))
        screen.blit(small_font_memory[19], (center_x - 8+16 *  0, center_y - 8+16 *  0)) # 0

        pygame.display.flip()

    pygame.quit()

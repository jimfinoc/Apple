#
import pygame
import math
import pygame.locals
import csv
import random
import sqlite3
import socket
import sys
import time
import pickle
import bz2
import argparse
import SocketServer, threading, time


parser = argparse.ArgumentParser(description='This allows you to run pygameboard.')
parser.add_argument('-i', '--initial', type=str, default='0')
parser.add_argument('-t', '--token', type=int, choices=xrange(0,8),default=6)
parser.add_argument('-f', '--fullscreen', type=bool, choices=[True,False],default=False)
parser.add_argument('-r', '--role', type=str, choices=['server','client','npc'], default='client')
args = parser.parse_args()
initial_dict = {
    "0":0,
    "1":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "A":10,
    "B":11,
    "C":12,
    "D":13,
    "E":14,
    "F":15,
    "G":16,
    "H":17,
    "I":18,
    "J":19,
    "K":20,
    "L":21,
    "M":22,
    "N":23,
    "O":24,
    "P":25,
    "Q":26,
    "R":27,
    "S":28,
    "T":29,
    "U":30,
    "V":31,
    "W":32,
    "X":33,
    "Y":34,
    "Z":35,
    "#":36,
    # "!":36,
    # "&":37,
    # '"':38,
    # "-":39,
    # " ":40,
    # ",":41,
    # "'":42,
    # ".":43,
    # "?":43,
    }
mycharacter_token = args.token
mycharacter_initial = initial_dict[args.initial.upper()]

print "args"
print ".initial", args.initial
print ".token", args.token
print ".fullscreen", args.fullscreen
print ".role", args.role

HOST = socket.gethostbyname('j-macbookpro.local')
HOST_PORT = 10996
CLIENT_PORT = 10997



pygame.init()
pygame.display.set_caption('pygame board '+str(args.role))

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

my_character_details = {}
my_command = {}
characters = {}
world = {}
stuff = {}


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

def push_to_client():
    global world
    global stuff
    global characters
    global my_command
    global my_character_details
    print "==push_to_clients at port", CLIENT_PORT
    data = {}
    data["world"] = world
    data["stuff"] = stuff
    data["characters"] = characters
    # print "sending client uncompressed unpickled data", data
    send_data = pickle.dumps(data)
    compressed_send_data = bz2.compress(send_data)
    # print "characters", characters
    for each in characters:
        if each == "server":
            # print "don't send to the server"
            pass
        else:
            print "send to client"
            print each
            sock.sendto(compressed_send_data, (each, CLIENT_PORT))
    print "done sending to clients"
    print ""


def push_to_server():
    global world
    global stuff
    global characters
    global my_command
    global my_character_details
    print "==push_to_server to ", HOST, "at port", HOST_PORT
    data = {}
    data["client_character"] = my_character_details
    data["client_command"] = my_command

    # print "sending client uncompressed unpickled data", data
    send_data = pickle.dumps(data)
    # print "send_data", send_data
    compressed_send_data = bz2.compress(send_data)
    # print "compressed_send_data",compressed_send_data
    # print "sending client compressed pickled", compressed_send_data
    sock.sendto(compressed_send_data, (HOST, HOST_PORT))



class ThreadedUDPRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        global world
        global stuff
        global characters
        global my_command
        global my_character_details
        received_data = self.request[0]
        socket = self.request[1]
        uncompressed_received_data = bz2.decompress(received_data)
        unpickled_uncompressed_received_data = pickle.loads(uncompressed_received_data)
        # print "received", unpickled_uncompressed_received_data
        current_thread = threading.current_thread()
        # print("{}: client: {}, wrote: {}".format(current_thread.name, self.client_address, received_data))
        # print "client_address", self.client_address[1]

        # print "the characters are", characters
        if args.role == 'server':
            try:
                timer = time.time()
                # print "got time of", timer
                # print unpickled_uncompressed_received_data["client_character"]
                # visitor = str(self.client_address[0])+","+str(self.client_address[1])
                # print "ipaddress is", self.client_address[0]
                # print "visitor", visitor

                characters[self.client_address[0]] = unpickled_uncompressed_received_data["client_character"]
                characters[self.client_address[0]]["time"] = timer
                # characters[visitor] = unpickled_uncompressed_received_data["client_character"]
                # characters[visitor]["time"] = timer
                # print "client_address", client_address[0]
                CLIENT[client_address[0]] = timer
            except:
                print "error with ThreadedUDPRequestHandler server role"
        if args.role == 'client':
            try:
                world = unpickled_uncompressed_received_data['world']
                characters = unpickled_uncompressed_received_data['characters']
                # print "received world", world
                # print "received characters", characters
            except:
                pass
        # characters[]

        # print "received_data", received_data
        # print("{}: client: {}, wrote: {}".format(current_thread.name, self.client_address, received_data))
        # socket.sendto(data.upper(), self.client_address)
        # print "world",world
        # data = {}
        # data["world"] = world
        # data["stuff"] = stuff
        # data["characters"] = characters
        # data["characters"][time.time()]
        # print "getting ready to send: ",data

        # print "client_command", unpickled_uncompressed_received_data["client_command"]
        # if "delete" in unpickled_uncompressed_received_data["client_command"].keys():
            # print "deleting", unpickled_uncompressed_received_data["client_command"]["delete"]

        # send_data = pickle.dumps(data)
        # compressed_send_data = bz2.compress(send_data)
        # print "send_data",len(compressed_send_data)
        # socket.sendto(compressed_send_data, self.client_address)

class ThreadedUDPServer(SocketServer.ThreadingMixIn, SocketServer.UDPServer):
    print "ThreadedUDPServer started"
    pass



done = False
clock = pygame.time.Clock()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if __name__ == '__main__':  # single underscore
    # from Database --------------------------------------------------------------------------------------------------------------------------------------------
    # conn = sqlite3.connect('dnd_game_4e.sqlite')
    # c = conn.cursor()
    # c.execute('''CREATE TABLE IF NOT EXISTS map
    #              (
    #              coordinates text UNIQUE,
    #              description text
    #              )''')
    print args.role
    if args.role == 'server':
        print "starting server server"
        print "Host", HOST
        print "Port", HOST_PORT
        server = ThreadedUDPServer((HOST, HOST_PORT), ThreadedUDPRequestHandler)
        print "server server should be started"
        PORT = HOST_PORT
    if args.role == 'client':
        print "starting client server"
        server = ThreadedUDPServer((socket.gethostbyname(socket.gethostname()), CLIENT_PORT), ThreadedUDPRequestHandler)
        print "client server should be started"
        PORT = CLIENT_PORT


    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True

    try:
        server_thread.start()
        print("Server started at {} port {}".format(HOST, PORT))
    except (KeyboardInterrupt, SystemExit):
        server.shutdown()
        server.server_close()
        exit()


    if args.role == 'server':
        conn = sqlite3.connect('dnd_game_4e.sqlite')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS map
                     (
                     coordinates text UNIQUE,
                     description text
                     )''')
        c.execute('SELECT * FROM map')
        conn.commit()
        rows = c.fetchall()
        for location,data in rows:
            x = int(location.split(",")[0])
            y = int(location.split(",")[1])
            print int(data)
            world[x,y] = int(data)



    print pygame.display.Info()
    if args.fullscreen == True:
        screen = pygame.display.set_mode(size,
                        pygame.FULLSCREEN |
                        pygame.DOUBLEBUF
                        )
    else:
        screen = pygame.display.set_mode(size,
                        pygame.DOUBLEBUF
                        )
    if args.role == 'client':
        push_to_server()
    if args.role == 'server':
        push_to_client()
    # print "communicate_with_server"
    # communicate_with_server()
    # try:
    # print "sending to ", HOST, "at port", PORT
    # sock.sendto("2" + "\n", (HOST, PORT))
    # received_data = sock.recv(4096)
    # print received_data
    # uncompressed_received_data = bz2.decompress(received_data)
    # unpickled_uncompressed_received_data = pickle.loads(uncompressed_received_data)
    # try:
    #     world = unpickled_uncompressed_received_data["world"]
    #     print "world loaded"
    # except:
    #     world = {}
    #     print "world not loaded"
    # try:
    #     stuff = unpickled_uncompressed_received_data["stuff"]
    # except:
    #     stuff = {}
    # try:
    #     characters = unpickled_uncompressed_received_data["characters"]
    # except:
    #     characters = {}
    #
    # print world

    # except:
        # pass
    # for location,data in rows:
    #     # print "location, data",
    #     x = int(location.split(",")[0])
    #     y = int(location.split(",")[1])
    #     # print x,
    #     # print y,
    #     # print int(data)
    #     world[x,y] = int(data)

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

    # land_tiles = load_tile_table("land_tiles.png", 16, 16)
    land_tiles = load_tile_table("terrain4.png", 16, 16)
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
    h_steps = pygame.display.get_surface().get_size()[0] / step
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
        print "_______________begin_______________"

        # sock.sendto("2" + "\n", (HOST, PORT))
        # received_data = sock.recv(4096)
        # print received_data
        # uncompressed_received_data = bz2.decompress(received_data)
        # unpickled_uncompressed_received_data = pickle.loads(uncompressed_received_data)
        # world = unpickled_uncompressed_received_data
        # data = communicate_with_server()
        # world = data["world"]
        # characters = data["characters"]
        if args.role == 'server':
            push_to_client()
        if args.role == 'client':
            push_to_server()


        # print world
        # stuff = unpickled_uncompressed_received_data["stuff"]
        # characters = unpickled_uncompressed_received_data["characters"]

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
            # print position
            # c.execute("DELETE FROM map WHERE coordinates=?", position)
            my_command["delete"] = game_location

            try:
                pass
                # del world[game_location]
            except:
                pass
            # conn.commit()
        if keys[pygame.K_SPACE] and not prior_key_states[pygame.K_SPACE]:
            position = (str(game_location[0])+","+str(game_location[1]),)
            if keys[pygame.K_RSHIFT] or keys[pygame.K_LSHIFT]:
                try:
                    world[game_location] -= 1
                except:
                    world[game_location] = 0
            else:
                try:
                    world[game_location] += 1
                except:
                    world[game_location] = 0
            terrain = (world[game_location],)
            # print position
            # c.execute("REPLACE INTO map VALUES (?,?)", (position[0],terrain[0],) )
            # conn.commit()

        xi = 0
        yi = 0
        # my_location_x, my_location_y = (10,10)
        # bad_guy_location_x, bad_guy_location_y = (8,12)
        center_x = pygame.display.get_surface().get_size()[0]/2
        center_y = pygame.display.get_surface().get_size()[1]/2
        screen.blit(graphic_memory[7], (-8, -8)) # 0
        vision = 6
        for x in range(-vision,vision+1):
            for y in range(-vision,vision+1):
                try:
                    location = (game_location[0] + x,game_location[1] + y)
                    # print "location",location, world[location]
                    image = graphic_memory[world[location]]
                except:
                    # image = graphic_memory[30*14+7]
                    image = graphic_memory[0]
                screen.blit(image, (center_x - 8+16 *  x, center_y-8+16 *  y))

        # drawing characters from server
        print "characters",characters
        remove_entry = False
        for each_key in characters:
            try:
                print "one at a time"
                print each_key
                print characters[each_key]
                if ( args.role == "server" ) and ( characters[each_key]["time"] + 5 < time.time() ):
                    remove_entry = each_key
                some_location = characters[each_key]["location"]
                some_char_token = characters[each_key]["char_token"]
                some_font_memory = characters[each_key]["char_initial"]
                print "my location",game_location
                print "some location",some_location
                my_character_details["location"] = game_location
                my_character_details["char_token"] = mycharacter_token
                my_character_details["char_initial"] = mycharacter_initial
                # image = character_memory[world[location]]
                if abs(some_location[0]-game_location[0]) <= vision:
                    screen.blit(character_memory[some_char_token], (center_x - 8+16 * (some_location[0]-game_location[0]), center_y - 8+16 * (some_location[1]-game_location[1])))
                    screen.blit(small_font_memory[some_font_memory], (center_x - 8+16 * (some_location[0]-game_location[0]), center_y - 8+16 * (some_location[1]-game_location[1])))
            except:
                pass
            # screen.blit(small_font_memory[some_font_memory], (some_location[0]- 8+16, some_location[1]- 8+16))
        # drawing my character
        screen.blit(character_memory[mycharacter_token], (center_x - 8+16 *   0, center_y-8+16 *   0))
        screen.blit(small_font_memory[mycharacter_initial], (center_x - 8+16 *  0, center_y - 8+16 *  0)) # 0
        if args.role == "client":
            my_character_details["location"] = game_location
            my_character_details["char_token"] = mycharacter_token
            my_character_details["char_initial"] = mycharacter_initial
            # my_character_details["address"]

        if args.role == "server":
            if remove_entry:
                try:
                    characters.pop(remove_entry)
                except:
                    pass
            characters["server"] = {}
            characters["server"]["location"] = game_location
            # print "game location",game_location
            characters["server"]["char_token"] = mycharacter_token
            characters["server"]["char_initial"] = mycharacter_initial
            characters["server"]["time"] = time.time()
        pygame.display.flip()

    pygame.quit()

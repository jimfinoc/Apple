#!/usr/bin/python
import math
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
import pprint

parser = argparse.ArgumentParser(description='This allows you to run pygameboard.')
parser.add_argument('-i', '--initial', type=str, default='0')
parser.add_argument('-t', '--token', type=int, choices=xrange(0,8),default=6)
parser.add_argument('-f', '--fullscreen', type=str, choices=["yes","no"],default="no")
parser.add_argument('-r', '--role', type=str, choices=['server','client','server_daemon'], default='client')
args = parser.parse_args()

if args.role != 'server_daemon':
    import pygame
    import pygame.locals

myrandomseed = random.uniform(0,10000000)

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

# print "args"
# print ".initial", args.initial
# print ".token", args.token
# print ".fullscreen", args.fullscreen
# print ".role", args.role

# HOST = socket.gethostbyname('j-macbookpro.local')
HOST = socket.gethostbyname('gameserver.local')
hostname = socket.gethostname()
CLIENT = socket.gethostbyname(hostname)

HOST_PORT = 10996
CLIENT_PORT = 10997
NPC_PORT = 10998


if args.role != 'server_daemon':
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
big_characters = {}
little_characters = {}
big_world = {}
little_world = {}
stuff = {}
time_check = 0.5


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
    global big_world
    global stuff
    global big_characters
    global my_command
    global my_character_details
    # print "=big push_to_clients at port", CLIENT_PORT
    data = {}
    # data["world"] = world
    # data["stuff"] = stuff

    data["characters"] = dict(big_characters)
    # print "sending client uncompressed unpickled data", data
    # print "big_characters", big_characters
    # print "big_characters"
    # print big_characters
    # print ""
    for each in data["characters"]:
        # print "==push_to_client"
        # print each,
        # print type(each),

        # print data["characters"][each]
        small_square = []
        try:
            push_location = big_characters[each]["location"]
            # print "push_location"
            # print push_location
            # print type(push_location)
            look  = 15
            # print look
            for x in range(-look,look+1):
                # print x
                for y in range(-look,look+1):
                    # print push_location[0]+x
                    # print push_location[1]+y
                    small_square.append( (push_location[0]+x , push_location[1]+y))
            # print small_square
        except:
            small_square.append( (0,0) )


        sliceofthe_world = dict((k, big_world[k]) for k in small_square if k in big_world)
        # print small_world
        data["world"] = sliceofthe_world
        send_data = pickle.dumps(data)
        compressed_send_data = bz2.compress(send_data)
        sock.sendto(compressed_send_data, (data["characters"][each]["IP"], CLIENT_PORT))
    # print "done sending to clients"
    # print ""

def push_to_npc():
    global big_world
    global stuff
    global big_characters
    global my_command
    global my_character_details
    data = {}

def push_to_server():
    global my_command
    global my_character_details
    # print "==push_to_server to ", HOST, "at port", HOST_PORT
    data = {}
    data["client_character"] = my_character_details
    data["client_command"] = my_command

    # print "sending client uncompressed unpickled data", data
    send_data = pickle.dumps(data)
    # print "my_command", my_command
    if my_command:
        my_command.pop(my_command.keys()[0])
    # print "send_data", send_data
    compressed_send_data = bz2.compress(send_data)
    # print "compressed_send_data",compressed_send_data
    # print "sending data to", (HOST, HOST_PORT)
    sock.sendto(compressed_send_data, (HOST, HOST_PORT))




class ThreadedUDPRequestHandlerForServer(SocketServer.BaseRequestHandler):
    def handle(self):
        # print "-ThreadedUDPRequestHandlerForServer"
        global big_world
        global stuff
        global big_characters
        conn = sqlite3.connect('dnd_game_4e.sqlite')
        c = conn.cursor()
        received_data = self.request[0]
        socket = self.request[1]
        uncompressed_received_data = bz2.decompress(received_data)
        unpickled_uncompressed_received_data = pickle.loads(uncompressed_received_data)
        data = unpickled_uncompressed_received_data
        current_thread = threading.current_thread()
        # live character check
        remove_entry = False
        for each_key in big_characters:
            if big_characters[each_key]["time"] + 5 < time.time():
                remove_entry = each_key
                # print "should pop"
        if remove_entry:
            try:
            # if 1==1:
                # print "trying to pop"
                big_characters.pop(remove_entry)
                print "removing guest", remove_entry,"at", time.ctime()
                # print "should have popped"
            except:
                # print "couldn't pop"
                pass
        try:
            client_IPaddress = self.client_address[0]
            timer = time.time()
            # print "got time of", timer
            # print unpickled_uncompressed_received_data["client_character"]
            visitor = str(client_IPaddress)+","+str(self.client_address[1])
            # print ""
            # print "--ipaddress is", client_IPaddress
            # print "--visitor", visitor
            # print "--Adding or updating character from client"
            # print ""
            if visitor in big_characters.keys():
                pass
            else:
                print "new guest," ,visitor, "," " from", client_IPaddress, "at", time.ctime()
            big_characters[visitor] = data["client_character"]
            big_characters[visitor]["time"] = timer
            big_characters[visitor]["IP"] = client_IPaddress
            # print "data",
            # print data
            # print ""
            command = data["client_command"]
            # print "command",
            # print command
            if command:
                if "delete" in command.keys():
                    try:
                        location_removal = command["delete"]
                        position = (str(location_removal[0])+","+str(location_removal[1]),)
                        del big_world[location_removal]
                        c.execute("DELETE FROM map WHERE coordinates=?", position)
                        conn.commit()
                    except:
                        print "error in command delete"
                if "set_tile" in command.keys():
                    try:
                        set_to = command["set_tile"]["value"]
                        location_set = command["set_tile"]["location"]
                        position = (str(location_set[0])+","+str(location_set[1]),)
                        big_world[location_set] = set_to
                        # print "big_world[location_set] = set_to"
                        # print "big_world[location_set] =",
                        # print set_to
                        # print "working_position"
                        # print position
                        # print type(position)
                        # terrain = set_to
                        # print "terrain"
                        # print terrain
                        if len(set_to) == 1:
                            terrain = (str(set_to[0])+",",)
                            print terrain
                        if len(set_to) == 2:
                            terrain = (str(set_to[0])+","+str(set_to[1]),)
                            print terrain
                        # print terrain
                        # print type(terrain)

                        c.execute("REPLACE INTO map VALUES (?,?)", (position[0],terrain[0],) )
                        conn.commit()
                    except:
                        print "error in command set_tile"

            # big_characters[visitor] = unpickled_uncompressed_received_data["client_character"]
            # big_characters[visitor]["time"] = timer
            # print "client_address", client_address[0]
            # CLIENT[client_address[0]] = timer
        except:
            print ""
            print "error with ThreadedUDPRequestHandlerForServer server role"
            print self.client_address[0]
            print self.client_address[1]
            print "Should you check this out?"
            print ""

class ThreadedUDPRequestHandlerForNPCs(SocketServer.BaseRequestHandler):
    def handle(self):
        # global little_world
        global big_characters
        # global stuff
        # global little_characters
        # global my_command
        # global my_character_details
        received_data = self.request[0]
        socket = self.request[1]
        uncompressed_received_data = bz2.decompress(received_data)
        unpickled_uncompressed_received_data = pickle.loads(uncompressed_received_data)
        data = unpickled_uncompressed_received_data
        current_thread = threading.current_thread()
        # if args.role == 'client':
        client_IPaddress = self.client_address[0]

        try:
            pass
            # print data
            # print "trying to receive a slice of the world"
            # little_world = unpickled_uncompressed_received_data['world']
            # little_characters = unpickled_uncompressed_received_data['characters']
            # print "received world", little_world
            # print "received little_characters", little_characters
        except:
            print ""
            print "error with ThreadedUDPRequestHandlerForNPCs server role"
            print self.client_address[0]
            print self.client_address[1]
            print "Do you hear what I hear?"
            print ""
        try:
            pass
            for each in data:
                # print "this is each"
                # print each
                timer = time.time()
                big_characters[client_IPaddress+","+each] = data[each]
                big_characters[client_IPaddress+","+each]["time"] = timer
                big_characters[client_IPaddress+","+each]["IP"] = client_IPaddress

        except:
            print "something went wrong with the NPC"
        # pp = pprint.PrettyPrinter(indent=4)
        # print "NPC data"
        # pp.pprint(data)
        # print ""
        # print "big_characters"
        # pp.pprint(big_characters)

class ThreadedUDPRequestHandlerForClient(SocketServer.BaseRequestHandler):
    def handle(self):
        global little_world
        global stuff
        global little_characters
        global my_command
        global my_character_details
        received_data = self.request[0]
        socket = self.request[1]
        uncompressed_received_data = bz2.decompress(received_data)
        unpickled_uncompressed_received_data = pickle.loads(uncompressed_received_data)
        data = unpickled_uncompressed_received_data
        current_thread = threading.current_thread()
        # if args.role == 'client':
        try:
            # print "trying to receive a slice of the world"
            little_world = dict( little_world.items() + unpickled_uncompressed_received_data['world'].items() )
            # little_world = unpickled_uncompressed_received_data['world']
            little_characters = unpickled_uncompressed_received_data['characters']
            # print "received world", little_world
            # print "received little_characters", little_characters
        except:
            print ""
            print "error with ThreadedUDPRequestHandlerForClient server role"
            print self.client_address[0]
            print self.client_address[1]
            print "What is going on?"
            print ""


class ThreadedUDPServer(SocketServer.ThreadingMixIn, SocketServer.UDPServer):
    print "ThreadedUDPServer started"
    pass



done = False
if args.role != 'server_daemon':
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
    if args.role == 'server' or args.role == 'server_daemon':
        print ""
        print "starting host server"
        serverS = ThreadedUDPServer(("", HOST_PORT), ThreadedUDPRequestHandlerForServer)
        print "server server should be started"
        server_threadS = threading.Thread(target=serverS.serve_forever)
        server_threadS.daemon = True
        try:
            server_threadS.start()
            print("Server started at {} port {}".format(HOST, HOST_PORT))
        except (KeyboardInterrupt, SystemExit):
            serverS.shutdown()
            serverS.server_close()
            exit()

    if args.role == 'server' or args.role == 'server_daemon':
        print ""
        print "starting NPC server"
        serverN = ThreadedUDPServer(("", NPC_PORT), ThreadedUDPRequestHandlerForNPCs)
        print "server server should be started"
        server_threadN = threading.Thread(target=serverN.serve_forever)
        server_threadN.daemon = True
        try:
            server_threadN.start()
            print("Server started at {} port {}".format(HOST, NPC_PORT))
        except (KeyboardInterrupt, SystemExit):
            serverN.shutdown()
            serverN.server_close()
            exit()
    if args.role != 'server_daemon':
        print ""
        print "starting client server"
        serverC = ThreadedUDPServer(("", CLIENT_PORT), ThreadedUDPRequestHandlerForClient)
        print "client server should be started"
        server_threadC = threading.Thread(target=serverC.serve_forever)
        server_threadC.daemon = True
        try:
            server_threadC.start()
            print("Server started at {} port {}".format(CLIENT, CLIENT_PORT))
        except (KeyboardInterrupt, SystemExit):
            serverC.shutdown()
            serverC.server_close()
            exit()

    if args.role == 'server' or args.role == 'server_daemon':
        print "loading"
        # global conn
        # global c
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
            splitdata = data.split(",")
            if len(splitdata) == 1:
                big_world[x,y] = (int(data),)
            if len(splitdata) == 2:
                terrain = int(splitdata[0].replace('(', ''))
                object = splitdata[1].replace(')', '')
                if object == "":
                    big_world[x,y] = (terrain,)
                else:
                    big_world[x,y] = (terrain,int(object))


    print ""
    print "pygame.display.Info() ::"
    if args.role != 'server_daemon':
        print pygame.display.Info()
        if args.fullscreen.lower() == "yes":
            screen = pygame.display.set_mode(size,
                            pygame.FULLSCREEN |
                            pygame.DOUBLEBUF
                            )
        else: screen = pygame.display.set_mode(size,pygame.DOUBLEBUF)
    if args.role != 'server_daemon': #server and client push data to server
        push_to_server()
    if args.role == 'server' or args.role == 'server_daemon': #only client does not push to client
        push_to_client()


    # load visuals  --------------------------------------------------------------------------------------------------------------------------------------------

    if args.role != 'server_daemon':
        keys = pygame.key.get_pressed()
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

        object_tiles = load_tile_table("object_tiles.png",16,16)
        object_memory = {}
        for x, row in enumerate(object_tiles):
            for y, tile in enumerate(row):
                object_memory[y*8+x] = tile
        print "object_memory loaded", len(object_memory), "sprites."


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
        game_location = (random.randint(0,3),random.randint(0,3))
        # game_location = (0,0) #starting location


    # visualize  --------------------------------------------------------------------------------------------------------------------------------------------
    if args.role != 'server_daemon':
        last_edit = (2,)
        mouse_object_lookup = {}
        mouse_terrain_lookup = {}
        first_pass = True
        mouse_buttons = (0,0,0)
        mouse_position = (0,0)

    # print "press q to quit"
    joystick_connected = False
    pygame.joystick.init()
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    print joysticks
    if len(joysticks) > 0:
        joystick_connected = joysticks[0]
    for each_joystick in joysticks:
        each_joystick.init()
        print "joystick name", each_joystick.get_name()
        print "axes",each_joystick.get_numaxes()
        print "buttons", each_joystick.get_numbuttons()
        print "hats", each_joystick.get_numhats()

    print "joystick_connected",
    print joystick_connected

    last_look_time = 0

    while not done:
        # print "_______________begin_______________"
        if args.role == 'server' or args.role == 'server_daemon':
            push_to_client()
        if args.role == 'client' or args.role == 'server':
            push_to_server()

        if args.role != 'server_daemon':
            clock.tick(10)
        else:
            time.sleep(.25)

        if args.role != 'server_daemon':
            prior_key_states = keys
            keys = pygame.key.get_pressed()

        # if args.role == 'server_daemon':
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             done = True
        #     if keys[pygame.K_q] and not prior_key_states[pygame.K_q]:
        #         done = True

        if args.role != 'server_daemon':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            if 1==1: #indent for keys
                move = [0,0]
                if keys[pygame.K_q] and not prior_key_states[pygame.K_q]:
                    done = True
                if keys[pygame.K_c] and not prior_key_states[pygame.K_c]:
                    last_edit = (last_edit[0],)
                # if keys[pygame.K_UP] and not prior_key_states[pygame.K_UP]:
                if keys[pygame.K_UP] and (time.time() - last_look_time > time_check):
                    move[1] -= 1
                    # last_look_time = time.time()
                    # game_location = (game_location[0] , game_location[1]-1)
                # if keys[pygame.K_DOWN] and not prior_key_states[pygame.K_DOWN]:
                if keys[pygame.K_DOWN] and (time.time() - last_look_time > time_check):
                    move[1] += 1
                    # last_look_time = time.time()
                    # game_location = (game_location[0] , game_location[1]+1)
                # if keys[pygame.K_LEFT] and not prior_key_states[pygame.K_LEFT]:
                if keys[pygame.K_LEFT] and (time.time() - last_look_time > time_check):
                    move[0] -= 1
                    # last_look_time = time.time()
                    # game_location = (game_location[0] -1, game_location[1])
                # if keys[pygame.K_RIGHT] and not prior_key_states[pygame.K_RIGHT]:
                if keys[pygame.K_RIGHT] and (time.time() - last_look_time > time_check):
                    move[0] += 1
                    # last_look_time = time.time()
                    # game_location = (game_location[0] +1, game_location[1])
                if keys[pygame.K_d] and not prior_key_states[pygame.K_d]:
                    position = (str(game_location[0])+","+str(game_location[1]),)
                    my_command["delete"] = game_location
                if keys[pygame.K_SPACE] and not prior_key_states[pygame.K_SPACE]:
                    position = (str(game_location[0])+","+str(game_location[1]),)
                    try:
                        print "000"
                        little_world[game_location] = (last_edit[0],last_edit[1])
                    except:
                        little_world[game_location] = (last_edit[0],)
                    print "little_world[game_location]",
                    print little_world[game_location]
                    print "type(little_world[game_location])"
                    print type(little_world[game_location])
                    terrain = 0
                    #---------------------------check before writing to database
                    if type(little_world[game_location]) is tuple:
                        print "111"
                        print "tuple check"
                        if len (little_world[game_location]) == 1:
                            terrain = (str(little_world[game_location][0]),)
                            print "terrain in check 1"

                        print "tuple check 2"
                        if len (little_world[game_location]) == 2:
                            print "222"
                            terrain = (str(little_world[game_location][0])+","+str(little_world[game_location][1]),)
                            print "terrain in check 2"

                    elif type(little_world[game_location]) is int:
                        print "int check"
                        terrain = (str(little_world[game_location][0]),)
                        # terrain = (little_world[game_location],)
                    # print position
                    # if args.role == "server":
                    #     print "333"
                    #     print "trying to modify"
                    #     print "terrain",
                    #     print terrain
                    #     print "type(terrain)"
                    #     print type(terrain)
                    #     print "terrain[0]",
                    #     print terrain[0]
                    #     c.execute("REPLACE INTO map VALUES (?,?)", (position[0],terrain[0],) )
                    #     conn.commit()
                    # if args.role == "client":
                    my_command["set_tile"] = {}
                    my_command["set_tile"]["value"] = little_world[game_location]
                    my_command["set_tile"]["location"] = game_location

                if [0,0] != move:
                    last_look_time = time.time()
                    game_location = (game_location[0] + move[0], game_location[1] + move[1])



            if (joystick_connected) and (time.time() - last_look_time > time_check):
                for button_number in range( joystick_connected.get_numbuttons() ):
                    if joystick_connected.get_button(button_number):
                        print "button_number",
                        print button_number
                for axes_number in range( joystick_connected.get_numaxes() ):
                    if joystick_connected.get_axis(axes_number):
                        pass
                        # print "axes_number",
                        # print axes_number
                for hats_number in range( joystick_connected.get_numhats() ):
                    if joystick_connected.get_axis(hats_number):
                        pass
                        # print "hats_number",
                        # print hats_number
                        # print joystick_connected.get_hat(hats_number)
                        hat = joystick_connected.get_hat(hats_number)
                        if (0,0) != hat:
                            last_look_time = time.time()

                        if hat[1] > 0:
                            game_location = (game_location[0] , game_location[1]-1)
                        elif hat[1] < 0:
                            game_location = (game_location[0] , game_location[1]+1)
                        if hat[0] > 0:
                            game_location = (game_location[0] +1, game_location[1])
                        elif hat[0] < 0:
                            game_location = (game_location[0] -1, game_location[1])




            xi = 0
            yi = 0
            # my_location_x, my_location_y = (10,10)
            # bad_guy_location_x, bad_guy_location_y = (8,12)
            center_x = pygame.display.get_surface().get_size()[0]/2
            center_y = pygame.display.get_surface().get_size()[1]/2
            # screen.blit(graphic_memory[7], (-8, -8)) # 0
            vision = 10
            for x in range(-vision,vision+1):
                for y in range(-vision,vision+1):
                    object_image = False
                    location = (game_location[0] + x,game_location[1] + y)
                    # print type (location)
                    # print type (little_world[location])
                    if location in little_world.keys():
                        if type(little_world[location]) is int:
                            # print "+++int check for image2"
                            # print little_world[location]
                            terrain_image = graphic_memory[little_world[location]]
                        if type(little_world[location]) is tuple:
                            # print little_world[location]
                            # print little_world[location][0]
                            terrain_image = graphic_memory[little_world[location][0]]
                            # print "+++tuple check for image2"
                            # print little_world[location][0]
                            if len (little_world[location]) == 2:
                                # print little_world[location][1]
                                object_image = object_memory[little_world[location][1]]
                            else:
                                object_image = False
                    else:
                        terrain_image = graphic_memory[0]
                        object_image = False
                    screen.blit(terrain_image, (center_x - 8+16 *  x, center_y-8+16 *  y))
                    if object_image:
                        screen.blit(object_image, (center_x - 8+16 *  x, center_y-8+16 *  y))

            bigX = 8
            spacing = 16 + 2
            startX = 550
            startY = 50
            object_offset = 140
            for xi in range(0,bigX):
                for yi in range(0,7):
                    screen.blit(graphic_memory[xi + yi * bigX], (startX + xi *spacing,startY + yi *spacing))
                    if first_pass:
                        mouse_terrain_lookup[xi + yi * bigX] =  (startX + xi *spacing, startY + yi *spacing, startX + xi *spacing + 16, startY + yi *spacing+ 16)
                    # screen.blit(graphic_memory[0], (600 , 100))
            # if first_pass:
                # print "little_world",little_world
            if 1==1: #indent for mouse
                if pygame.mouse.get_focused():
                    mouse_buttons = pygame.mouse.get_pressed()
                    mouse_position = pygame.mouse.get_pos()
                # print "mouse_buttons",
                # print mouse_buttons
                # print "mouse_position",
                # print mouse_position
                if mouse_buttons[0]:
                    for each in mouse_terrain_lookup:
                        if (mouse_position[0] > mouse_terrain_lookup[each][0]) and (mouse_position[0] < mouse_terrain_lookup[each][2]) and (mouse_position[1] > mouse_terrain_lookup[each][1]) and (mouse_position[1] < mouse_terrain_lookup[each][3]):
                           last_edit = (each,)
                           print "last_edit",
                           print  last_edit

                for xi in range(0,bigX):
                    for yi in range(0,5):
                        screen.blit(object_memory[xi + yi * bigX], (startX + xi *spacing, startY + object_offset + yi *spacing))
                        if first_pass:
                            mouse_object_lookup[xi + yi * bigX] =  (startX + xi *spacing, startY + object_offset + yi *spacing , startX + xi *spacing + 16, startY + object_offset + yi * spacing + 16 )

                if mouse_buttons[0]:
                    for each in mouse_object_lookup:
                        if (mouse_position[0] > mouse_object_lookup[each][0]) and (mouse_position[0] < mouse_object_lookup[each][2]) and (mouse_position[1] > mouse_object_lookup[each][1]) and (mouse_position[1] < mouse_object_lookup[each][3]):
                           last_edit = (last_edit[0],each)
                           print "checking objects"
                           print last_edit
            # if first_pass:
                # print "mouse_terrain_lookup",
                # print mouse_terrain_lookup
                # print "mouse_object_lookup",
                # print mouse_object_lookup

            try:
                screen.blit(graphic_memory[last_edit[0]], (614, 25 ))
                screen.blit(object_memory[last_edit[1]], (614, 25 ))
            except:
                try:
                    screen.blit(graphic_memory[last_edit[0]], (614, 25 ))
                except:
                    screen.blit(graphic_memory[last_edit], (614, 25 ))

            # print "each_key,little_characters[each_key]"
            for each_key in little_characters:
                try:
                    # print "one at a time"
                    # print each_key,
                    # print little_characters[each_key]
                    some_location = little_characters[each_key]["location"]
                    some_char_token = little_characters[each_key]["char_token"]
                    some_font_memory = little_characters[each_key]["char_initial"]
                    # print "my location",game_location
                    # print "some location",some_location
                    my_character_details["location"] = game_location
                    my_character_details["char_token"] = mycharacter_token
                    my_character_details["char_initial"] = mycharacter_initial
                    # image = character_memory[little_world[location]]
                    # print each_key,little_characters[each_key]
                    # if some_char_token != mycharacter_token and some_font_memory != mycharacter_initial:
                    if (abs(some_location[0]-game_location[0]) <= vision):
                        if "seed" in little_characters[each_key].keys():
                            if little_characters[each_key]["seed"] != myrandomseed:
                                screen.blit(character_memory[some_char_token], (center_x - 8+16 * (some_location[0]-game_location[0]), center_y - 8+16 * (some_location[1]-game_location[1])))
                                screen.blit(small_font_memory[some_font_memory], (center_x - 8+16 * (some_location[0]-game_location[0]), center_y - 8+16 * (some_location[1]-game_location[1])))
                        else:
                            screen.blit(character_memory[some_char_token], (center_x - 8+16 * (some_location[0]-game_location[0]), center_y - 8+16 * (some_location[1]-game_location[1])))
                            screen.blit(small_font_memory[some_font_memory], (center_x - 8+16 * (some_location[0]-game_location[0]), center_y - 8+16 * (some_location[1]-game_location[1])))

                except:
                    pass
                # screen.blit(small_font_memory[some_font_memory], (some_location[0]- 8+16, some_location[1]- 8+16))
            # drawing my character
            screen.blit(character_memory[mycharacter_token], (center_x - 8+16 *   0, center_y-8+16 *   0))
            screen.blit(small_font_memory[mycharacter_initial], (center_x - 8+16 *  0, center_y - 8+16 *  0)) # 0
            # if args.role == "client":
            if 1==1:
                # print my_character_details
                my_character_details["location"] = game_location
                my_character_details["char_token"] = mycharacter_token
                my_character_details["char_initial"] = mycharacter_initial
                my_character_details["seed"] = myrandomseed
                # my_character_details["address"]
                # characters['127.0.0.1'] = {}
                # characters['127.0.0.1']["location"] = game_location
                # # print "game location",game_location
                # characters['127.0.0.1']["char_token"] = mycharacter_token
                # characters['127.0.0.1']["char_initial"] = mycharacter_initial
                # characters['127.0.0.1']["time"] = time.time()
            pygame.display.flip()
            first_pass = False


    pygame.quit()

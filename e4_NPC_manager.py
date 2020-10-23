# Python!
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

import os
def lPrint(x,y,text):
    print("\033["+str(x)+";"+str(y)+"H"+str(text) )



parser = argparse.ArgumentParser(description='This allows you to add npcs to the pygameboard.')
parser.add_argument('-n', '--number', type=int, choices=xrange(0,10),default=1)
parser.add_argument('-t', '--token', type=int, choices=xrange(0,8),default=2)
# parser.add_argument('-r', '--role', type=str, choices=['server','client','server_daemon'], default='client')
parser.add_argument('-x', type=int, default=0)
parser.add_argument('-y', type=int, default=0)
args = parser.parse_args()
print "args"
print ".token", args.token
print ".number", args.number

time.sleep(2)
temp = os.system("clear")

little_world = {}
little_characters = {}
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# HOST = socket.gethostbyname('j-macbookpro.local')
hostname = socket.gethostname()
CLIENT = socket.gethostbyname(hostname)
HOST = socket.gethostbyname('gameserver.local')
HOST_PORT = 10996
CLIENT_PORT = 10997
NPC_PORT = 10998

data = {}

# data["NPC1"] = {
#                'char_initial': 28,
#                'char_token': 8,
#                'location': (-1, 0),
# }
# data["NPC2"] = {
#                'char_initial': 29,
#                'char_token': 9,
#                'location': (0, 0),
# }
# data["NPC3"] = {
#                'char_initial': 29,
#                'char_token': 10,
#                'location': (-1, 1),
# }
# data["NPC4"] = {
#                'char_initial': 29,
#                'char_token': 11,
#                'location': (0, 1),
# }
for i in range(10):
    data["NPC"+str(i)] = {
                   'char_initial': i,
                   'char_token': 1,# enemy
                   'location': (0, 0),
    }

# data["NPC1"] = {
#                'char_initial': 1, # number 1
#                'char_token': 1, # enemy
#                'location': (args.x, args.y),
# }

# data["NPC2"] = {
#                'char_initial': 2,
#                'char_token': 1,# enemy
#                'location': (0, 0),
# }

data["Innkeeper"] = {
               'char_initial': " ", # number 1
               'char_token': 4,
               'location': (4, 11),
}
data["Armorer"] = {
               'char_initial': " ", # number 1
               'char_token': 4,
               'location': (0, 23),
}
data["Smith"] = {
               'char_initial': " ", # number 1
               'char_token': 4,
               'location': (13, 23),
}
data["Sexton"] = {
               'char_initial': " ", # number 1
               'char_token': 4,
               'location': (-7, -19),
}

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
        # try:
            # print "trying to receive a slice of the world"
        little_world = dict( little_world.items() + unpickled_uncompressed_received_data['world'].items() )
            # little_world = unpickled_uncompressed_received_data['world']
        little_characters = unpickled_uncompressed_received_data['characters']
            # print "received world", little_world
            # print "received little_characters", little_characters
        # except:
        #     print ""
        #     print "error with ThreadedUDPRequestHandlerForClient server role"
        #     print self.client_address[0]
        #     print self.client_address[1]
        #     print "What is going on?"
        #     print ""


class ThreadedUDPServer(SocketServer.ThreadingMixIn, SocketServer.UDPServer):
    # print "ThreadedUDPServer started"
    pass



def push_to_server():
    global data
    timer = time.time()
    send_data = pickle.dumps(data)
    compressed_send_data = bz2.compress(send_data)
    string = str(HOST) + " "+ str(timer)
    lPrint (20,1, string)
    sock.sendto(compressed_send_data, (HOST, NPC_PORT))

done = False

if __name__ == '__main__':  # single underscore
    serverC = ThreadedUDPServer(("", CLIENT_PORT), ThreadedUDPRequestHandlerForClient)
    server_threadC = threading.Thread(target=serverC.serve_forever)
    server_threadC.daemon = True
    try:
        server_threadC.start()
        # print("Server started at {} port {}".format(CLIENT, CLIENT_PORT))
    except (KeyboardInterrupt, SystemExit):
        serverC.shutdown()
        serverC.server_close()
        exit()

    for each in data.keys():
        data[each]["last_look_time"] = time.time()
    time_check = 0.5
    last = 0
    while not done:
        row = 0
        for each in data.keys():
            if (time.time() - data[each]["last_look_time"] > time_check):
                data[each]["last_look_time"] = time.time()
                location = data[each]["location"]
                move = [0,0]
                option = ("N","S","E","W","Long Delay","Mid Delay","Short Delay")
                option = ("N","S","E","W","D")
                direction = "D"
                direction = random.choice(option)
                if direction == "Short Delay":
                    data[each]["last_look_time"] = data[each]["last_look_time"] + 0.10
                if direction == "D":
                    data[each]["last_look_time"] = data[each]["last_look_time"] + 0.10
                if direction == "Mid Delay":
                    data[each]["last_look_time"] = data[each]["last_look_time"] + 0.20
                if direction == "Long Delay":
                    data[each]["last_look_time"] = data[each]["last_look_time"] + 0.70
                if direction == "N":
                    move[0] -= 1
                if direction == "S":
                    move[0] += 1
                if direction == "E":
                    move[1] -= 1
                if direction == "W":
                    move[1] += 1
                data[each]["direction"] = direction
                # print direction
                # print "-----------",little_world[location][0]
                # print ( location[0]+move[0] , location[1]+move[1] )
                # print little_world[ ( location[0]+move[0] , location[1]+move[1] ) ]
                desired_location = ( location[0]+move[0] , location[1]+move[1] )
                try:
                    if little_world[ ( desired_location[0] , desired_location[1] ) ][0] in [2,3,5,6,7,18,19,20,21,26,27,28,29]:
                        clear = True
                        for eachcheck in little_characters:
                            if desired_location == little_characters[eachcheck]["location"]:
                                clear = False
                                # print "someone there"
                        if clear:
                            data[each]["location"] = ( desired_location[0] , desired_location[1])
                            # data[eachcheck]["location"] = ( location[0]+move[0] , location[1]+move[1] )
                        else:
                            pass
                            # print "someone there"
                        # print "little_characters"
                        # print little_characters
                except:
                    print little_characters.keys()
                #     print "error"
                #     print "error"
                #     print "error"
                #     print "error"
                #     pass

        for each in data.keys():
            row += 1
            pass
            # print each
            lPrint (row,1, each)
            lPrint (row, 7, data[each])
            now = time.time()
            lPrint (18, 1, last-now)
            lPrint (19, 1, now)
            last = now
        push_to_server()
        # time.sleep(0.05)

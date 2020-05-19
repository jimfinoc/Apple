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
args = parser.parse_args()
print "args"
print ".token", args.token
print ".number", args.number

time.sleep(2)
temp = os.system("clear")


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

HOST = socket.gethostbyname('j-macbookpro.local')
HOST_PORT = 10996
CLIENT_PORT = 10997
NPC_PORT = 10998

data = {}

data["NPC1"] = {
               'char_initial': 28,
               'char_token': 8,
               'location': (-1, 0),
}
data["NPC2"] = {
               'char_initial': 29,
               'char_token': 9,
               'location': (0, 0),
}
data["NPC3"] = {
               'char_initial': 29,
               'char_token': 10,
               'location': (-1, 1),
}
data["NPC4"] = {
               'char_initial': 29,
               'char_token': 11,
               'location': (0, 1),
}
data["NPC5"] = {
               'char_initial': 29,
               'char_token': 1,
               'location': (3, 3),
}

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
    while not done:
        row = 0
        # print data
        for each in data:
            row += 1
            pass
            lPrint (row,1, each)
            lPrint (row, 7, data[each])

        push_to_server()
        time.sleep(1)

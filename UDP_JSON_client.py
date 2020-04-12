import socket
import sys
import time
import json

# server_name = input('Enter the server name:')
# print server_name
# HOST = socket.gethostbyname(server_name)
HOST = socket.gethostbyname('j-macbookpro.local')
# HOST = socket.gethostbyname('raspigames.local')
# HOST, PORT = "10.0.1.184", 60106
PORT = 10996

# HOST, PORT = "raspigames.local", 60106
dict = {}
dict['name'] = "James"
dict['steer'] = 1
dict['thrust'] = -1
# data = " ".join(sys.argv[1:])
print dict
data = json.dumps(dict)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

timercounter = 0
# for i in range(100000):
i = 0
while (True):
    i += 1
    # if (timercounter%1000==0):
    time.sleep(.1)
    print "sending to ", HOST, "at port", PORT
    sock.sendto(data + str(i) + "\n", (HOST, PORT))
    # received = sock.recv(1024)
    print("Sent:     {}".format(data + str(i)))
    # print("Received: {}".format(received))

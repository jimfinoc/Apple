# import socket
# import sys
# import time
#
# HOST, PORT = "localhost", 9999
# data = " ".join(sys.argv[1:])
#
# # SOCK_DGRAM is the socket type to use for UDP sockets
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
# # As you can see, there is no connect() call; UDP has no connections.
# # Instead, data is directly sent to the recipient via sendto().
# timercounter = 0
# for i in range(100000):
#     # if (timercounter%1000==0):
#     time.sleep(.01)
#     sock.sendto(data + str(i) + "\n", (HOST, PORT))
#     received = sock.recv(1024)
#     print "Sent:     {}".format(data)
#     print "Received: {}".format(received)

import socket
import sys
import time

HOST = socket.gethostbyname('raspigames.local')
# HOST, PORT = "10.0.1.184", 60106
PORT = 10996

# HOST, PORT = "raspigames.local", 60106
data = " ".join(sys.argv[1:])
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

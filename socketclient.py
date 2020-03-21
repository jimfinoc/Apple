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

HOST, PORT = "localhost", 8888
data = " ".join(sys.argv[1:])
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

timercounter = 0
for i in range(100000):
    # if (timercounter%1000==0):
    time.sleep(.05)
    sock.sendto(data + str(i) + "\n", (HOST, PORT))
    received = sock.recv(1024)
    print("Sent:     {}".format(data))
    print("Received: {}".format(received))

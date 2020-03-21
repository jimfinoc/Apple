# import SocketServer
#
# class MyUDPHandler(SocketServer.BaseRequestHandler):
#     """
#     This class works similar to the TCP handler class, except that
#     self.request consists of a pair of data and client socket, and since
#     there is no connection the client address must be given explicitly
#     when sending data back via sendto().
#     """
#
#     def handle(self):
#         data = self.request[0].strip()
#         socket = self.request[1]
#         print "{} wrote:".format(self.client_address[0])
#         print data
#         socket.sendto(data.upper(), self.client_address)
#
# if __name__ == "__main__":
#     HOST, PORT = "localhost", 9999
#     server = SocketServer.UDPServer((HOST, PORT), MyUDPHandler)
#     server.serve_forever()
import SocketServer, threading, time

class ThreadedUDPRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        current_thread = threading.current_thread()
        print("{}: client: {}, wrote: {}".format(current_thread.name, self.client_address, data))
        socket.sendto(data.upper(), self.client_address)

class ThreadedUDPServer(SocketServer.ThreadingMixIn, SocketServer.UDPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = "raspigames.local", 60106
    # HOST, PORT = "10.0.1.56", 60106

    server = ThreadedUDPServer((HOST, PORT), ThreadedUDPRequestHandler)

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True

    try:
        server_thread.start()
        print("Server started at {} port {}".format(HOST, PORT))
        while True: time.sleep(100)
    except (KeyboardInterrupt, SystemExit):
        server.shutdown()
        server.server_close()
        exit()

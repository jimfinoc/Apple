import SocketServer, threading, time
import socket
import json

class ThreadedUDPRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        current_thread = threading.current_thread()
        print("{}: client: {}, wrote: {}".format(current_thread.name, self.client_address, data))
        print data
        try:
            dict = json.loads(data)
            print dict
        except:
            print "cannot deserialize data"
        # socket.sendto(data.upper(), self.client_address)

class ThreadedUDPServer(SocketServer.ThreadingMixIn, SocketServer.UDPServer):
    pass

if __name__ == "__main__":
    # HOST, PORT = "raspigames.local", 60106
    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)
    # ipaddress = socket.gethostbyname('raspigames.local')
    # HOST, PORT = "10.0.1.184", 60106
    HOST, PORT = ipaddress, 10996
    print "Name:", hostname
    print "Host: ",HOST
    print "Port: ",PORT

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

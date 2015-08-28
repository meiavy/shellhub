import socket
import threading
import SocketServer
import sys

clients=[]

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        clients.append(self)
        print self.client_address
        print "client count:",len(clients)
        try:
            while True:
                data = self.request.recv(1024)
                cur_thread = threading.current_thread()
                response = "{}: {}".format(cur_thread.name, data)
                for client in clients:
                    print "for"
                    client.request.sendall(response)
            else:
                print "else"
                clients.remove(self)
        finally:
            print "finally"
            clients.remove(self)

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "localhost", 9997

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print "Server loop running in thread:", server_thread.name

    sys.stdin.readline()
    server.shutdown()
    server.server_close()
import socket
import sys
import os

HOST, PORT = "localhost", 9997
#data = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((HOST, PORT))
    bRun=True
    while bRun:
        
        data=sys.stdin.readline()
        
        if data=="exit":
            break
        sock.sendall(data)
        # Receive data from the server and shut down
        received = sock.recv(1024)
        print "Sent:     {}".format(data),
        print "Received: {}".format(received),
finally:
    sock.close()



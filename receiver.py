# Save as server.py 
# Message Receiver
import os
from socket import *
host = "10.31.172.96" #cris ip
port = 13000
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
print "Waiting to receive messages..."
while True:
    (data, addr) = UDPSock.recvfrom(buf)
    print "Received message: " + data
    if data == "exit":
        break
UDPSock.close()
os._exit(0)

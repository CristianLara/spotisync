# Save as client.py 
# Message Sender
import os
from socket import *
# host = "128.12.26.98" # set to IP address of target computer --- neven ip
host = "10.31.172.96" # set to IP address of target computer --- cris ip
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
while True:
    data = raw_input("Enter message to send or type 'exit': ")
    UDPSock.sendto(data, addr)
    if data == "exit":
        break
UDPSock.close()
os._exit(0)

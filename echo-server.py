#!/usr/bin/env python

"""
A simple echo server
"""

import socket

print("Initializing server...")
host = '127.0.0.1'
port = 5000
backlog = 5
size = 1024
print("Setting up listening socket...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(backlog)
print("Listen for connections...")
while 1:
    (client, address) = s.accept()
    print("Connection from " + str(address))
    data = client.recv(size)
    if data:
        client.send(data)
    else:
        print("No data received!")
    client.close()

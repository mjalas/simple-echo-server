#!/usr/bin/env python

"""
A simple echo server
"""

import socket


class SimpleEchoServer():
    def __init__(self, host, port, backlog=5, packet_size=1024):
        self.host = host
        self.port = port
        self.backlog = backlog
        self.packet_size = packet_size

    def run(self):
        print("Setting up listening socket...")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))
        s.listen(self.backlog)
        print("Listen for connections on port " + str(self.port) + "...")
        while 1:
            (client, address) = s.accept()
            print("Connection from " + str(address))
            data = client.recv(self.packet_size)
            if data:
                client.send(data)
            else:
                print("No data received!")
            client.close()

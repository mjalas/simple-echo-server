#!/usr/bin/env python

"""
A simple echo server
"""

from echo_server.simple_echo_server import SimpleEchoServer


def main():
    print("Initializing server...")
    host = '127.0.0.1'
    port = 5000
    server = SimpleEchoServer(host, port)
    server.run()

if __name__ == '__main__':
    main()

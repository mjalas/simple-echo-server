#!/usr/bin/env python

"""
A simple echo server
"""

from echo_server.simple_echo_server import SimpleEchoServer
from echo_server.server_option_parser import ServerOptionParser

DEFAULT_PORT = 5000
DEFAULT_ADDRESS = '127.0.0.1'


def main():
    print("Initializing server...")
    optionParser = ServerOptionParser()
    optionParser.parseOptions()
    try:
        port = optionParser.port
    except:
        port = DEFAULT_PORT
    try:
        address = optionParser.address
    except:
        address = DEFAULT_ADDRESS
    server = SimpleEchoServer(address, port)
    server.run()

if __name__ == '__main__':
    main()

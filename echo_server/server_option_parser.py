from optparse import OptionParser


class ServerOptionParser(object):

    def __init__(self):
        self.parser = OptionParser(usage="usage: %prog [options]",
                                   version="%prog 1.0")
        self.parser.add_option("-p", "--port",
                               type="int",
                               dest="port",
                               help="User specified port number.")
        self.parser.add_option( "-a", "--address",
                               dest="address",
                               help="Address of remote host (default is localhost).")

    def parseOptions(self):
        (options, args) = self.parser.parse_args()
        if options.port is not None:
            self.port = options.port
        if options.address is not None:
            self.address = options.address

        self.args = args
        self.options = options

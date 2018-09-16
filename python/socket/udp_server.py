# -*- coding: UTF-8 -*-
import socket
import string

import memformat

class UdpServer:

    def __init__(self, listen_port, listen_ip='0.0.0.0',  recvbuflen = 2048):
        self.ip = listen_ip
        self.port = listen_port
        self.buflen = recvbuflen

    def start(self, isdaemon = False, printhead = True):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.bind((self.ip, self.port))
            
            while True:
                data, address = s.recvfrom(self.buflen)
                if printhead:
                    print '==============================================='
                    print '= From   : {} , {}'.format(str(address[0]), address[1])
                    print '= Length : {}'.format(len(data))
                    print '==============================================='

                    print MemFormat().format(data)

        except Exception as e:
            print 'Exception :' + str(e)

if __name__ == '__main__':
    sys.path
    UdpServer(listen_port = 5555).start()

#!/usr/bin/env python3

import socket
import binascii
import struct

ETH_TYPE_IP = 0x0800 # ip type ethernet packets

class networkSniffer(object):
    def __init__(self,sock):
        self.sock = sock
    
    def sniff_forever(self):
        while True:
            data = sock.recvfrom(2048)
            self.parse(data[0])
    
    @staticmethod
    def _parseMacAddress(addr):
        macaddr = addr.decode()
        out = macaddr[0:2]
        for i in range(2,len(macaddr),2):
            if i % 2 ==0:
                out += ":" + macaddr[i:i+2]
        return out
    
    def parse(self, data):
        ethernet_header = struct.unpack("!6s6s2s",data[0:14])
        print("SRC MAC: {}".format(networkSniffer._parseMacAddress(binascii.hexlify(ethernet_header[0]))))
        print("DST MAC: {}".format(networkSniffer._parseMacAddress(binascii.hexlify(ethernet_header[1]))))
        print()

try:
    sock = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(ETH_TYPE_IP))
    sniffer = networkSniffer(sock)
    sniffer.sniff_forever()
except socket.error:
    print("please run me as root !!!")
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
            print("captured frame on interface: {}".format(data[1][0]))
            networkSniffer.parseRAWPacket(data[0])
    
    @staticmethod
    def _parseMacAddress(addr):
        macaddr = addr.decode()
        out = macaddr[0:2]
        for i in range(2,len(macaddr),2):
            if i % 2 ==0:
                out += ":" + macaddr[i:i+2]
        return out
    
    @staticmethod
    def parseRAWPacket(data):
        protocol_version = None
        ethernet_header = struct.unpack("!6s6s2s",data[0:14])
        print("### MAC INFO ###")
        print("SRC MAC: {}".format(networkSniffer._parseMacAddress(binascii.hexlify(ethernet_header[0]))))
        print("DST MAC: {}\n".format(networkSniffer._parseMacAddress(binascii.hexlify(ethernet_header[1]))))
        print("### IP INFO ###")
        if struct.unpack("!s",data[14:15])[0] == b'E': #checking if the ip header has options or not b'E' == 0x0405 which meand ipv4 and IHL=5
            ip_header = struct.unpack("!9ss2s4s4s",data[14:34])
            print("SRC IP: {}".format(socket.inet_ntoa(ip_header[3])))
            print("DST IP: {}\n".format(socket.inet_ntoa(ip_header[4])))
            protocol_version = ip_header[1]
        else:
            print("Currently unable to parse ip packets with options header\n")
            return
        if protocol_version == b'\x06': #TCP
            print("### TCP DUMP ###")
            tcp_header = struct.unpack("!2s2s16s",data[34:54])
            print("SRC port: {}".format(int(binascii.hexlify(tcp_header[0]),16)))
            print("DST port: {}\n".format(int(binascii.hexlify(tcp_header[1]),16)))
            # print("### RAW PAYLOAD ###")
            # print("\n{}\n".format(data[54:]))
        elif protocol_version == b'\x11': #UDP
            print("### UDP DUMP ###")
            udp_header = struct.unpack("!2s2s4s",data[34:42])
            print("SRC port: {}".format(int(binascii.hexlify(udp_header[0]),16)))
            print("DST port: {}\n".format(int(binascii.hexlify(udp_header[1]),16)))
            # print("### RAW PAYLOAD ###")
            # print("\n{}\n".format(data[42:]))
try:
    sock = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(ETH_TYPE_IP))
    sniffer = networkSniffer(sock)
    sniffer.sniff_forever()
except socket.error:
    print("please run me as root !!!")
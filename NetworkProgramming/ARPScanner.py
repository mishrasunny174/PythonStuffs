#!/usr/bin/env python3

import netifaces
from scapy.all import *

default_interface = netifaces.interfaces()[netifaces.AF_INET]
broadcast_address = netifaces.ifaddresses(default_interface)[netifaces.AF_LINK][0]["broadcast"]
local_mac_address = netifaces.ifaddresses(default_interface)[netifaces.AF_LINK][0]["addr"]
local_ip = netifaces.ifaddresses(default_interface)[netifaces.AF_INET][0]["addr"]

for lsb in range(0,256):
    ip_addr = '.'.join(local_ip.split('.')[0:3]+[str(lsb)])
    frame = Ether(dst=broadcast_address,src=local_mac_address)/ARP(pdst=ip_addr,hwdst=broadcast_address,hwsrc=local_mac_address,psrc=local_ip)
    response = srp1(frame,iface=default_interface,timeout=1,verbose=0)
    if response:
        print("{} is at MAC: {}".format(response.psrc,response.hwsrc))
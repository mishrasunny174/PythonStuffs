#!/usr/bin/env python3

from scapy.all import *
import sys

ssids = []


def sniffWifi(p):
    if p.haslayer(Dot11Beacon):
        ssid = p[Dot11].info
        if ssid not in ssids:
            ssids.append(ssid)
            print(str(ssid))
    else:
        pass


def main():
    if len(sys.argv) != 2:
        print("Usage: {} <monitor mode interface>".format(sys.argv[0]))
        exit(1)
    try:
        sniff(iface=sys.argv[1], prn=sniffWifi,
              filter="wlan type mgt subtype beacon")
    except PermissionError:
        print("Please run me as root !!!")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3 

import socket

LHOST = "0.0.0.0"
LPORT = 1234

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((LHOST,LPORT))
sock.listen()
(client_sock,(client_ip, client_port)) = sock.accept()
print("connected to %s" % client_ip)
data = "dummy"
while len(data) != 0:
    data = client_sock.recv(2048).strip()
    print("recieved data: %s"%data)
    client_sock.send(data + bytes("\n",encoding="utf-8"))

sock.close()
client_sock.close()
#!/usr/bin/env python3

import socket
import select

LHOST = "0.0.0.0"
LPORT = 1234

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((LHOST,LPORT))
sock.listen(100)

clients = []

while True:
    read, write, ex = select.select([sock] + clients, [], [])
    for s in read:
        if s is sock:
            client, addr = s.accept()
            clients.append(client)
            print("Connected: {}".format(addr))
        else:
            data = s.recv(2048).strip()
            if len(data) != 0:
                s.send(data + bytes("\n",encoding="utf-8"))
            else:
                s.send(bytes("bye!",encoding="utf-8"))
                # print("Disconnected: {}".format(s))
                clients.remove(s)
                s.close()

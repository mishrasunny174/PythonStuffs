#!/usr/bin/env python3

from multiprocessing import Process
import socket
import os

LHOST = "0.0.0.0"
LPORT = 1234

def handleClient(client):
    data = "dummy"
    clientSock = client[0]
    print("connection recieved: {}".format(client[1]))
    while len(data) != 0:
        data = clientSock.recv(2048).strip()
        print("Process %d: recieved %s"%(os.getpid(),data))
        clientSock.send(data + bytes("\n", encoding="utf-8"))
    clientSock.close()

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((LHOST,LPORT))
sock.listen(100)
while True:
    client = sock.accept()
    worker = Process(target=handleClient, args=(client,))
    worker.start()

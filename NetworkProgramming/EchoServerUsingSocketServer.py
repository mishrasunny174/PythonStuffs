#!/usr/bin/env python3

import socketserver

LHOST = "0.0.0.0"
LPORT = 1234

class clientHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print("Connection opened: {}".format(self.client_address))
        data = "dummy"
        while len(data) != 0:
            data = self.request.recv(2048).strip()
            self.request.send(data+bytes("\n",encoding="utf-8"))
        print("Connection closed: {}".format(self.client_address))

server = socketserver.TCPServer((LHOST,LPORT),clientHandler)
server.serve_forever()

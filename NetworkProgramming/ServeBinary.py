#!/usr/bin/env python3
import os
import socketserver
import sys
import threading

HOST = '127.0.0.1'
PORT = 4444

class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        super.handle()
        self.request.send("Hi")

class forkServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass

def main():
    server = forkServer((HOST,PORT),Handler.__class__)
    server.allow_reuse_address = True
    server.max_children = 100
    server.serve_forever()

if __name__ == '__main__':
    main()

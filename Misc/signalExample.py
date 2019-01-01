#!/usr/bin/env python3

import signal

def handler_SIGINT(signal,context):
    print("HAHA! you cant make me exit")

signal.signal(signal.SIGINT,handler_SIGINT)

while True:
    pass
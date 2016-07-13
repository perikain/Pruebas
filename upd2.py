#!/usr/bin/env python

import socket

host = "192.168.56.1"
port = 12345
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print s.sendto("Hello all", (host,port))
s.close()
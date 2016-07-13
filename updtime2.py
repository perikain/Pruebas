#!/usr/bin/env python
#!-*- coding: utf-8 -*-

import socket

host = "192.168.56.1"
port = 12345
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
try:
    s.bind((host,port))
    s.settimeout(5)
    data, addr = s.recvfrom(1024)
    print "obtained ", data
    s.close()

except socket.timeout:
    print "Client host NOT connected"
    s.close()

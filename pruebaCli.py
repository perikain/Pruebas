#!/usr/bin/env python
#!-*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "192.168.56.1"
port = 12345
s.connect((host,port))
print s.recv(1024)

frase = ""

while frase != "salir()":
    frase = raw_input()
    s.send(frase)

print "Exiting and closing connection server"

s.close()
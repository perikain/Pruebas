#!/usr/bin/env python

import socket

host = "192.168.56.1"
port = 12345
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
conn, addr = s.accept()
print "Connected by", addr
conn.send("Thanks")
conn.close()

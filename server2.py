#!/usr/bin/env python

import socket
host = "192.168.56.1"
port  = 12345
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host, port))
s.listen(2)

while True:
    conn,addr = s.accept()
    print addr, "Now connected"
    conn.sent("Thank you for connecting")
    conn.close()
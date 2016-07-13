#!/usr/bin/env python
#!-*- coding: utf-8 -*-

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1" # server address
port = 12345 # server port
s.connect((host,port))
print s.recv(1024)
s.send("Hello Server")  #Al conectar al servidor, el puerto del cliente es aleatorio.
s.close

#!/usr/bin/env python
#!-*- coding: utf-8 -*-

import socket

host = "192.168.56.1"
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))
s.settimeout(5)                 #añade una espera de 5 segundos, sólo entonces muestra el mensade error.
data, addr = s.recvfrom(1024) #recvfrom devuelve dos datos, primero el dato y segundo la dirección del cliente.
print "received from ", addr
print "obtained ", data
s.close()


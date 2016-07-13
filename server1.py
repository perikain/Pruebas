#!/usr/bin/env python
#!-*- coding: utf-8 -*-
import socket

host = "127.0.0.1" #server adress
port = 12345 #Port of server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port)) #bind server
s.listen(2)
conn, addr = s.accept()
print addr, "Now connected" #El puerto que imprimimos es el de respuesta del cliente, que es aleatorio.
conn.send("Thank you for connecting")
conn.close()
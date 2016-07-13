#!/usr/bin/env python
#!-*- coding: utf-8 -*-

import socket
import select
import sys
import class_server

class Client:
    def __init__(self, (socket, address)):
        self.socket = socket
        self.address = address
        self.size = 1024

        self.screenname = None

        self.socket.setblocking(0)


    def fileno(self):
        return self.socket.fileno()


    def send(self, data):
        self.socket.send(data)



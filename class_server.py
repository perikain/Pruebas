#!/usr/bin/env python
#!-*- coding: utf-8 -*-

import socket
import select
import sys
import class_client

class Server:
    def __init__(self):
        self.host = ''
        self.port = 12345
        self.server = None
        self.inputs = []
        self.running = True

    def open_socket(self):
        try:
            self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
            self.server.bind((self.host,self.port))
            self.server.listen(5)
            self.server.setblocking(0)

            print "Listening on %s:%s" % (self.host,self.port)

        except socket.error, (value, message):
            if self.server:
                self.server.close()
            print "Could not open socket: " + message
            sys.exit(1)

    def process_new_client(self):
        print "Incoming Connection"
        c = class_client.Client(self.server.accept())
        self.inputs.append(c)
        c.send("-------------------------------\n")
        c.send("Welcome to the A.R. Chat Server\n")
        c.send("-------------------------------\n")
        c.send("Please enter your screen name:\n")

    def process_console_command(self, cmd):
        print "console: %s" % cmd

        if (cmd == "quit"):
            self.shutdown()

    def process_client_message(self, client):
        data = client.socket.recv(1024)
        if data:
            msg = data.rstrip()

            if client.screenname:
                self.sendall(msg, client.screenname)
            else:
                client.screenname = msg[:12]
                self.sendall("%s logged in" % client.screenname)
        else:
            client.socket.close()
            self.inputs.remove(client)
            print "client disconnecting"

            if client.screenname:
                self.sendall("%s disconnected" % client.screenname)


    def sendall(self, data, fromuser=None):
        for c in self.inputs:
            if isinstance(c, class_client.Client):
                if c.screenname:
                    if fromuser:
                        c.send("::".join([fromuser, data]) + "\n")
                    else:
                        c.send(data + "\n")
            elif c == sys.stdin:
                print "%s --> %s" % (fromuser, data)


    def shutdown(self):
        for c in self.inputs:
            if isinstance(c, class_client.Client):
                self.inputs.remove(c)
                c.send("Server Shutting Down!\n")
                c.socket.close()

            if self.server:
                self.server.close()

            self.running = False


    def run(self):
        self.inputs = [self.server, sys.stdin]

        self.running = True
        while self.running:
            inputready, outputready, exceptready = select.select(self.inputs, [], [])

            for s in inputready:
                if s == self.server:
                    self.process_new_client()

                elif s == sys.stdin:
                    inp = sys.stdin.readline().rstrip()
                    self.process_console_command(inp)

                elif isinstance(s, class_client.Client):
                    self.process_client_message(s)

        self.shutdown()

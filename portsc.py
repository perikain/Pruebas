#!/usr/bin/env python
#!-*- coding: utf-8 -*-

import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('cls', shell=True)
rmip = raw_input("\t Enter the remote host IP to scan: ")
r1 = int(raw_input("\t Enter the start port number:\t"))
r2 = int(raw_input("\t Enter the last port number:\t"))
print "*"*40
print "\nA.R. Scanner is working on ", rmip
print "*"*40

t1 = datetime.now()

try:
    for port in xrange(r1,r2):
        mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = mySocket.connect_ex((rmip,port))
        if result == 0:
            print "Port open: -->\t", port
            # print desc[port]
        mySocket.close()

except KeyboardInterrupt:
    print "You stop this..."
    sys.exit()

except socket.error:
    print "Could not connect to server"
    sys.exit()

t2 = datetime.now()
total = t2 - t1

print "Scanning complete in ", total



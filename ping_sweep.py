#!/usr/bin/env python
#!-*- coding: utf-8 -*-

import os
import platform
from datetime import datetime

net = raw_input("Enter the Network address ")
net1 =  net.split('.')
a = '.'
net2 = net1[0]+a+net1[1]+a+net1[2]+a
st1 = int(raw_input("Enter the Starting Number "))
en1 = int(raw_input("Enter the Last Number "))

en1 += 1

oper = platform.system()

if (oper == "Windows"):
    ping1 = "ping -n 1 "
elif (oper == "Linux"):
    ping1 = "ping -c 1 "
else:
    ping1 = "ping -c 1 "

t1 = datetime.now()

print "Scanning in progress..."
for ip in xrange(st1,en1):
    addr = net2+str(ip)
    comm = ping1+addr
    response = os.popen(comm)
    for line in response.readlines():
        if(line.count("TTL")):
            break
        if(line.count("TTL")):
            print addr, "--> LIVE"
t2 = datetime.now()
total = t2 - t1
print "Scanning complete in ", total



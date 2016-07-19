#!/usr/bin/env python
#!-*- coding: utf-8 -*-

import os
import collections
import platform
import socket
import subprocess
import sys
import threading

from datetime import datetime
'''Section 1'''

net = raw_input("Enter the Network Addres ")
net1 = net.split('.')
a = '.'
net2 = net1[0]+a+net1[1]+a+net1[2]+a
st1 = int(raw_input("Enter the Starting Number "))
en1 = int(raw_input("Enter the Last Number "))
en1 = en1 + 1
dic = collections.OrderedDict()
oper = platform.system()

if (oper == "Windows"):
    ping1 = "ping -n 1 "
elif (oper == "Linux"):
    ping1 = "ping -c 1 "
else:
    ping1 = "ping -c 1 "
t1 = datetime.now()

'''Section 2'''

class MyThread (threading.Thread):
    def __init__(self,st,en):
        threading.Thread.__init__(self)
        self.st = st
        self.en = en

    def run(self):
        run1(self.st, self.en)


'''Section 3'''
def run1(st1, en1):
    #print "Scanning in progess..."
    for ip in xrange(st1,en1):
        #print ".",
        addr = net2+str(ip)
        comm = ping1+addr
        response = os.popen(comm)
        for line in response.readlines():
            if(line.count("TTL")):
                break
        if (line.count("TTL")):
            #print addr, "--> Live"
            dic[ip] = addr

'''Section 4'''
total_ip = en1-st1
tn = 20 #number of ip handled by one thread
total_thread = total_ip / tn
total_thread = total_thread +1
threads = []
try:
    for i in xrange(total_thread):
        en = st1+tn
        if (en > en1):
            en = en1
        thread = MyThread(st1,en)
        thread.start()
        threads.append(thread)
        st1 = en
except:
    print "Error: unable to start thread."
print "\t Number of Threads active: ", threading.active_count()

for t in threads:
    t.join()

print "Exiting main thread"
dict = collections.OrderedDict(sorted(dic.items()))
for key in dict:
    print dict[key], "--> Live"

t2 = datetime.now()
total = t2 - t1
print "Scanning complete in ", total




#!/usr/bin/env python
#!-*- coding: utf-8 -*-

import threading
import time
import socket
import subprocess
import sys
from datetime import datetime
import thread
import shelve


'''Section 1'''

subprocess.call('cls',shell=True)


'''Section 2'''
class MyThread(threading.Thread):
    def __init__(self, threadName, rmip, r1, r2, c):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.rmip = rmip
        self.r1 = r1
        self.r2 = r2
        self.c = c
    def run(self):
        scantcp(self.threadName, self.rmip,self.r1, self.r2, self.c)


'''Section 3'''
def scantcp(threadName, rmip, r1, r2, c):
    try:
        for port in xrange(r1, r2):
            mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(c)
            result =  mySocket.connect_ex((rmip,port))

            if result == 0:
                print "Port Open: ----->\t", port, "--", data.get(port, "Not in Database")
                mySocket.close()

    except KeyboardInterrupt:
        print "You stop this."
        sys.exit()
    except socket.gaierror:
        print "Hostname could not be resolved."
        sys.exit()
    except socket.error:
        print "Could not connect to Server."
        sys.exit()

'''Section 4'''
print "*"*60
print " \tWelcome this is the Advanced Port Scanner of A.R.\n"
d = raw_input("\t Press D for Domain Name or Press I for IP Address\t")

if (d == 'D' or d =='d'):
    rmserver = raw_input("\t Enter the Domain Name to scan: \t")
    rmip = socket.gethostbyname(rmserver)
elif (d == 'I' or d == 'i'):
    rmip = raw_input("\t Enter the IP Address to scan: ")
else:
    print "Wrong input"

#rmip = socket.gethostbyname(rmserver)
r11 = int(raw_input("\t Enter the start port number\t"))
r21 = int(raw_input("\t Enter the last port number\t"))
connect = raw_input("For Low connectivity press L and for High connectivity press H:\t")

if (connect == "L" or connect == "l"):
    c = 1.5
elif (connect == "H" or connect == "h"):
    c = 0.5
else:
    print "\t Wrong Input"

print "\n A.R.'s Scanner is working on ", rmip
print "*"*60
t1 = datetime.now()
tp = r21 - r11

tn = 30
#tn number of port handled by one thread
tnum = tp /tn
if (tp%tn != 0):
    tnum = tnum + 1

if (tnum > 300):
    tn = tp/300
    tn = tn + 1
    tnum = tp/tn
    if(tp%tn != 0):
        tnum = tnum + 1

'''Section 5'''

threads = []

try:
    for i in xrange(tnum):
        #print "i is ", i
        k = i
        r2 = r11+tn
        #thread=str(i)
        thread = MyThread("T1", rmip, r11, r2, c)
        thread.start()
    threads.append(thread)
    r11 = r2

except:
    print "Error: Unable to start thread."

print "\t Number of Threas active:", threading.active_count()

for t in threads:
    t.join()
print "Exiting Main Thread"
t2 = datetime.now()

total = t2 - t1
print "Scanning complete in " , total





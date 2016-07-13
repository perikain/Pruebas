#!/usr/bin/env python
#!-*- coding: utf-8 -*-


import os
response = os.popen('ping -n 1 74.125.133.104')
for line in response.readlines():
    print line

#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import subprocess
proc = subprocess.Popen("C:\Users\Public\serial.exe",stdin=subprocess.PIPE,stdout=subprocess.PIPE)

while 1:
    message = proc.stdout.read(640)
    print message
    print "------------------------"

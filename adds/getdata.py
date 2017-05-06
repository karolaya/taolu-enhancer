#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import subprocess
proc = subprocess.Popen("C:\Users\Public\serial.exe",stdin=subprocess.PIPE,stdout=subprocess.PIPE)

state = "run"
while state == "run":
    cppMessage = proc.stdout.readline().rstrip("\n") 
    print "data ->" + cppMessage + " \n"

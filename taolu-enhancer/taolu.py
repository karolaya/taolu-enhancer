'''
	Entry point of the taolu-enhancer system
'''
import subprocess
import cv2
import numpy as np
import matplotlib.pyplot as mplt
from threading import Thread
from interface.application import Application as App
from collections import namedtuple


proc = subprocess.Popen("C:\\Users\\user\\Documents\\Git\\taolu-enhancer\\taolu-enhancer\\Debug\\serial.exe",
stdin=subprocess.PIPE,
stdout=subprocess.PIPE)

Joint2D = namedtuple('Joint2D', ['x', 'y'])

app = App(proc)

def convert3DTo2D(a, b, c):
	xx = int((a + 2.2)*640/4.4)
	yy = int((b + 1.6)*480/3.2)

	if xx > 640:
		xx = 640
	if yy > 480:
		yy = 480

	xx = xx
	yy = 480 - yy
	return Joint2D(x=xx, y=yy) 

i = 0
joints = list()
while 1:
	line = proc.stdout.readline()
	line = line.strip()

	if len(line) > 60 and len(line) < 1000:
		joints = list()
		tam = [i.split(',') for i in line.decode('utf-8').split(';')][:-1]
		print(tam)
		for t in tam:
			joints.append(convert3DTo2D(float(t[0]), float(t[1]), float(t[2])))

	if len(line) == 921600:
		mv = memoryview(line)
		numeric = np.asarray(mv)-48
		AR = numeric[0::3].reshape((480,640))
		AG = numeric[1::3].reshape((480,640))
		AB = numeric[2::3].reshape((480,640))
		
		A = np.dstack([AB, AG, AR])
		app.loadVideoHolder(A, joints)
		cv2.waitKey(15)

	app.checkPendingOperations()
	#cv2.imshow('video',A)
		
	#print(numeric)
	#i +=1
	app.update()
	app.update_idletasks()
"""
app = App()
#img = cv2.imread("shinobu.jpg",1)
while 1:
	drawPoint(img,240,320,5)
	app.loadVideoHolder(img)
	app.update()
	app.update_idletasks()
"""




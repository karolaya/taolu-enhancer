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

def convert3DTo2D(x0, y0, z0):
	xt = x0*320/2.2
	yt = y0*240/1.6

	angx = 57*xt/640
	angy = 43*yt/480
	#print("ax: "+str(angx))
	#print("ay: "+str(angy))

	xr = np.tan(angx*np.pi/180)*640*4.2/(z0)
	yr = np.tan(angy*np.pi/180)*480*4.2/(z0)
	#print("xr: "+str(xr))
	#print("yr: "+str(yr))

	xpix = 320 + xr
	ypix = np.abs(yr-240)
	#print("xpix: "+str(xpix))
	#print("ypix: "+str(ypix))

	if xpix > 639:
		xpix = 639
	if ypix > 479:
		ypix = 479

	return Joint2D(x = int(xpix), y = int(ypix)) 

i = 0
joints = list()
while 1:
	line = proc.stdout.readline()
	line = line.strip()

	if len(line) > 60 and len(line) < 1000:
		joints = list()
		tam = [i.split(',') for i in line.decode('utf-8').split(';')][:-1]
		#print(tam)
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




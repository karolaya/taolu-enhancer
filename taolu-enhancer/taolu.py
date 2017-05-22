'''
	Entry point of the taolu-enhancer system
'''
import subprocess
import cv2
import numpy as np
import matplotlib.pyplot as mplt
from threading import Thread
from interface.application import Application as App

'''
proc = subprocess.Popen("C:\\Users\\Public\\serial.exe",
stdin=subprocess.PIPE,
stdout=subprocess.PIPE)

app = App()

i = 0
while 1:
	line = proc.stdout.readline()
	line = line.strip()
	print(line)
	if len(line) == 921600:
		mv = memoryview(line)
		numeric = np.asarray(mv)-48
		AR = numeric[0::3].reshape((480,640))
		AG = numeric[1::3].reshape((480,640))
		AB = numeric[2::3].reshape((480,640))
		
		A = np.dstack([AB, AG, AR])
		app.loadVideoHolder(A)
		#cv2.imshow('video',A)
		cv2.waitKey(15)
		#print(numeric)
		#i +=1
		app.update()
		app.update_idletasks()'''

app = App()
img = cv2.imread("shinobu.jpg",1)
while 1:
	app.loadVideoHolder(img)
	app.update()
	app.update_idletasks()

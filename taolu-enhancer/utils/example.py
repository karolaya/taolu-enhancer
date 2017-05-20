import subprocess
import cv2
import numpy as np
import matplotlib.pyplot as mplt

proc = subprocess.Popen("C:\\Users\\Public\\serial.exe",
stdin=subprocess.PIPE,
stdout=subprocess.PIPE)

state = "run"
i = 0
cppMessage = ''
mplt.figure()

while 1:
    line = proc.stdout.readline()
    line = line.strip()
    if len(line) == 921600:
        mv = memoryview(line)
        numeric = np.asarray(mv)-48
        AR = numeric[0::3].reshape((480,640))
        AG = numeric[1::3].reshape((480,640))
        AB = numeric[2::3].reshape((480,640))
        
        A = np.dstack([AR, AG, AB])
        cv2.imshow('video',A)
        cv2.waitKey(15)
        #print(numeric)
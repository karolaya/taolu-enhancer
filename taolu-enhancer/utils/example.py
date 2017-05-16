import subprocess
import cv2
import numpy as np
import matplotlib.pyplot as mplt

def guessVal(i):
    if i - 48 < 0:
        if i - 48 == -1:
            return 219
        return i + 208
    return i - 48

proc = subprocess.Popen("C:\\Users\\Public\\serial.exe",
stdin=subprocess.PIPE,
stdout=subprocess.PIPE)

state = "run"
i = 1
cppMessage = ''
mplt.figure()

while 1:
    AR = list()
    AG = list()
    AB = list()  
    line = proc.stdout.readline()
    line = line.strip()
    if len(line) == 1920:
        numeric = [guessVal(line[i]) for i in range(len(line))]
        AR.append(numeric[0::3])
        AG.append(numeric[1::3])
        AB.append(numeric[2::3])
        i = i + 1
        print(i)
        if (i == 480):
                #mplt.figure()
                AR = np.array(AR,dtype = np.uint8)
                AB = np.array(AB,dtype = np.uint8)
                AG = np.array(AG,dtype = np.uint8)
                A = cv2.merge((AR,AB,AG))
                mplt.imshow(A)
                cv2.waitKey(0)
                A = []
                i = 0 

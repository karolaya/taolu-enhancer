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

proc = subprocess.Popen("C:\\Users\\user\\Documents\\Git\\taolu-enhancer\\taolu-enhancer\\Debug\\serial.exe",
stdin=subprocess.PIPE,
stdout=subprocess.PIPE)

state = "run"
i = 0
cppMessage = ''
A = list()
AR = list()
AG = list()
AB = list()
mplt.figure()
while 1:
        
    line = proc.stdout.readline()
    line = line.strip()
    if len(line) == 1920:
        numeric = [guessVal(line[i]) for i in range(len(line))]
        AR.append(numeric[0::3])
        AG.append(numeric[1::3])
        AB.append(numeric[2::3])
        print(i)
        i = i + 1
    if (i == 480):
                AR = np.array(AR, np.uint8)
                AG = np.array(AG, np.uint8)
                AB = np.array(AB, np.uint8)
                num = cv2.merge([AB, AG, AR])
                print(num)
                mplt.imshow(num)
                mplt.show()
                A = []
                AR = []
                AG = []
                AB = []
                i = 0

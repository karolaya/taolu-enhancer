import numpy as np
import cv2
import tkinter as tk
import subprocess
import matplotlib.pyplot as mplt

proc = subprocess.Popen("C:\\Users\\Public\\serial.exe",
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE)

#Set up GUI
screen = tk.Tk()  #Makes main screen
screen.wm_title("Taolu enhancer")
screen.config(background="#FFFFFF")

#Graphics screen
frame = tk.Frame(screen, width=640, height=480)
frame.grid(row=0, column=0, padx=10, pady=2)

#Capture video frames
#l_image = tk.Label(frame)
i = 0
def show_image():
    line = proc.stdout.readline()
    line = line.strip()
    if len(line) == 921600:
        mv = memoryview(line)
        numeric = np.asarray(mv)-48
        AR = numeric[0::3].reshape((480,640))
        AG = numeric[1::3].reshape((480,640))
        AB = numeric[2::3].reshape((480,640))
        A = cv2.merge((AR,AG,AB))
        P = PhotoImage(image = Image.fromarray(A))
        Pl = Label(image = P)
        Pl.grid()
        Pl.image = P
        Pl.after(10, show_frame)

show_image()  #Display 2
screen.mainloop()  #Starts GUI
"""
i = 0
while 1:
    line = proc.stdout.readline()
    line = line.strip()
    if len(line) == 921600:
        mv = memoryview(line)
        numeric = np.asarray(mv)-48
        AR = numeric[0::3].reshape((480,640))
        AG = numeric[1::3].reshape((480,640))
        AB = numeric[2::3].reshape((480,640))
        
        A = cv2.merge((AR,AG,AB))
        cv2.imshow('video',A)
        cv2.waitKey(15)
        #print(numeric)
"""
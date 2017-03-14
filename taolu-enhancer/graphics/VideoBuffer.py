import cv2
import numpy as np
from threading import Thread

class VideoBuffer(Thread):
    def __init__(self, conn):
        self.active = True
        self.lock = False
        self.connector = conn
    
    def loopSource(self, count=1):
        if not self.lock:
            self.lock = True
            thread = Thread(target=self.parseFrames, args=())
            thread.start()

    def parseFrames(self):
        while self.active:
            (depth,_), (rgb,_) = self.connector.getKinectData()

            d3 = np.dstack((depth, depth, depth)).astype(np.uint8)
            da = np.hstack((d3,rgb))

            cv2.imshow('both', np.array(da[::1,::1,::-1]))
            cv2.waitKey(5)

import time
import subprocess
from threading import Thread

class Writer:
    STANDBY_MODE = 0
    JOINTS_MODE = 1
    RGB_MODE = 2

    def __init__(self, pipe, def_type=STANDBY_MODE):
        self.def_type = def_type
        self.proc = subprocess.Popen(pipe,
            stdin = subprocess.PIPE,
            stdout = subprocess.PIPE)

    def setDefaultConnectionType(self, conn_type):
        self.def_type = conn_type

    def issueTimedCommand(self, conn_type, interval):
        self.proc.stdin.write(str(conn_type))
        t = Thread(None, target=self.waitElapsed, args=(time.time(), interval))
        t.start()

    def waitElapsed(self, init_time, interval):
        while time.time() - init_time < interval:
            pass
        self.proc.stdin.write(str(self.def_type))

class Reader:
    def __init__(self, pipe):
        self.sw = False
        self.proc = subprocess.Popen(pipe,
            stdin = subprocess.PIPE,
            stdout = subprocess.PIPE)

    def startReading(self):
        self.sw = True
        t = Thread(None, target=self.readDataInBuffer, args=())
        t.start()

    def readDataInBuffer(self):
        while(self.sw):
            mess = proc.stdout.readline().rstrip("\n")
            if(!mess.empty()):
                print(mess)
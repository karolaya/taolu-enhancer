import time
import subprocess
from threading import Thread

class Writer:
    STANDBY_MODE = 0
    JOINTS_MODE = 1
    RGB_MODE = 2

    def __init__(self, proc, def_type = STANDBY_MODE):
        self.def_type = def_type
        self.proc = proc

    def setDefaultConnectionType(self, conn_type):
        self.def_type = conn_type

    def issueTimedCommand(self, reader, interval):
        self.proc.stdin.write(str(conn_type))
        t = Thread(None, target = self.waitElapsed, args = (time.time(), interval, reader))
        t.start()

    def waitElapsed(self, init_time, interval, reader):
        while time.time() - init_time < interval:
            print('Holo')
        reader.sw = True
        self.proc.stdin.write(str(self.def_type))

class Reader:
    def __init__(self, pipe, conn_type):
        self.sw = False
        self.conn = conn_type
        self.lst = ["form"]
        self.proc = subprocess.Popen(pipe,
            stdin = subprocess.PIPE,
            stdout = subprocess.PIPE)

    def startReading(self):
        self.sw = True
        t = Thread(None, target = self.readDataInBuffer, args = (self.conn))
        t.start()

    def readDataInBuffer(self, conn_type):
        while(self.sw):
            mess = self.proc.stdout.readline().rstrip("\n")
            if mess is not "" and conn_type == 1:
                #self.lst.append(cmm_s[i])
            else:
                print(mess)
        if conn_type == 1:
            Joints_lst(mess)

    def jointsLst(cmm):
        cmm_s = cmm.split(";")
        del cmm_s[-1]
        i = 0

        for i in range(len(cmm_s)):
            self.lst.append(cmm_s[i])

    def getProcess(self):
        return self.proc

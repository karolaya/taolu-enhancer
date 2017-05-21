import time
import subprocess
import listaDB as klist
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
        conn_type = reader.getConnType()
        
        # Wait for connection to stablish
        while reader.conn_flag == 0:
            pass
        print('Connection stablished')
        self.proc.stdin.write(bytes(str(conn_type) + '\n','ASCII'))
        t = Thread(None, target = self.waitElapsed, args = (time.time(), interval, reader))
        t.start()

    def waitElapsed(self, init_time, interval, reader):
        while time.time() - init_time < interval:
            pass
        print('Finished sending')
        reader.sw = False
        self.proc.stdin.write(bytes(str(self.def_type) + '\n','ASCII'))

class Reader:
    def __init__(self, pipe, conn_type):
        self.sw = False
        self.conn = conn_type
        self.lst_cpp = []
        self.conn_flag = 0
        self.proc = subprocess.Popen(pipe,
            stdin = subprocess.PIPE,
            stdout = subprocess.PIPE)

    def startReading(self):
        self.sw = True
        t = Thread(None, target = self.readDataInBuffer, args = (self.conn,))
        t.start()

    def readDataInBuffer(self, conn_type):
        while(self.sw):
            print('Reading')
            mess = self.proc.stdout.readline().strip(b"\n")
            if self.conn_flag == 0:
                self.conn_flag = 1
            if mess is not '' and conn_type == 1:
                self.lst_cpp.append(mess)
        if conn_type == 1:
            print(self.lst_cpp[1])
            self.jointsLst(self.lst_cpp[1:])

    def jointsLst(self, cmm):
        klist.listaDB(self.lst_cpp)

    def getProcess(self):
        return self.proc

    def getConnType(self):
        return self.conn

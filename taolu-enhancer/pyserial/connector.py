import time
import subprocess
import pyserial.listaDB as klist
from threading import Thread


class Reader:
    def __init__(self, conn_type,proc,move = ""):
        self.proc = proc
        self.move = move
        self.sw = False
        self.conn = conn_type

        self.lst_cpp = []
        self.conn_flag = 0

    def startReading(self, interval):
        self.sw = True
        t = Thread(None, target = self.readDataInBuffer, args = (self.conn,time.time(),interval))
        t.start()

    def readDataInBuffer(self, conn_type, init_time, interval):
        while self.conn_flag == 0 or time.time() - init_time < interval:
            #try:
                mess = self.proc.stdout.readline()
                mess = mess.strip()
                if len(mess) < 1000:
                    mess = mess.decode('utf-8')
                    print('Reading')
                    if self.conn_flag == 0:
                        print('\nConnection stablished')
                        init_time = time.time()
                        self.conn_flag = 1
                    if mess is not '':
                        self.lst_cpp.append(mess)
            #except Exception:
            #    print('Error in PIPE')
        print('Connection finished')
        if conn_type == 1 and len(self.lst_cpp) > 1:
            self.jointsLst(self.lst_cpp[1:])
        elif conn_type == 2 and len(self.lst_cpp) > 1:
            self.guessFromModel(self.lst_cpp[1:])


    def jointsLst(self, cmm):
        klist.listaDB(self.lst_cpp, self, self.move)

    def guessFromModel(self,cmm):
        klist.listaDB(self.lst_cpp, self, save = False)

    def getProcess(self):
        return self.proc

    def getConnType(self):
        return self.conn

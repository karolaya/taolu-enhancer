from connector import Writer, Reader

koko = Writer("C:\\Users\\user\\Documents\\Git\\taolu-enhancer\\taolu-enhancer\\Debug\\serial.exe")
koko.issueTimedCommand(1, 10)

kok = Reader(koko.getProcess())
kok.startReading()

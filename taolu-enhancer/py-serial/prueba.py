import subprocess

def guessVal(i):
	if i - 48 < 0:
		if i - 48 == -1:
			return 219
		return i + 208
	return i - 48

proc = subprocess.Popen("C:\\Users\\user\\Documents\\Visual Studio 2017\\serial.exe",
stdin=subprocess.PIPE,
stdout=subprocess.PIPE)

state = "run"
i = 0
cppMessage = ''
while 1:
	line = proc.stdout.readline()
	line = line.strip()
	if len(line) == 1920:
		numeric = ','.join([str(guessVal(line[i])) for i in range(len(line))])
	
		#print(numeric)
		#print('********************************')
		print(str(i))
	    
		i = i + 1

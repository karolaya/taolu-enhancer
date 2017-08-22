# Open data file
forms = list()
with open('confidence.txt', 'r') as f:
    line = f.readline()
    if 'Forma' in line:
        forms.append(int(line.split(' ')[1]), 0)

#cmm = ['x,y,z;x1,y1,z1;x2,y2,z2;','x,y,z;x1,y1,z1;x2,y2,z2;','x,y,z;x1,y1,z1;x2,y2,z2;']
import numpy as np
from utils.db import saveJointsDB, saveAnglesDB
from utils.angle_calculator import obtainAngles
from core.classifier import SVMClassifier


def listaDB(cmm, master, move = "", save = True):
    lst = []
    vals = []
    lst_db = []

    for k in range(len(cmm)):
        cmm_s = ','.join(cmm[k].split(';'))[0:-1].split(',')
        if len(cmm_s) == 60:
            lst.append(cmm_s)

    for j in range(60):
        vals.append(np.mean([float(a[j]) for a in lst]))
    #print(vals)

    for i in range(0, len(vals), 3):
        s_db = str(vals[i]) + ',' + str(vals[i + 1]) + ',' + str(vals[i + 2])
        lst_db.append(s_db)

    angles = obtainAngles([lst_db], 'prueba')
    angles = angles[0][1:]
    angles = np.array(angles).reshape(1,-1)
    svm = SVMClassifier()
    if save == True:
        saveJointsDB([move] + lst_db)
        saveAnglesDB(move)
    else:
        a = svm.getConfidence(angles)[0]
        print(a)
        if max(a) -0.5 == int(max(a)):
            master.move = svm.guessValueSVM(angles)
        else:
            master.move = "Unknown"



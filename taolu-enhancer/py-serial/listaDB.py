#cmm = ['x,y,z;x1,y1,z1;x2,y2,z2;','x,y,z;x1,y1,z1;x2,y2,z2;','x,y,z;x1,y1,z1;x2,y2,z2;']

def listaDB(cmm):
    lst = ['form']

    for k in range(len(cmm)):
        cmm_s = cmm[k].split(";")
        del cmm_s[-1]
        i = 0
        for i in range(len(cmm_s)):
            lst.append(cmm_s[i])
        lst.append("form")
    del lst[-1]
    for j in range(0, len(lst), lst[1:].index('form') + 1):
        print lst[j:j + lst[1:].index('form') + 1]

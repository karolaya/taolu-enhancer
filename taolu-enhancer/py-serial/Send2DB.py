cmm = "x,y,z;x1,y1,z1;x2,y2,z2;x3,y3,z3;"

def Joints_lst(cmm):
    cmm_s = cmm.split(";")
    del cmm_s[-1]

    lst = ["form"]
    i = 0

    for i in range(len(cmm_s)):
        lst.append(cmm_s[i])

    return(lst)
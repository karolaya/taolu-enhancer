import sqlite3
import numpy as np
from angle_calculator import calculateAngleProjection,Joint
from definitions import Projections,Joints

def savePointsDB(data):
    conn = sqlite3.connect('database.db') #connection object
    c = conn.cursor()
    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS joints
                (n_sample INTEGER PRIMARY KEY,
                move TEXT NOT NULL,
                HIP_CENTER TEXT NOT NULL,
                SPINE TEXT NOT NULL,
                SHOULDER_CENTER TEXT NOT NULL,
                HEAD TEXT NOT NULL,
                SHOULDER_LEFT TEXT NOT NULL,
                ELBOW_LEFT TEXT NOT NULL,
                WRIST_LEFT TEXT NOT NULL,
                HAND_LEFT TEXT NOT NULL,
                SHOULDER_RIGHT TEXT NOT NULL,
                ELBOW_RIGHT TEXT NOT NULL,
                WRIST_RIGHT TEXT NOT NULL,
                HAND_RIGHT TEXT NOT NULL,
                HIP_LEFT TEXT NOT NULL,
                KNEE_LEFT TEXT NOT NULL,
                ANKLE_LEFT TEXT NOT NULL,
                FOOT_LEFT TEXT NOT NULL,
                HIP_RIGHT TEXT NOT NULL,
                KNEE_RIGHT TEXT NOT NULL,
                ANKLE_RIGHT TEXT NOT NULL,
                FOOT_RIGHT TEXT NOT NULL)
                ''')
    c.executemany('''INSERT INTO joints VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', data)
    conn.commit()
    conn.close()
    print("[!]Table joints added/updated")

def saveAnglesDB(move):
    conn = sqlite3.connect('database.db') #connection object
    c = conn.cursor()
    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS angles
                (n_sample INTEGER PRIMARY KEY,
                move TEXT NOT NULL,
                NECK_TORSO REAL NOT NULL,
                SHOULDER_ARM_R REAL NOT NULL,
                SHOULDER_ARM_L REAL NOT NULL,
                ARM_ARM_R REAL NOT NULL,
                ARM_ARM_L REAL NOT NULL,
                HIP_LEG_R REAL NOT NULL,
                HIP_LEG_L REAL NOT NULL,
                LEG_LEG_R REAL NOT NULL,
                LEG_LEG_L REAL NOT NULL,
                ARM_HIPLINE_R REAL NOT NULL,
                ARM_HIPLINE_L REAL NOT NULL,
                THIGH_HIPLINE_R REAL NOT NULL,
                THIGH_HIPLINE_L REAL NOT NULL)
                ''')

    c.execute('SELECT HIP_CENTER,SPINE,SHOULDER_CENTER,HEAD,'
                'SHOULDER_LEFT,ELBOW_LEFT,WRIST_LEFT,HAND_LEFT,'
                'SHOULDER_RIGHT,ELBOW_RIGHT,WRIST_RIGHT,HAND_RIGHT,'
                'HIP_LEFT,KNEE_LEFT,ANKLE_LEFT,FOOT_LEFT,HIP_RIGHT,'
                'KNEE_RIGHT,ANKLE_RIGHT,FOOT_RIGHT '
                'FROM joints WHERE move = "'+move+'"')
    jointslist = c.fetchall()
    angles = ["",0,0,0,0,0,0,0,0,0,0,0,0,0]
    angleslist = []
    for i in range(0,len(jointslist)):
        angles[0] = move

        # Neck-Head Angle:
        J1 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_HEAD].split(',')]
        J2 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_SHOULDER_CENTER].split(',')]
        J3 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_SPINE].split(',')]
        angles[Projections.ANGLE_NECK_TORSO] = calculateAngleProjection(Joint(x=J1[0], y=J1[1],z=J1[2]),Joint(x=J2[0], y=J2[1],z=J2[2]),Joint(x=J3[0], y=J3[1],z=J3[2]))

        # Neck-Elbow-Right Angle:
        J1 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_SHOULDER_CENTER].split(',')]
        J2 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_SHOULDER_RIGHT].split(',')]
        J3 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_ELBOW_RIGHT].split(',')]
        angles[Projections.ANGLE_SHOULDER_ARM_R] = calculateAngleProjection(Joint(x=J1[0], y=J1[1],z=J1[2]),Joint(x=J2[0], y=J2[1],z=J2[2]),Joint(x=J3[0], y=J3[1],z=J3[2]))

        # Neck-Elbow-Left Angle:
        J1 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_SHOULDER_CENTER].split(',')]
        J2 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_SHOULDER_LEFT].split(',')]
        J3 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_ELBOW_LEFT].split(',')]
        angles[Projections.ANGLE_SHOULDER_ARM_L] = calculateAngleProjection(Joint(x=J1[0], y=J1[1],z=J1[2]),Joint(x=J2[0], y=J2[1],z=J2[2]),Joint(x=J3[0], y=J3[1],z=J3[2]))

        # Elbow-Hand-Right Angle:
        J1 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_SHOULDER_RIGHT].split(',')]
        J2 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_ELBOW_RIGHT].split(',')]
        J3 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_HAND_RIGHT].split(',')]
        angles[Projections.ANGLE_ARM_ARM_R] = calculateAngleProjection(Joint(x=J1[0], y=J1[1],z=J1[2]),Joint(x=J2[0], y=J2[1],z=J2[2]),Joint(x=J3[0], y=J3[1],z=J3[2]))

        # Elbow-Hand-Left Angle:
        J1 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_SHOULDER_LEFT].split(',')]
        J2 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_ELBOW_LEFT].split(',')]
        J3 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_HAND_LEFT].split(',')]
        angles[Projections.ANGLE_ARM_ARM_L] = calculateAngleProjection(Joint(x=J1[0], y=J1[1],z=J1[2]),Joint(x=J2[0], y=J2[1],z=J2[2]),Joint(x=J3[0], y=J3[1],z=J3[2]))

        # Hip-Leg-Right Angle:
        J1 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_HIP_CENTER].split(',')]
        J2 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_HIP_RIGHT].split(',')]
        J3 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_KNEE_RIGHT].split(',')]
        angles[Projections.ANGLE_HIP_LEG_R] = calculateAngleProjection(Joint(x=J1[0], y=J1[1],z=J1[2]),Joint(x=J2[0], y=J2[1],z=J2[2]),Joint(x=J3[0], y=J3[1],z=J3[2]))

        # Hip-Leg-Left Angle:
        J1 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_HIP_CENTER].split(',')]
        J2 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_HIP_LEFT].split(',')]
        J3 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_KNEE_LEFT].split(',')]
        angles[Projections.ANGLE_HIP_LEG_L] = calculateAngleProjection(Joint(x=J1[0], y=J1[1],z=J1[2]),Joint(x=J2[0], y=J2[1],z=J2[2]),Joint(x=J3[0], y=J3[1],z=J3[2]))

        # Leg-Leg-Right Angle:
        J1 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_HIP_RIGHT].split(',')]
        J2 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_KNEE_RIGHT].split(',')]
        J3 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_FOOT_RIGHT].split(',')]
        angles[Projections.ANGLE_LEG_LEG_R] = calculateAngleProjection(Joint(x=J1[0], y=J1[1],z=J1[2]),Joint(x=J2[0], y=J2[1],z=J2[2]),Joint(x=J3[0], y=J3[1],z=J3[2]))

        # Leg-Leg-Left Angle:
        J1 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_HIP_LEFT].split(',')]
        J2 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_KNEE_LEFT].split(',')]
        J3 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_FOOT_LEFT].split(',')]
        angles[Projections.ANGLE_LEG_LEG_L] = calculateAngleProjection(Joint(x=J1[0], y=J1[1],z=J1[2]),Joint(x=J2[0], y=J2[1],z=J2[2]),Joint(x=J3[0], y=J3[1],z=J3[2]))

        # Arm-Hip-Right Angle:
        J1 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_ELBOW_RIGHT].split(',')]
        J2 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_SHOULDER_RIGHT].split(',')]
        J3 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_HIP_RIGHT].split(',')]
        angles[Projections.ANGLE_ARM_HIPLINE_R] = calculateAngleProjection(Joint(x=J1[0], y=J1[1],z=J1[2]),Joint(x=J2[0], y=J2[1],z=J2[2]),Joint(x=J3[0], y=J3[1],z=J3[2]))

        # Arm-Hip-Left Angle:
        J1 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_ELBOW_LEFT].split(',')]
        J2 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_SHOULDER_LEFT].split(',')]
        J3 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_HIP_LEFT].split(',')]
        angles[Projections.ANGLE_ARM_HIPLINE_L] = calculateAngleProjection(Joint(x=J1[0], y=J1[1],z=J1[2]),Joint(x=J2[0], y=J2[1],z=J2[2]),Joint(x=J3[0], y=J3[1],z=J3[2]))

        # Thigh-Hipline-Right
        J1 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_HIP_LEFT].split(',')]
        J2 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_HIP_RIGHT].split(',')]
        J3 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_KNEE_RIGHT].split(',')]
        angles[Projections.ANGLE_THIGH_HIPLINE_R] = calculateAngleProjection(Joint(x=J1[0], y=J1[1],z=J1[2]),Joint(x=J2[0], y=J2[1],z=J2[2]),Joint(x=J3[0], y=J3[1],z=J3[2]))

        # Thigh-Hipline-Left
        J1 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_HIP_RIGHT].split(',')]
        J2 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_HIP_LEFT].split(',')]
        J3 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_KNEE_LEFT].split(',')]
        angles[Projections.ANGLE_THIGH_HIPLINE_L] = calculateAngleProjection(Joint(x=J1[0], y=J1[1],z=J1[2]),Joint(x=J2[0], y=J2[1],z=J2[2]),Joint(x=J3[0], y=J3[1],z=J3[2]))
        angleslist.append(angles)
    c.executemany('''INSERT INTO angles VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', angleslist)
    conn.commit()
    conn.close()
    print("[!]Table angles added/updated")


data = [["mov1","1,1,1","2,2,2","3,3,3","4,4,4","5,5,5","1,1,1","2,2,2","3,3,3","4,4,4","5,5,5","1,1,1","2,2,2","3,3,3","4,4,4","5,5,5","1,1,1","2,2,2","3,3,3","4,4,4","5,5,5"],
        ["mov2","1,1,1","2,2,2","3,3,3","4,4,4","5,5,5","1,1,1","2,2,2","3,3,3","4,4,4","5,5,5","1,1,1","2,2,2","3,3,3","4,4,4","5,5,5","1,1,1","2,2,2","3,3,3","4,4,4","5,5,5"]
        ]

#savePointsDB(data)
saveAnglesDB("mov2")

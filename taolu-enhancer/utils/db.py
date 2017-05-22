import sqlite3
import numpy as np
from utils.angle_calculator import calculateAngleProjection,Joint, obtainAngles
from utils.definitions import Projections,Joints

def getAnglesDB():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM angles")
    return c.fetchall()

def saveJointsDB(data):
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
    c.execute('''INSERT INTO joints VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', data)
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
    c.execute('DELETE FROM angles WHERE move = "'+move+'"')
    c.execute('SELECT HIP_CENTER,SPINE,SHOULDER_CENTER,HEAD,'
                'SHOULDER_LEFT,ELBOW_LEFT,WRIST_LEFT,HAND_LEFT,'
                'SHOULDER_RIGHT,ELBOW_RIGHT,WRIST_RIGHT,HAND_RIGHT,'
                'HIP_LEFT,KNEE_LEFT,ANKLE_LEFT,FOOT_LEFT,HIP_RIGHT,'
                'KNEE_RIGHT,ANKLE_RIGHT,FOOT_RIGHT '
                'FROM joints WHERE move = "'+move+'"')

    jointslist = c.fetchall()
    angleslist = obtainAngles(jointslist, move)
    c.executemany('''INSERT INTO angles VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', angleslist)
    conn.commit()
    conn.close()
    print("[!]Table angles added/updated")


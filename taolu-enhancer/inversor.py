import sqlite3
import numpy as np

conn = sqlite3.connect('database.db') #connection object
c = conn.cursor()
# Create table

c.execute('SELECT move,HIP_CENTER,SPINE,SHOULDER_CENTER,HEAD,'
            'SHOULDER_LEFT,ELBOW_LEFT,WRIST_LEFT,HAND_LEFT,'
            'SHOULDER_RIGHT,ELBOW_RIGHT,WRIST_RIGHT,HAND_RIGHT,'
            'HIP_LEFT,KNEE_LEFT,ANKLE_LEFT,FOOT_LEFT,HIP_RIGHT,'
            'KNEE_RIGHT,ANKLE_RIGHT,FOOT_RIGHT '
            'FROM joints')

joints_array = np.array(c.fetchall())
joints_array = np.hstack((joints_array[:,:1],np.fliplr(joints_array[:,1:])))


c.execute("DELETE from joints")
conn.commit()

c.execute('SELECT move,HIP_CENTER,SPINE,SHOULDER_CENTER,HEAD,'
            'SHOULDER_LEFT,ELBOW_LEFT,WRIST_LEFT,HAND_LEFT,'
            'SHOULDER_RIGHT,ELBOW_RIGHT,WRIST_RIGHT,HAND_RIGHT,'
            'HIP_LEFT,KNEE_LEFT,ANKLE_LEFT,FOOT_LEFT,HIP_RIGHT,'
            'KNEE_RIGHT,ANKLE_RIGHT,FOOT_RIGHT '
            'FROM joints')
joints_array_vacia = np.array(c.fetchall())
print(joints_array_vacia)
joints_array = joints_array.tolist()

c.executemany('''INSERT INTO joints VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', joints_array)
conn.commit()
conn.close()
print("[!]Table joints added/updated")



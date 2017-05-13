import sqlite3

def saveDB(data):
    conn = sqlite3.connect('database.db') #connection object
    c = conn.cursor()
    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS points
                (n_sample INTEGER PRIMARY KEY,
                form TEXT NOT NULL,
                HIP_CENTER TEXT NOT NULL,
                SPINE REAL NOT NULL,
                SHOULDER_CENTER NOT NULL,
                HEAD NOT NULL,
                SHOULDER_LEFT NOT NULL,
                ELBOW_LEFT NOT NULL,
                WRIST_LEFT NOT NULL,
                HAND_LEFT NOT NULL,
                SHOULDER_RIGHT NOT NULL,
                ELBOW_RIGHT NOT NULL,
                WRIST_RIGHT NOT NULL,
                HAND_RIGHT NOT NULL,
                HIP_LEFT NOT NULL,
                KNEE_LEFT NOT NULL,
                ANKLE_LEFT NOT NULL,
                FOOT_LEFT NOT NULL,
                HIP_RIGHT NOT NULL,
                KNEE_RIGHT NOT NULL,
                ANKLE_RIGHT NOT NULL,
                FOOT_RIGHT NOT NULL)
                ''')
    c.executemany('''INSERT INTO points VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', data)
    conn.commit()
    conn.close()
    print("[!]Table points added/updated")

data = [["form1","1,1,1","2,2,2","3,3,3","4,4,4","5,5,5","1,1,1","2,2,2","3,3,3","4,4,4","5,5,5","1,1,1","2,2,2","3,3,3","4,4,4","5,5,5","1,1,1","2,2,2","3,3,3","4,4,4","5,5,5"],
        ["form2","1,1,1","2,2,2","3,3,3","4,4,4","5,5,5","1,1,1","2,2,2","3,3,3","4,4,4","5,5,5","1,1,1","2,2,2","3,3,3","4,4,4","5,5,5","1,1,1","2,2,2","3,3,3","4,4,4","5,5,5"]
        ]

saveDB(data)

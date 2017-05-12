import numpy as np
from collections import namedtuple
from definitions import Joints
import sqlite3

def calculateAngleProjection(central, superior, inferior):
    # Build vectors based on request
    sup_vector = np.array([superior.x - central.x, superior.y - central.y, superior.z - central.z])
    inf_vector = np.array([inferior.x - central.x, inferior.y - central.y, inferior.z - central.z])

    cos_angle = np.dot(sup_vector, inf_vector)/(np.linalg.norm(sup_vector)*np.linalg.norm(inf_vector))
    cos_angle = float('%.5f'%(cos_angle))
    angle = np.arccos(cos_angle)

    return angle
    
OFFSET = 0.1
Joint = namedtuple('Joint', ['x', 'y', 'z'])



    

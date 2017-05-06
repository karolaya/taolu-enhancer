import numpy as np
from collections import namedtuple
from definitions import Joints
from definitions import Projections

Joint = namedtuple('Joint', ['x', 'y', 'z'])

def calculateAngleProjection(central, superior, inferior):
    # Build vectors based on request
    sup_vector = np.array([superior.x - central.x, superior.y - central.y, superior.z - central.z])
    inf_vector = np.array([inferior.x - central.x, inferior.y - central.y, inferior.z - central.z])

    angle = np.dot(sup_vector, inf_vector)/(np.linalg.norm(sup_vector)*np.linalg.norm(inf_vector))

    return angle
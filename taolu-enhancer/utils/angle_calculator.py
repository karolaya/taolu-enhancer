import numpy as np
from collections import namedtuple
from utils.definitions import Projections,Joints

import sqlite3

def obtainAngles(jointslist, move):
    angleslist = []
    for i in range(len(jointslist)):
        angles = ["",0,0,0,0,0,0,0,0,0,0,0,0,0]
        angles[0] = move
        # Neck-Head Angle:
        J3 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_SPINE].split(',')]
        J2 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_SHOULDER_CENTER].split(',')]
        J1 = [float(i) for i in jointslist[i][Joints.NUI_SKELETON_POSITION_HEAD].split(',')]
        
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

    #print(angleslist)
    return angleslist

def calculateAngleProjection(inferior, central, superior):
    # Build vectors based on request
    sup_vector = np.array([superior.x - central.x, superior.y - central.y, superior.z - central.z])
    inf_vector = np.array([inferior.x - central.x, inferior.y - central.y, inferior.z - central.z])

    cos_angle = np.dot(sup_vector, inf_vector)/(np.linalg.norm(sup_vector)*np.linalg.norm(inf_vector))
    cos_angle = float('%.5f'%(cos_angle))
    angle = np.arccos(cos_angle)

    if np.isnan(angle):
        return 0

    return angle
    
OFFSET = 0.1
Joint = namedtuple('Joint', ['x', 'y', 'z'])



    

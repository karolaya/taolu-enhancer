import cv2
import numpy as np
import matplotlib.pyplot as mplt

A = np.zeros((32,32))

"""
A = np.array([[1,2,3,4,5,6,7,8,9,10],
              list(reversed([1,2,3,4,5,6,7,8,9,10])),
              [1,2,3,4,5,6,7,8,9,10],
              list(reversed([1,2,3,4,5,6,7,8,9,10])),
              [1,2,3,4,5,6,7,8,9,10],
              list(reversed([1,2,3,4,5,6,7,8,9,10])),
              [1,2,3,4,5,6,7,8,9,10],
              list(reversed([1,2,3,4,5,6,7,8,9,10])),
              [1,2,3,4,5,6,7,8,9,10],
              list(reversed([1,2,3,4,5,6,7,8,9,10]))
              ],dtype = np.uint8)
"""
mplt.figure()
mplt.imshow(A)
mplt.show()

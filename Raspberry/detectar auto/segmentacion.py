import cv2
import numpy as np
import math as m
from matplotlib import pyplot as plt

for i in range(0,1):
    directorio = "nombre1.jpg"
    a = cv2.imread(directorio)
    rgB = np.matrix(a[:,:,0])
    rGb = np.matrix(a[:,:,1])
    Rgb = np.matrix(a[:,:,2])
    I = cv2.absdiff(Rgb,rGb)
    II = I
    #cv2.imshow("", II)
    #cv2.waitKey(0)
    [fil, col] = I.shape
    for o in range(0, fil):
        for oo in range(0, col):
            if I[o, oo]<100:
                I[o, oo] = 0
    for o in range(0, fil):
        for oo in range(0, col):
            if I[o, oo]>50:
                I[o, oo] = 1
    cv2.imshow("", I*255)
    cv2.waitKey(0)
    """
    if i==0:
        se = np.ones((50,50), np.uint8)
        se2 = np.ones((10,10), np.uint8)
    closing = cv2.morphologyEx(I, cv2.MORPH_CLOSE, se)
    dilation = cv2.dilate(closing, se2, 1)
    """

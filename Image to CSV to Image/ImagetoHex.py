import cv2

import numpy as np
import os
if os.path.exists('csvfile.csv'):
    os.remove('csvfile.csv')

in_image = cv2.imread("input.png",-1)

height , width = in_image.shape[:2]
lresult = []

c =0
for h in range(height-1):
    lresult =[]
    for w in range(width-1):

        b = in_image[h][w][0]
        g = in_image[h][w][1]
        r = in_image[h][w][2]
        p = in_image[h][w][3]
        a = str(hex(b)[2:] if len(hex(b)[2:])==2 else '0'+hex(b)[2:])
        a = a+ str(hex(g)[2:] if len(hex(g)[2:])==2 else '0'+hex(g)[2:])
        a = a+ str(hex(r)[2:] if len(hex(r)[2:])==2 else '0'+hex(r)[2:])
        a = a+ str(hex(p)[2:] if len(hex(p)[2:])==2 else '0'+hex(p)[2:])
        a ="'" +a +"'"

        lresult.append(a)

    with open('csvfile.csv','a') as f:
        f.write(','.join(lresult))
        f.write('\n')
        c= c+1
        print c

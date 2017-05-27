import cv2
import numpy as np
import csv

reader = csv.reader(open("csvfile.csv", "rb"), delimiter=",")
x = list(reader)
result = np.array(x).astype("string")
height ,width = result.shape

size = height,width,4
img = np.zeros(size,dtype=np.uint8)

for h in range(height-1):
    for w in range(width-1):
        val = result[h][w]
        img[h][w][0]=int(result[h][w][1:3],16)
        img[h][w][1] =int(result[h][w][3:5],16)
        img[h][w][2] =int(result[h][w][5:7],16)
        img[h][w][3]=int(result[h][w][7:9],16)

cv2.imwrite('output.png',img)

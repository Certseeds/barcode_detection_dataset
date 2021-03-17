import cv2
import numpy as np
from typing import List
import os
import matplotlib.pyplot as plt



def rotate_bound(image, angle):
    # grab the dimensions of the image and then determine the
    # center
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
 
    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
 
    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))
 
    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
 
    # perform the actual rotation and return the image
    return cv2.warpAffine(image, M, (nW, nH))

if __name__ == '__main__':
    path: List = "C:\\Users\\nanos\\repo\\barcode_detection_dataset\\pictures\\images\\20210317_2\\"
    resize_dir = path + "90\\"
    #os.mkdir(resize_dir)
    for i in os.listdir(path):
        if len(i) < 4:
            continue
        print(i)
        img = cv2.imread(path + i)
        img90 = rotate_bound(img, 270)
        # plt.imshow(img, cmap='gray')
        # plt.show()
        # plt.imshow(img, cmap='gray')
        # plt.show()
        cv2.imwrite(resize_dir + i, img90)

#!/usr/bin/env python3
# coding=utf-8
import cv2
import os
import matplotlib.pyplot as plt

if __name__ == '__main__':
    path: str = "./images/20210316_2"
    resize_dir: str = path + "/resize"
    os.mkdir(resize_dir)
    for i in os.listdir(path):
        print(i)
        img = cv2.imread(path + i)
        # plt.imshow(img, cmap='gray')
        # plt.show()
        img = cv2.resize(img, (480, 640))
        # plt.imshow(img, cmap='gray')
        # plt.show()
        cv2.imwrite(resize_dir + i, img)

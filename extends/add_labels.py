#!/usr/bin/env python3
# coding=utf-8
'''
Github: https://github.com/Certseeds/barcode_detection_dataset
Author: nanoseeds
'''
import math
import pathlib
import random
import string

import cv2
import numpy as np
from barcode import EAN13, EAN8, JAN, UPCA, Code128
from barcode.writer import ImageWriter


def main() -> None:
    for i in range(0, 4, 1):
        temp = randomImage(i)
        cv2.imshow("x", rotate(temp))
        cv2.waitKey(0)
    subFolder = pathlib.Path('./origins/imagenet_2012_n07248320')
    count = 0
    for img in subFolder.iterdir():
        print(img.iterdir)
        count += 1
        image = cv2.imread(str(img.absolute()))
        image, shape = draw_barcode_to_picture(image)
        # cv2.rectangle(image, (shape[0] - shape[2] // 2, shape[1] - shape[3] // 2),(shape[0] + shape[2] // 2, shape[1] + shape[3] // 2), (255, 0, 0))
        # cv2.imshow("x", image)
        # cv2.waitKey(0)
        with open(str(img.absolute()).replace("origins", "labels").replace("JPEG", "txt"), "w+") as file:
            file.write(f"0 {shape[0]:.6f} {shape[1]:.6f} {shape[2]:.6f} {shape[3]:.6f}\n")
        cv2.imwrite(str(img.absolute()).replace("origins", "images"), image)


# Our barcode is ready. Let's save it.


def draw_barcode_to_picture(img: np.ndarray):
    randomBarcode = randomImage(random.randint(0, 3))
    image2 = rotate(randomBarcode)
    height2, weight2 = 300, 300
    img = cv2.resize(img, (600, 600))
    randomX = random.randint(0, 300)
    randomY = random.randint(0, 300)
    img[randomX:height2 + randomX, randomY:weight2 + randomY, :] = cv2.resize(image2, (weight2, height2))
    return img, ((randomY + weight2 // 2) / 600, (randomX + height2 // 2) / 600, weight2 / 600, height2 / 600)


def randomImage(number: int = -1) -> np.ndarray:
    randomInt = random.randint(0, 3)
    if number != -1:
        randomInt = number
    if randomInt == 0:
        return randomEAN13()
    elif randomInt == 1:
        return randomEAN8()
    elif randomInt == 2:
        return randomUPC()
    elif randomInt == 3:
        return randomCode128()
    pass


def randomEAN13() -> np.ndarray:
    number = ''.join(random.choice(string.digits) for i in range(12))
    my_code = EAN13(number, writer=ImageWriter())
    my_code.save("new_code", None, None)
    temp = cv2.imread("new_code.png")
    temp = temp[0:220, 40:480]
    return temp


def randomEAN8() -> np.ndarray:
    number = ''.join(random.choice(string.digits) for i in range(7))
    my_code = EAN8(number, writer=ImageWriter())
    my_code.save("new_code", None, None)
    temp = cv2.imread("new_code.png")
    temp = temp[0:220, 40:374]
    return temp


def randomUPC() -> np.ndarray:
    number = ''.join(random.choice(string.digits) for i in range(11))
    my_code = UPCA(number, writer=ImageWriter())
    my_code.save("new_code", None, None)
    temp = cv2.imread("new_code.png")
    temp = temp[0:220, 40:480]
    return temp


def randomCode128() -> np.ndarray:
    number = ''.join(random.choice(string.digits + string.ascii_letters) for i in range(13))
    my_code = Code128(number, writer=ImageWriter())
    my_code.save("new_code", None, None)
    temp = cv2.imread("new_code.png")
    temp = temp[0:220, 0:480]
    return temp


def rotate(img: np.ndarray) -> np.ndarray:
    return rotate_image(img, random.randint(0, 360))


# come from
# https://stackoverflow.com/questions/22041699/rotate-an-image-without-cropping-in-opencv-in-c
def rotate_image(mat, angle):
    height, width = mat.shape[:2]
    image_center = (width / 2, height / 2)

    rotation_mat = cv2.getRotationMatrix2D(image_center, angle, 1)

    radians = math.radians(angle)
    sin = math.sin(radians)
    cos = math.cos(radians)
    bound_w = int((height * abs(sin)) + (width * abs(cos)))
    bound_h = int((height * abs(cos)) + (width * abs(sin)))

    rotation_mat[0, 2] += ((bound_w / 2) - image_center[0])
    rotation_mat[1, 2] += ((bound_h / 2) - image_center[1])

    rotated_mat = cv2.warpAffine(mat, rotation_mat, (bound_w, bound_h), borderValue=(0, 0, 0))
    return rotated_mat


if __name__ == '__main__':
    main()

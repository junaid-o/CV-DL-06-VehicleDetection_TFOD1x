## Bulk Image resizer

# USAGE: Place this script in the folder containing the images to be resized
# and then run it

from configparser import Interpolation
from email.mime import image
from turtle import width
import numpy as np
import cv2
import os

dir_path= os.getcwd()

print(dir_path)

width =640
height = 640

dim = (width, height)

def main():
    for filename in os.listdir(dir_path):

        # If the images are not in .JPG, change the format below
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png") or filename.endswith(".JPG"):
            image = cv2.imread(filename)

            print(filename)

            resized = cv2.resize(image, dim, Interpolation= cv2.INTER_AREA)
            cv2.imwrite(filename, resized)

main()            

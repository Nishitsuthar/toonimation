import cv2
import easygui
import numpy as np
import imageio
import sys
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk

# now lets create the simple box which hold the path string of our file or Image
def upload_file():
    path_of_image = easygui.fileopenbox()
    toonify(path_of_image)


# for now i successfully upload the image and its time to load the image into Program
def toonify(path_of_image):
    # read the image
    original_image = cv2.imread(path_of_image)
    original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
    # print(original_image) image is stored in form of numbers


    if original_image is None:
        print("Can not find the image please, Choose the appropriate file")
        sys.exit()

    resize_image1 = cv2.resize(original_image, (960, 540))
    plt.show(resize_image1, cmap="gray")

    grayScaleImage = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    resize_image2 = cv2.resize(original_image, (960, 540))
    plt.show(resize_image2, cmap="gray")

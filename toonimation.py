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

# main window
top = tk.Tk()
top.geometry("400x400")
top.title("Toonimation")
top.configure(background="gray")
label = Label(top, background="#CDCDCD", font=("Noto sans", 20, "bold"))

# now lets create the simple box which hold the path string of our file or Image
def upload_file():
    path_of_image = easygui.fileopenbox()
    toonify(path_of_image)


# for now i successfully upload_file the image and its time to load the image into Program
def toonify(path_of_image):
    # read the image
    original_image = cv2.imread(path_of_image)
    original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
    # print(original_image) image is stored in form of numbers

    if original_image is None:
        print("Can not find the image please, Choose the appropriate file")
        sys.exit()

    resize_image1 = cv2.resize(original_image, (960, 540))
    # plt.show(resize_image1, cmap="gray")

    grayScaleImage = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    resize_image2 = cv2.resize(grayScaleImage, (960, 540))
    # plt.show(resize_image2, cmap="gray")

    # smoothing the Image
    smoothGrayScale = cv2.medianBlur(grayScaleImage, 5)
    resize_image3 = cv2.resize(smoothGrayScale, (960, 540))

    # this spet retrive the edges of an Image
    get_edge = cv2.adaptiveThreshold(
        smoothGrayScale, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9
    )
    resize_image4 = cv2.resize(get_edge, (960, 540))

    color_image = cv2.bilateralFilter(original_image, 9, 300, 300)
    resize_image5 = cv2.resize(color_image, (960, 540))

    cartoon_image = cv2.bitwise_and(color_image, color_image, mask=get_edge)
    resize_image6 = cv2.resize(cartoon_image, (960, 540))

    images = [
        resize_image1,
        resize_image2,
        resize_image3,
        resize_image4,
        resize_image5,
        resize_image6,
    ]

    fig, axes = plt.subplots(
        3,
        2,
        figsize=(8, 8),
        subplot_kw={"xticks": [], "yticks": []},
        gridspec_kw=dict(hspace=0.1, wspace=0.1),
    )

    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i], cmap="gray")

    save1 = Button(
        top,
        text="Save cartoon image",
        command=lambda: save_image(path_of_image, resize_image6),
        padx=30,
        pady=5,
    )
    save1.configure(
        background="#364156", foreground="white", font=("calibri", 10, "bold")
    )
    save1.pack(side=TOP, pady=50)

    plt.show()


def save_image(resize_image6, path_of_image):
    # imwrite() is used for saving an image
    new_name = "Toonimated_Image"
    path1 = os.path.dirname(path_of_image)
    extension = os.path.splitext(path_of_image)[1]
    path = os.path.join(path1, new_name + extension)
    cv2.imwrite(path, cv2.cvtColor(resize_image6, cv2.COlOR_RGB2BGR))
    I = "Image saved by name " + new_name + "at" + path
    tk.messagebox.showinfo(title=None, message=I)


# button in the middle of the screen
upload_file = Button(
    top, text="Cartoonify an Image", command=upload_file, padx=10, pady=5
)
upload_file.configure(
    background="#364156", foreground="white", font=("calibri", 10, "bold")
)
upload_file.pack(side=TOP, pady=50)


top.mainloop()

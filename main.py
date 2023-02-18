import cv2 #for image processing
import easygui #to open the filebox
import numpy as np #to store image
import imageio #to read image stored at particular path
import sys
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

def upload():
    ImagePath = easygui.fileopenbox(title="Cartoonify Image")
    cartoonify(ImagePath)

def cartoonify(ImagePath):
    originalImage = cv2.imread(ImagePath)
    originalImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2RGB)

    if originalImage is None:
        print("Image not found")
        sys.exit()

    resize1 = cv2.resize(originalImage, (540,540))
    #plt.imshow(resize1, cmap="gray")

    grayScaleImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    resize2 = cv2.resize(grayScaleImage, (540, 540))
    #plt.imshow(resize2, cmap="gray")

    smoothGrayScale = cv2.medianBlur(grayScaleImage, 5)
    resize3 = cv2.resize(smoothGrayScale, (540, 540))
    #plt.imshow(resize3, cmap="gray")

    getEdge = cv2.adaptiveThreshold(smoothGrayScale, 255, 
                    cv2.ADAPTIVE_THRESH_MEAN_C, 
                    cv2.THRESH_BINARY, 25, 25)

    resize4 = cv2.resize(getEdge, (540, 540))
    #plt.imshow(resize4, cmap='gray')

    colorImage = cv2.bilateralFilter(originalImage, 9, 300, 300)
    resize5 = cv2.resize(colorImage, (540, 540))
    #plt.imshow(resize5, cmap='gray')

    cartoonImage = cv2.bitwise_and(colorImage, colorImage, mask=getEdge)
    resize6 = cv2.resize(cartoonImage, (540, 540))
    #plt.imshow(resize6, cmap='gray')

    images=[resize1, resize2, resize3, resize4, resize5, resize6]
    fig, axes = plt.subplots(3,2, figsize=(8,8), subplot_kw={'xticks':[], 'yticks':[]}, gridspec_kw=dict(hspace=0.1, wspace=0.1))
    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i], cmap='gray')
    #save button code
    plt.show()


upload()

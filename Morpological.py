import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('morpological.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernal = np.ones((5,5), np.uint8)

dilation = cv2.dilate(mask, kernal, iterations=5)
erosion = cv2.erode(mask, kernal, iterations=5)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal) #MORPH_OPEN=erosion then dilation
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal) #MORPH_CLOSE=dilation then erosion
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal) #MORPH_GRADIENT=differentiation between erosion and dilation
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal) #MORPH_TOPHAT=differentiation between opening and closing

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
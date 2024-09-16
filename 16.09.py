import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt

def plotting(im):

    img = cv.imread(im, cv.IMREAD_COLOR)
    img = img[...,::-1] # to RGB

    small = cv.resize(img, (0,0), fx=0.125, fy=0.125)
    small_1 = cv.resize(img, (0,0), fx=0.125, fy=0.125, interpolation=cv.INTER_AREA)
    small_2 = cv.resize(img, (0,0), fx=0.125, fy=0.125, interpolation=cv.INTER_LANCZOS4)
    small_3 = cv.resize(img, (0,0), fx=0.125, fy=0.125, interpolation=cv.INTER_NEAREST)    
    
    A = np.zeros((int((img.shape)[0]/8),int((img.shape[1]/8)),3))

    for r in range(0,int((np.array(img.shape)/8)[0])):
        for i in range(0,int((np.array(img.shape)/8)[1])):
            A[r,i,0] = img[r*8,i*8,0]
            A[r,i,1] = img[r*8,i*8,1]
            A[r,i,2] = img[r*8,i*8,2]

    blur = cv.GaussianBlur(A,(9,9),0)
    
    titles = ["original", "resize 1/8", "resize 1/8 with INTER_AREA", "resize 1/8 with INTER_LANCZOS4", "resize 1/8 with INTER_NEAREST", "resize 1/8 with Gaussian"]
    images = [img, small, small_1, small_2, small_3, blur]
    
    for i in range(6):
        plt.subplot(2, 3 , i + 1)
        plt.title(titles[i])
        plt.imshow(images[i]/255)

    plt.show()

plotting("mwa.jpg")

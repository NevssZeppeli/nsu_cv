import cv2 as cv
img = cv.imread("/home/nevss/Загрузки/photo_2022-05-12_19-01-32.jpg")

cv.imshow("Display window", img)
k = cv.waitKey(0) # Wait for a keystroke in the window

import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
print(kernel)
path = "D:\SEM 6\Comp_vision\Programs\Sample_Images\Sample8.jpg"
img =cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(imgBlur,100,200)
cv2.imwrite("Output8.jpg",imgCanny)
cv2.waitKey(0)

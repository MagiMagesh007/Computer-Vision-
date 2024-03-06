import cv2
img = cv2.imread(r"D:\SEM 6\Comp_vision\Programs\Sample_Images\Pagani.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
orb = cv2.ORB_create(nfeatures=2000)
kp = orb.detect(gray, None)
kp, des = orb.compute(gray, kp)
img1 = cv2.drawKeypoints(gray, kp, None, (0,0,255), flags=0)
cv2.imwrite("Output35_ORB_Keypoints.jpg", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
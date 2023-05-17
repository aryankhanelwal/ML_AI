import cv2

img = cv2.imread('myselfie.png')
img2 = cv2.imread('firstimg.png')
img2 = img2[0:255,0:255,:]
img2.shape
# hell = cv2.add(img,img2)
# cv2.imshow('contact',hell)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)
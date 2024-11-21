import cv2
import numpy as np
image_path = "C:/Users/ADMIN/Downloads/SampleImage.jfif"
img = cv2.imread(image_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.ones((3, 3), np.uint8)
eroded_image = cv2.erode(gray, kernel, iterations=1)
cv2.imshow('Original Image', gray)
cv2.waitKey(0)
cv2.imshow('Eroded Image', eroded_image) 
cv2.imwrite('eroded_image.jpg', eroded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

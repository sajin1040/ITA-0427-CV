import cv2
import numpy as np

src_image = cv2.imread("C:/Users/ADMIN/Downloads/SampleImage.jfif")
gray_image = cv2.cvtColor(src_image, cv2.COLOR_BGR2GRAY)

blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
k = 1.5
high_boost_image = cv2.addWeighted(gray_image, 1, blurred_image, -k, 0)

cv2.imshow("Original Image", src_image)
cv2.waitKey(0)
cv2.imshow("High-Boost Sharpened Image", high_boost_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

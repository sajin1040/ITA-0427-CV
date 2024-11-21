import cv2
import numpy as np

src_image = cv2.imread("C:/Users/ADMIN/Downloads/SampleImage.jfif")
gray_image = cv2.cvtColor(src_image, cv2.COLOR_BGR2GRAY)

sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)

sobel_x_abs = np.absolute(sobel_x)
sobel_x_uint8 = np.uint8(sobel_x_abs)

cv2.imshow("Original Image", src_image)
cv2.waitKey(0)
cv2.imshow("Sobel X Edge Detection", sobel_x_uint8)

cv2.waitKey(0)
cv2.destroyAllWindows()

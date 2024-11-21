import cv2
import numpy as np

src_image = cv2.imread("C:/Users/ADMIN/Downloads/SampleImage.jfif")
gray_image = cv2.cvtColor(src_image, cv2.COLOR_BGR2GRAY)

sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)

sobel_y_abs = np.absolute(sobel_y)
sobel_y_uint8 = np.uint8(sobel_y_abs)

cv2.imshow("Original Image", src_image)
cv2.waitKey(0)
cv2.imshow("Sobel Y Edge Detection", sobel_y_uint8)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

src_image = cv2.imread("C:/Users/ADMIN/Downloads/SampleImage.jfif")
gray_image = cv2.cvtColor(src_image, cv2.COLOR_BGR2GRAY)

sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)

gradient_magnitude = cv2.magnitude(sobel_x, sobel_y)
gradient_magnitude = np.uint8(np.clip(gradient_magnitude, 0, 255))

sharpened_image = cv2.addWeighted(gray_image, 1.5, gradient_magnitude, -0.5, 0)

cv2.imshow("Original Image", src_image)
cv2.waitKey(0)
cv2.imshow("Gradient Masking Sharpened Image", sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

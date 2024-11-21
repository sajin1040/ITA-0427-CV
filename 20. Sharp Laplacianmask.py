import cv2
import numpy as np

src_image = cv2.imread("C:/Users/ADMIN/Downloads/SampleImage.jfif")
gray_image = cv2.cvtColor(src_image, cv2.COLOR_BGR2GRAY)

laplacian_kernel = np.array([[0,  1, 0],
                             [1, -4, 1],
                             [0,  1, 0]], dtype=np.float32)

laplacian = cv2.filter2D(gray_image, -1, laplacian_kernel)
sharpened_image = cv2.addWeighted(gray_image, 1.5, laplacian, -0.5, 0)

cv2.imshow("Original Image", src_image)
cv2.waitKey(0)
cv2.imshow("Sharpened Image", sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np
src_image = cv2.imread("C:/Users/ADMIN/Downloads/SampleImage.jfif")
template = cv2.imread("C:/Users/ADMIN/Downloads/SampleImage.jfif", 0) 
gray_image = cv2.cvtColor(src_image, cv2.COLOR_BGR2GRAY)
result = cv2.matchTemplate(gray_image, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
locations = np.where(result >= threshold)
for pt in zip(*locations[::-1]):
    cv2.rectangle(src_image, pt, (pt[0] + template.shape[1], pt[1] + template.shape[0]), (0, 255, 0), 2)
cv2.imshow("Detected Watch", src_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

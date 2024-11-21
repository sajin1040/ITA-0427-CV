import cv2
import numpy as np

src_image = cv2.imread("C:/Users/ADMIN/Downloads/SampleImage.jfif")
dst_image = cv2.imread("C:/Users/ADMIN/Downloads/SampleImage.jfif")

src_points = np.array([[50, 50], [200, 50], [50, 200], [200, 200]], dtype=np.float32)
dst_points = np.array([[60, 60], [220, 70], [70, 220], [230, 230]], dtype=np.float32)

H, status = cv2.findHomography(src_points, dst_points)

transformed_image = cv2.warpPerspective(src_image, H, (dst_image.shape[1], dst_image.shape[0]))

cv2.imshow("Source Image", src_image)
cv2.waitKey(0)
cv2.imshow("Destination Image", dst_image)
cv2.waitKey(0)
cv2.imshow("Transformed Image", transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

import numpy as np
import cv2

def compute_homography_dlt(src_points, dst_points):
    A = []
    for i in range(len(src_points)):
        x, y = src_points[i][0], src_points[i][1]
        x_prime, y_prime = dst_points[i][0], dst_points[i][1]
        A.append([-x, -y, -1, 0, 0, 0, x * x_prime, y * x_prime, x_prime])
        A.append([0, 0, 0, -x, -y, -1, x * y_prime, y * y_prime, y_prime])
    A = np.array(A)
    _, _, Vt = np.linalg.svd(A)
    h = Vt[-1, :]
    H = h.reshape(3, 3)
    return H

def apply_homography(src_image, H, dst_shape):
    return cv2.warpPerspective(src_image, H, (dst_shape[1], dst_shape[0]))

src_image = cv2.imread("C:/Users/ADMIN/Downloads/SampleImage.jfif")
dst_image = cv2.imread("C:/Users/ADMIN/Downloads/SampleImage.jfif")

src_points = np.array([[50, 50], [200, 50], [50, 200], [200, 200]], dtype=np.float32)
dst_points = np.array([[60, 60], [220, 70], [70, 220], [230, 230]], dtype=np.float32)

H = compute_homography_dlt(src_points, dst_points)
transformed_image = apply_homography(src_image, H, dst_image.shape)

cv2.imshow("Source Image", src_image)
cv2.waitKey(0)
cv2.imshow("Destination Image", dst_image)
cv2.waitKey(0)
cv2.imshow("Transformed Image", transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

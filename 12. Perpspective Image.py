import cv2
import numpy as np
image = cv2.imread("C:/Users/ADMIN/Downloads/SampleImage.jfif")
x1, y1 = 100, 100
x2, y2 = 300, 100
x3, y3 = 300, 300
x4, y4 = 100, 300
original_points = np.float32([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
width, height = 200, 400
desired_points = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
matrix = cv2.getPerspectiveTransform(original_points, desired_points)
output_image = cv2.warpPerspective(image, matrix, (width, height))
cv2.imshow('Original Image', image)
cv2.waitKey(0)
cv2.imshow('Transformed Image', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

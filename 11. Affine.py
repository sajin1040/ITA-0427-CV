import cv2
import numpy as np
image = cv2.imread("C:/Users/ADMIN/Downloads/SampleImage.jfif")
angle = 30
scale = 0.5
rotation_matrix = cv2.getRotationMatrix2D((image.shape[1] / 2, image.shape[0] / 2), angle, scale)
transformed_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))
cv2.imshow('Original Image', image)
cv2.imshow('Transformed Image', transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

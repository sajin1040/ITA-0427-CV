import cv2
image = cv2.imread("C:/Users/ADMIN/Downloads/SampleImage.jfif")
flipped_image = cv2.flip(image, 1)
rotated_image = cv2.rotate(flipped_image, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Original Image', image)
cv2.waitKey(0)
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

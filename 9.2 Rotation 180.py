import cv2
image = cv2.imread("C:/Users/ADMIN/Downloads/SampleImage.jfif")
cv2.imshow('original',image)
cv2.waitKey(0)
flipped_horizontally = cv2.flip(image, 1)
rotated_image = cv2.flip(flipped_horizontally, 0)
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


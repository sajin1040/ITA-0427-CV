import cv2
src_image = cv2.imread("C:/Users/ADMIN/Downloads/SampleImage.jfif")
gray_image = cv2.cvtColor(src_image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray_image, 100, 200)
cv2.imshow("Original Image", src_image)
cv2.waitKey(0)
cv2.imshow("Edge Detection", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

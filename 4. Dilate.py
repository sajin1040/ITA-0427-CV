import cv2
import numpy as np
import matplotlib.pyplot as plt
original_image = cv2.imread("C:/Users/ADMIN/Downloads/SampleImage.jfif", cv2.IMREAD_GRAYSCALE)
equalized_image = cv2.equalizeHist(original_image)
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
plt.imshow(original_image, cmap='gray')
plt.title('Original Image')
plt.subplot(1, 2, 2)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image')
plt.show()

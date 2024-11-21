import cv2
import numpy as np
cap = cv2.VideoCapture("C:/Users/ADMIN/Downloads/videoplayback.mp4")
pts1 = np.float32([[200, 300], [5, 2], [0, 4], [6, 0]])
pts2 = np.float32([[0, 0], [4, 0], [0, 1], [4, 6]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)

while True:
    ret, frame = cap.read()
    if not ret: 
        break
    result = cv2.warpPerspective(frame, matrix, (frame.shape[1], frame.shape[0]))
    cv2.imshow('Original Frame', frame)
    cv2.waitKey(1)
    cv2.imshow('Transformed Frame', result)
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()

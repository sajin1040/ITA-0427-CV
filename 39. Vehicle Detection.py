import cv2
vehicle_cascade = cv2.CascadeClassifier("C:/Users/ADMIN/Downloads/cars.xml")
cap = cv2.VideoCapture("C:/Users/ADMIN/Downloads/videoplayback.mp4")
while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break
    for (x, y, w, h) in vehicle_cascade.detectMultiScale(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)):
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow('Detected Vehicles', frame)
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()

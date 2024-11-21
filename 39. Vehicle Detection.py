import cv2
cap = cv2.VideoCapture("C:/Users/ADMIN/Downloads/videoplayback.mp4")
vehicle_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_car.xml')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    for (x, y, w, h) in vehicle_cascade.detectMultiScale(gray, 1.1, 3, minSize=(30, 30)):
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow('Vehicle Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break
cap.release()
cv2.destroyAllWindows()

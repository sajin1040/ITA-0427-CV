import cv2

cap = cv2.VideoCapture(r'C:\Users\ADMIN\Downloads\videoplayback.mp4')  

fps = cap.get(cv2.CAP_PROP_FPS)
speed = 1  
while True:
    ret, frame = cap.read()
    if not ret: break
    
    cv2.imshow('Video', frame)
    
    key = cv2.waitKey(int(1000 / (fps * speed))) & 0xFF
    if key == ord('q'): break 
    if key == ord('f'): speed = 2  
    if key == ord('s'): speed = 0.5 

cap.release()
cv2.destroyAllWindows()

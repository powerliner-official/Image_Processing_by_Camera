# this project is for powerliner academy
import cv2
cap = cv2.VideoCapture(1)
while True :
    ret , frame = cap.read()
    cv2.imshow("powerliner", frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
#you can close camera by [Q]
import cv2
frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture("http://192.168.0.102:8080/video")

cap.set(3,frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)

myColor = [[]]

def findColor(img):
    imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # lower = np.array([h_min,s_min,v_min])
    # upper = np.array([h_max,s_max,v_max])
    # mask = cv2.inRange(imgHsv,lower,upper)
    # cv2.imshow("Img",mask)


while True:
    success, img = cap.read()
    cv2.imshow("Result" , img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break


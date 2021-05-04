import cv2
import datetime
cap = cv2.VideoCapture(0)
# cap instance
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# cap.set(3,3000)
# cap.set(4,3000)
# print(cap.get(3))
# print(cap.get(4))
while True:
    # while True:
    # Read the video
    ret, frame = cap.read()
    if ret == True:
        # Font
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = "Width: " + str(cap.get(3)) + 'Height: '+ str(cap.get(4))
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame,datet,(10, 50),font,1,
                            (0,255,255),2,cv2.LINE_AA)
        # cv2.imshow("frame",frame)
        cv2.imshow("Gray",frame)
        # Stop the loop
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break

cap.release()
# out.release()  #out release|
cv2.destroyAllWindows()

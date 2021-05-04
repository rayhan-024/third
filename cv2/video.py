import cv2
cap = cv2.VideoCapture("http://192.168.0.100:8080/video")
# fourcc connection
forrcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Output.avi',forrcc,20.0,(640,480))
print(cap.isOpened())
while (cap.isOpened()):

    # while True:
    # Read the video
    ret, frame = cap.read()
    if ret == True:
        # cap instance
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # Convert color gray
        # out.write(frame) # fourcc
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # Show the video
        cv2.imshow("frame",frame)
        cv2.imshow("Gray",frame)
        # Stop the loop
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break

cap.release()
out.release()  #out release|
cv2.destroyAllWindows()

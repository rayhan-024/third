
import numpy as np
import  cv2
# img = cv2.imread('lena.jpg')

# Black Image
img = np.zeros([512,512,3],np.uint8)
#
# Draw Line
imges = cv2.line(img,(0,0),(255,255),(147,96,44 ),10)# 237, 14, 129
# Draw arroeline
imges = cv2.arrowedLine (img,(0,255),(255,255),(147,96,44 ),10)# 237, 14, 129
# Draw rectangle
imges = cv2.rectangle(img,(384,0),(510,128),(0,0,255),-1)
# Draw circle
image = cv2.circle(img,(447,63),53,(0,255,0),10)
# Take font
font = cv2.FONT_HERSHEY_SIMPLEX
# Input text
images = cv2.putText(img,"Opencv",(10,500),font,4,(255,255,255),10,cv2.LINE_AA)
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

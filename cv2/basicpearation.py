import numpy as np
import cv2

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')

print(img.shape) #returns a tuple of numbers of rows, columns ,and channels
print(img.size) # Total number of pixels in accessd
print(img.dtype) # Return image datatype is obtained
b,g,r = cv2.split(img)
cv2.merge((b,g,r))
# select the ball
ball = img[280:340,330:390]
# copy this position
img[273:333, 100:160] = ball

img = cv2.resize(img,(512,512))
img2 = cv2.resize(img2,(512,512))

# dst = cv2.add(img2,img) ;

dst = cv2.addWeighted(img,.5,img2,.5,0);


cv2.imshow("image", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

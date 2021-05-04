'''import cv2
import  numpy as np

img  = cv2.imread('gradient.png')

__, th1 = cv2.threshold(img,50,255,cv2.THRESH_BINARY)
__, th2 = cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)
__, th3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
__, th4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
__, th5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

cv2.imshow("Image",img)
cv2.imshow("Th1",th1)
cv2.imshow("Th2",th2)
cv2.imshow("Th3",th3)
cv2.imshow("Th4",th4)
cv2.imshow("Th5",th5)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
import cv2
import  numpy as np
from matplotlib import pyplot as plt
img  = cv2.imread('gradient.png')

__, th1 = cv2.threshold(img,50,255,cv2.THRESH_BINARY)
__, th2 = cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)
__, th3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
__, th4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
__, th5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','Binary','Binaruy_inv','Trunc','Tozero','tozreo_inv']
images = [img,th1,th2,th3,th4,th5]
for i in range(6):
    plt.subplot(2, 3, i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
# cv2.imshow("Image",img)
# cv2.imshow("Th1",th1)
# cv2.imshow("Th2",th2)
# cv2.imshow("Th3",th3)
# cv2.imshow("Th4",th4)
# cv2.imshow("Th5",th5)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
plt.show()
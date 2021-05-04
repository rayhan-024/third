import  cv2
import  numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('smarties.png',cv2.IMREAD_GRAYSCALE)
__, mask = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)
kernal = np.ones((5,5),np.uint8)

dialation = cv2.dilate(mask,kernal,iterations=2)
erosion = cv2.erode(mask,kernal,iterations=1)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal, )
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal, )

titles = ['images','mask','kernal','erosion','opening','closing']
images = [img,mask,dialation,erosion,opening,closing]

for i in range(len(images)):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

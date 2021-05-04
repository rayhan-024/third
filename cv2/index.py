#
import cv2
# Get Images
img = cv2.imread('lena.jpg',-1)

print(img)

# Show images
cv2.imshow("Image",img)
# Time windows
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k ==ord('s'):
    # Copy Images
    cv2.imwrite('lena_copy.png',img)
    cv2.destroyAllWindows()
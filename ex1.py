import cv2
img = cv2.imread('v.jpg',0)
print(img)
cv2.imshow('v',img)
cv2.waitKey(300)
cv2.destroyAllWindows()
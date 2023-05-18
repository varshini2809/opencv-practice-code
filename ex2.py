import cv2
#import numpy as np
img = cv2.imread('v.jpg',0)
print(img)
cv2.imshow('v',img)  #img will store in v
cv2.waitKey(0)  #image will display until u press escape key
cv2.imwrite('quote.jpg',img) #copy of the image
cv2.destroyAllWindows()  
import cv2 
image =cv2.imread("quote.jpg")
resized_image=cv2.resize(image,None,fx=0.005,fy=0.5)
cv2.imshow("Original image",image)
cv2.imshow("Resized image",resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
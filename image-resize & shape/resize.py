import cv2

image = cv2.imread('image-resize & shape\WhatsApp Image 2026-03-16 at 3.39.46 PM.jpeg')


if image is  None:
    print('image not found')

else:
    print('image loaded')

    resized = cv2.resize(image,(300,300))
    cv2.imshow('original image',image)
    cv2.imshow('resized image',resized)
    cv2.waitKey(0)  
    cv2.destroyAllWindows()
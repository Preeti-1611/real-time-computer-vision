import cv2

image = cv2.imread('image-resize & shape\WhatsApp Image 2026-03-16 at 3.39.46 PM.jpeg')
print(image.shape)
if image is not None:
    cropped = image[600:669,1000:1100]
    cv2.imshow('original',image)
    cv2.imshow('cropped',cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:    
    print("Error: Image not found.")
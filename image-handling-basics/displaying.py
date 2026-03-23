import cv2

image = cv2.imread('Phase-1\demo_digram.png.png')

if image is  not None:
    cv2.imshow('loaded image',image)# open the window
    cv2.waitKey(0)# wait until any key is pressed
    cv2.destroyAllWindows() # close the window
else:
    print("Image not found.")
import cv2

image = cv2.imread('Phase-1\demo_digram.png')

if image is not None:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscale Image', gray_image)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()

else:
    print("Error: Image not found.")
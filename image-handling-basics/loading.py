import cv2

image = cv2.imread('Phase-1\demo_digram.png.png')

if image is None:
    print("Error: Image not found.")
else:
    print("Image loaded successfully.")
import cv2
image = cv2.imread('Phase-1\demo_digram.png')

if image is not None:   
    height, width, channels = image.shape
    print(f"Image dimensions: {width} x {height} pixels")  
    print(f"image loaded: \n width: {width} pixels \n height: {height} pixels \n channels: {channels}") 
else:
    print("Error: Image not found.")
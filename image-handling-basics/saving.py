import cv2

image = cv2.imread('Phase-1\demo_digram.png.png')


if image is not None:
    success =cv2.imwrite('Phase-1\saved_image.png', image)
    if success:
        print("Image saved successfully as saved_image.png.")
    else:

      print("failed to  saved successfully.")
else:
    print("Error: Image not found.")    
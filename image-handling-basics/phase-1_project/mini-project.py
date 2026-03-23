import cv2

user = input('user please enter the image file path:')
image = cv2.imread(user)

choice = input('do you want to show the image (1) or save the image (2)? ')

if choice =='1':
    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow('grayscale image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif choice =='2':
    ask = input('please enter the file name u want to save it as')
    
    cv2.imwrite(ask, image)     
    print(f'image saved successfully as {ask}')
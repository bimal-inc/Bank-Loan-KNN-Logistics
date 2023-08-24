
#Bimal Yadav

import cv2
import numpy as np


image_path = 'p.png'
image = cv2.imread(image_path)


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)


edges = cv2.Canny(blurred, threshold1=30, threshold2=150)


contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


for i, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if area > 1000:  
        x, y, w, h = cv2.boundingRect(contour)
        rectangle_image = image[y:y+h, x:x+w]
        orientation = 'vertical' if h > w else 'horizontal'
        
        if orientation == 'vertical':
            rotated_image = cv2.rotate(rectangle_image, cv2.ROTATE_90_CLOCKWISE)
        else:
            rotated_image = rectangle_image
        
      
        window_name = f'Rectangle {i + 1}'
        cv2.imshow(window_name, rotated_image)


cv2.waitKey(0)
cv2.destroyAllWindows()

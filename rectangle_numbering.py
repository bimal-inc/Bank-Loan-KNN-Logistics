
#Bimal Yadav

import cv2
import numpy as np


image_path = 'p.png'
image = cv2.imread(image_path)


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


blurred = cv2.GaussianBlur(gray, (5, 5), 0)

edges = cv2.Canny(blurred, threshold1=30, threshold2=150)


contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


min_contour_area = 1000
aspect_ratios = []
filtered_contours = []
for contour in contours:
    area = cv2.contourArea(contour)
    if area > min_contour_area:
        x, y, w, h = cv2.boundingRect(contour)
        aspect_ratio = w / float(h)
        aspect_ratios.append(aspect_ratio)
        filtered_contours.append(contour)


sorted_indices = np.argsort(aspect_ratios)


for i, index in enumerate(sorted_indices, start=1):
    x, y, w, h = cv2.boundingRect(filtered_contours[index])
    text_x = x + w // 2
    text_y = y + h + 20
    cv2.putText(image, str(i), (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)


cv2.imshow('Numbered Rectangles', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

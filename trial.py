##[Team cuatro]
#[Smart-Traffic management]

import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
im1 = cv2.imread('D:/My_projects/img_gc/4frame0.png')
assert not isinstance(im1,type(None)), 'image not found'

bbox, label, conf = cv.detect_common_objects(im1)
output_image1 = draw_bbox(im1, bbox, label, conf)
plt.imshow(output_image1)
plt.show()
print('Number of cars in cam-1 in the image is '+ str(label.count('car')))

#total = label.count('car')
#2nd image
im2 = cv2.imread('C:/Users/Alex/Downloads/image.png')
assert not isinstance(im2,type(None)), 'image not found'

bbox, label, conf = cv.detect_common_objects(im2)
output_image2 = draw_bbox(im2, bbox, label, conf)
plt.imshow(output_image2)
plt.show()
print('Number of cars in cam-2 in the image is '+ str(label.count('car')))

#total = label.count('car')
#3rd image
im3 = cv2.imread('D:/My_projects/img_gc/pngkuttan.png')
assert not isinstance(im3,type(None)), 'image not found'

bbox, label, conf = cv.detect_common_objects(im3)
output_image3 = draw_bbox(im3, bbox, label, conf)
plt.imshow(output_image3)
plt.show()
print('Number of cars in cam-3 in the image is '+ str(label.count('car')))

#total = label.count('car')
#4th image
im4 = cv2.imread('D:/My_projects/img_gc/traff0.png')
assert not isinstance(im4,type(None)), 'image not found'

bbox, label, conf = cv.detect_common_objects(im4)
output_image4 = draw_bbox(im4, bbox, label, conf)
plt.imshow(output_image4)
plt.show()
print('Number of cars in cam-4 in the image is '+ str(label.count('car')))

#total = label.count('car')
#print(total)


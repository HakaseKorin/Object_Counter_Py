import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox

image = cv2.imread("cars.jpeg")

box, label, count = cv.detect_common_objects(image, model='yolov3-tiny')
output = draw_bbox(image, box, label, count)

plt.imshow(output)
plt.show()
print("Number of cars in this image are "+str(label.count('car')))

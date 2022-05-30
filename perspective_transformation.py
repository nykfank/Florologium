import cv2
from operator import itemgetter
from glob import glob
import numpy as np
#import matplotlib.pyplot as plt

paper = cv2.imread('nikon_current.jpg')
# Coordinates that you want to Perspective Transform
#pts1 = np.float32([[1,136],[348,1],[320,464],[696,205]])
pts1 = np.float32([[100, 0],[696-100, 0],[-100, 464],[696+100,464]])
# Size of the Transformed Image
pts2 = np.float32([[0,0],[696,0],[0,464],[696,464]])
for val in pts1:
    cv2.circle(paper,(val[0],val[1]),5,(0,255,0),-1)
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(paper,M,(696,464))
#plt.imshow(dst)
cv2.imwrite("foo.jpg", dst)
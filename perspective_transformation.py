#!/usr/bin/python3
import cv2, numpy, sys
paper = cv2.imread(sys.argv[1])
bgColor = 255, 255, 255
sy = paper.shape[0]
sx = paper.shape[1]
d1 = int(sx / 3.5) # Top trapezoid points distance to border.
d2 = int(sx / 3) # Shift outside image.
d3 = int(sx / 7) # Crop distance.
pts1 = numpy.float32([[d1-d2, 0], [sx-d1+d2, 0], [-d2, sy], [sx+d2, sy]])
pts2 = numpy.float32([[0, 0], [sx, 0], [0, sy], [sx, sy]])
M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(paper, M, (sx,sy), flags=cv2.INTER_LINEAR, borderValue=bgColor)
crop_img = dst[0:sy, d3:sx-d3]
cv2.imwrite(sys.argv[2], crop_img)

import cv2, numpy, sys

mult = 8 # Size multiplier [8 = full, 1 = scaled for web].
sx = 696*mult # Size horizontal
sy = 464*mult # Size vertical
d1 = 200*mult # Top trapezoid points distance to border.
d2 = 250*mult # Shift outside image.
d3 = 100*mult # Crop distance.

paper = cv2.imread(sys.argv[1])
pts1 = numpy.float32([[d1-d2, 0], [sx-d1+d2, 0], [-d2, sy], [sx+d2, sy]])
pts2 = numpy.float32([[0, 0], [sx, 0], [0, sy], [sx, sy]])
M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(paper, M, (sx,sy), cv2.BORDER_TRANSPARENT)
crop_img = dst[0:sy, d3:sx-d3]
cv2.imwrite(sys.argv[2], crop_img)

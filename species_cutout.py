#!/usr/bin/python3
import cv2, numpy, sys, os
data_file = "%s/Florologium/plant_positions.txt" % os.environ['HOME']
outdir = '%s/cutout' % os.environ['HOME']
xsize = 320
ysize = 240
img = cv2.imread(sys.argv[1])
if not os.path.isdir(outdir): os.mkdir(outdir)

specd = {}
for n, i in enumerate(open(data_file).readlines()):
    if not n: continue
    Species_Name, X_Coordinate, Y_Coordinate, Start_hour, End_hour = i.strip().split('\t')
    specd[Species_Name] = tuple(map(int, [X_Coordinate, Y_Coordinate, Start_hour, End_hour]))

for Species_Name, (X_Coordinate, Y_Coordinate, Start_hour, End_hour) in specd.items():
    crop_img = img[Y_Coordinate:Y_Coordinate+ysize, X_Coordinate:X_Coordinate+xsize]
    outfilename = '%s/%s.jpg' % (outdir, Species_Name)
    cv2.imwrite(outfilename, crop_img)

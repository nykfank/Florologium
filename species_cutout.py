#!/usr/bin/python3
import cv2, numpy, sys, os
data_file = "%s/Florologium/plant_positions.txt" % os.environ['HOME']
outdir = '%s/cutout' % os.environ['HOME']
outurl = 'https://www.florologium.ch/cutout'
outfile_html = '%s/cutout/table.html' % os.environ['HOME']
outfile_marked = '%s/cutout/species_marked.jpg' % os.environ['HOME']

xsize = 400
ysize = 300
xsize_marked = 696
ysize_marked = 464
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
    img = cv2.rectangle(img, (X_Coordinate, Y_Coordinate), (X_Coordinate+xsize, Y_Coordinate+ysize), (0,0,255), 20)
img_small = cv2.resize(img, (xsize_marked, ysize_marked), interpolation = cv2.INTER_AREA)
cv2.imwrite(outfile_marked, img_small)

html = '<p>\n<img src="%s/species_marked.jpg" width="%d" height="%d" alt="Flower positions marked"/>\n</p>\n' % (outurl, xsize_marked, ysize_marked)
for Species_Name, (X_Coordinate, Y_Coordinate, Start_hour, End_hour) in specd.items():
    html += '<p>\n<strong>%s (%dh - %dh)</strong><br/>\n' % (Species_Name, Start_hour, End_hour)
    html += '<img src="%s/%s.jpg" width="%d" height="%d" alt="%s"/>\n</p>' % (outurl, Species_Name, xsize, ysize, Species_Name)
zeit = os.path.splitext(os.path.basename(sys.argv[1]))[0]
zeit2 = '%s-%s-%s %s:%s' % (zeit[0:4], zeit[4:6], zeit[6:8], zeit[9:11], zeit[11:13])
html += '<p>Picture taken at %s</p>\n' % zeit2

open(outfile_html, 'w').write(html)

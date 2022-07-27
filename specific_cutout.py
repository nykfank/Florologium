#!/usr/bin/python3
import cv2, sys, os, cgi, StringIO
form = cgi.FieldStorage()
img_id = form.getvalue('img_id')
# Remove all non digit and underline chars from img_id
sel_species = form.getvalue('species')
data_file = "%s/Florologium/plant_positions.txt" % os.environ['HOME']
xsize = 400
ysize = 300
img_fn = '/mnt/big/katzidien_backup/var/www/florologium/nikon/%s.jpg' % img_id
img = cv2.imread(img_fn)
specd = {}
for n, i in enumerate(open(data_file).readlines()):
    if not n: continue
    Species_Name, X_Coordinate, Y_Coordinate, Start_hour, End_hour = i.strip().split('\t')
    specd[Species_Name] = tuple(map(int, [X_Coordinate, Y_Coordinate, Start_hour, End_hour]))
Species_Name, (X_Coordinate, Y_Coordinate, Start_hour, End_hour) = specd[sel_species]
crop_img = img[Y_Coordinate:Y_Coordinate+ysize, X_Coordinate:X_Coordinate+xsize]
out = StringIO.StringIO()
img.save(out, 'PNG')
print('Content-type: image/png\n\n%s' % out.getvalue())

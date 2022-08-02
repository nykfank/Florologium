#!/usr/bin/python3

data_file = "/home/pi/Florologium/plant_positions.txt"
img_dir = '/var/www/florologium/nikon'
out_dir = '/var/www/florologium/scut'
xsize = 400
ysize = 300

import cv2, sys, os, cgi, datetime

def load_species_positions(data_file):
    specd = {}
    for n, i in enumerate(open(data_file).readlines()):
        if not n: continue
        Species_Name, X_Coordinate, Y_Coordinate, Start_hour, End_hour = i.strip().split('\t')
        specd[Species_Name] = tuple(map(int, [X_Coordinate, Y_Coordinate, Start_hour, End_hour]))
    return(specd)

form = cgi.FieldStorage()
#cgitb.enable()
today = datetime.date.today()
year = int(form.getvalue('year', today.year)) 
mon = int(form.getvalue('mon', today.month))
day = int(form.getvalue('day', today.day - 1))
hour, minute = int(form.getvalue('hour', 12)), int(form.getvalue('minute', 0))
sel_species = form.getvalue('species', 'Gazania')
img_id = '%d%02d%02d_%02d%02d' % (year, mon, day, hour, minute)
out_fn = '%s/%s_%s.png' % (out_dir, sel_species, img_id)
if not os.path.isfile(out_fn):
    img_files = os.listdir(img_dir)
    img_matches = [i for i in img_files if i.startswith(img_id)]
    if len(img_matches) == 1: 
        img_fn = '%s/%s' % (img_dir, img_matches[0])
        img = cv2.imread(img_fn)
        specd = load_species_positions(data_file)
        X_Coordinate, Y_Coordinate, Start_hour, End_hour = specd[sel_species]
        crop_img = img[Y_Coordinate:Y_Coordinate+ysize, X_Coordinate:X_Coordinate+xsize]
    else:
        import numpy
        crop_img = numpy.zeros((ysize, xsize, 3), numpy.uint8)
    cv2.imwrite(out_fn, crop_img)
    img_str = cv2.imencode('.png', crop_img)[1].tobytes()
else:
    img_str = open(out_fn, 'rb').read()

sys.stdout.buffer.write(b"Content-Type: image/png\n\n")
sys.stdout.buffer.write(img_str)

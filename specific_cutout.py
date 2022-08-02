#!/usr/bin/python3
import cv2, sys, os, cgi, numpy, cgitb
form = cgi.FieldStorage()
cgitb.enable()
year, mon, day = int(form.getvalue('year', 2022)), int(form.getvalue('mon', 7)), int(form.getvalue('day', 30))
hour, minute = int(form.getvalue('hour', 15)), int(form.getvalue('minute', 15))
sel_species = form.getvalue('species', 'Gazania')
img_dir = '/mnt/big/katzidien_backup/var/www/florologium/nikon'
img_files = os.listdir(img_dir)
img_id = '%d%02d%02d_%02d%02d' % (year, mon, day, hour, minute)
out_fn = '/var/www/florologium/scut/%s_%s.png' % (sel_species, img_id)
if not os.path.isfile(out_fn):
    img_matches = [i for i in img_files if i.startswith(img_id)]
    assert(len(img_matches) == 1)
    data_file = "/home/pi/Florologium/plant_positions.txt"
    xsize = 400
    ysize = 300
    img_fn = '/var/www/florologium/nikon/%s' % img_matches[0]
    img = cv2.imread(img_fn)
    specd = {}
    for n, i in enumerate(open(data_file).readlines()):
        if not n: continue
        Species_Name, X_Coordinate, Y_Coordinate, Start_hour, End_hour = i.strip().split('\t')
        specd[Species_Name] = tuple(map(int, [X_Coordinate, Y_Coordinate, Start_hour, End_hour]))
    X_Coordinate, Y_Coordinate, Start_hour, End_hour = specd[sel_species]
    crop_img = img[Y_Coordinate:Y_Coordinate+ysize, X_Coordinate:X_Coordinate+xsize]
    cv2.imwrite(out_fn, crop_img)
print('Content-Type: text/html;charset=utf-8\n\n')
print('<html><head><title>Test</title></head><body>\n')
print('<p><img src="http://florologium.ch/scut/%s_%s.png"/></p>' % (sel_species, img_id))
print('</body></html>')
#img_str = cv2.imencode('.png', crop_img)[1].tobytes()
#print('Content-type: image/png\n\n%s' % numpy.array(img_str).tostring())
#out = sys.stdout
#out.write(b"Content-Type: image/png\r\n")
#out.write(numpy.array(img_str).tostring())

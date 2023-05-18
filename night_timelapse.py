#!/usr/bin/python3
# TODO: Use date for filename, then symlink to current video.
indir = '/var/www/box'
outdir = '/tmp/box_1044x696'

fps = 5
nb_hours = 24

import PIL.Image,os,sys,time, shutil, datetime

vidfile = '/var/www/box/box_timelapse_%s.mp4' % datetime.date.today()
vidfile2 = '/var/www/box_timelapse.mp4'
def load_font(fontSize):
 """Load the arial TTF font from the default location for gentoo and debian linux"""
 import PIL.ImageFont
 f1 = '/usr/share/fonts/corefonts/arialbd.ttf' 
 f2 = '/usr/share/fonts/truetype/msttcorefonts/Arial_Bold.ttf'
 if os.path.isfile(f1): font=PIL.ImageFont.truetype(f1,fontSize)
 if os.path.isfile(f2): font=PIL.ImageFont.truetype(f2,fontSize)
 return font

def draw_date(img,txs):
 """Write date and time in the image"""
 import PIL.ImageDraw
 fontSize=int(img.size[1]/20)
 draw = PIL.ImageDraw.Draw(img) # new draw instance 
 arial=load_font(fontSize)
 draw.text((10, 10), txs, fill='white', font=arial)
 return img

files = list(filter(lambda x : x.endswith('.jpg'), sorted(os.listdir(indir))))
filetime = list(map(lambda x : int(time.mktime(time.strptime(x, "%Y%m%d_%H%M%S.jpg"))), files))
mintime = min(filter(lambda x: x > time.time()-nb_hours*60*60, filetime))
start_index = filetime.index(mintime)
if not os.path.isdir(outdir): 
	os.mkdir(outdir)
else:
	for f in os.listdir(outdir): os.unlink('%s/%s' % (outdir, f))
selected_files = files[start_index:]
print('Using %d of %d images.' % (len(selected_files), len(files)))
for f in selected_files: 
	ifn = '%s/%s' % (indir, f)
	ofn = '%s/%s' % (outdir, f)
	shutil.copy(ifn, ofn)
	i = PIL.Image.open(ofn)
	txs = f.replace('.jpg', '').replace('_', ' ')
	i2 = draw_date(i, txs)
	i2.save(ofn)

cmd = "ffmpeg -y -hide_banner -loglevel panic -framerate %d -pattern_type glob -i '%s/*.jpg' -s 1044x696 -c:v libx264 -strict -2 -pix_fmt yuv420p -f mp4 %s" % (fps, outdir, vidfile)
print(cmd)
r = os.popen(cmd)
os.symlink(vidfile, vidfile2)

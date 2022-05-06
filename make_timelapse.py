#!/usr/bin/python3
import sys, os, time
indir = '/home/nyk/nikon_696x464'
outdir = '/home/nyk/nikon_696x464_last24h'
vidfile = '/home/nyk/video/nikon_timelapse.mp4'
nb_img = 12*24
files = sorted(os.listdir(indir))
filetime = list(map(lambda x : int(time.mktime(time.strptime(x, "%Y%m%d_%H%M%S.jpg"))), files))
mintime = min(filter(lambda x: x > time.time()-24*60*60, filetime))
start_index = filetime.index(mintime)
print('Using %d of %d images.' % (len(files)-start_index, len(files)))
if not os.path.isdir(outdir): 
	os.mkdir(outdir)
else:
	for f in os.listdir(outdir): os.unlink('%s/%s' % (outdir, f))
for f in files[start_index:]:
	os.symlink('%s/%s' % (indir, f), '%s/%s' % (outdir, f))
cmd = "ffmpeg -y -hide_banner -framerate 5 -pattern_type glob -i '%s/*.jpg' -c:v libx264 -strict -2 -pix_fmt yuv420p -f mp4 %s" % (outdir, vidfile)
print(cmd)
r = os.popen(cmd)

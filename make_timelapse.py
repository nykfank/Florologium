#!/usr/bin/python3
import sys, os, time
nb_days = int(sys.argv[1])
indir = '/home/nyk/nikon_696x464'
outdir = '/home/nyk/nikon_696x464_%d' % nb_days
vidfile = '/home/nyk/video/nikon_timelapse.mp4'
fps = 5
if nb_days > 1: 
	vidfile = '/home/nyk/video/nikon_timelapse%d.mp4' % nb_days
	fps = 20
files = sorted(os.listdir(indir))
filetime = list(map(lambda x : int(time.mktime(time.strptime(x, "%Y%m%d_%H%M%S.jpg"))), files))
mintime = min(filter(lambda x: x > time.time()-nb_days*24*60*60, filetime))
start_index = filetime.index(mintime)
print('Using %d of %d images.' % (len(files)-start_index, len(files)))
if not os.path.isdir(outdir): 
	os.mkdir(outdir)
else:
	for f in os.listdir(outdir): os.unlink('%s/%s' % (outdir, f))
for f in files[start_index:]:
	os.symlink('%s/%s' % (indir, f), '%s/%s' % (outdir, f))
cmd = "ffmpeg -y -hide_banner -loglevel panic -framerate %d -pattern_type glob -i '%s/*.jpg' -c:v libx264 -strict -2 -pix_fmt yuv420p -f mp4 %s" % (fps, outdir, vidfile)
print(cmd)
r = os.popen(cmd)

#!/usr/bin/python3
import sys, os, time
indir = '/var/www/box'
outdir = '/tmp/box_1044x696'
vidfile = '/var/www/box_timelapse.mp4'
fps = 5
nb_hours = 24
files = sorted(os.listdir(indir))
filetime = list(map(lambda x : int(time.mktime(time.strptime(x, "%Y%m%d_%H%M%S.jpg"))), files))
mintime = min(filter(lambda x: x > time.time()-nb_hours*60*60, filetime))
start_index = filetime.index(mintime)
if not os.path.isdir(outdir): 
	os.mkdir(outdir)
else:
	for f in os.listdir(outdir): os.unlink('%s/%s' % (outdir, f))
selected_files = files[start_index:]
print('Using %d of %d images.' % (len(selected_files), len(files)))
for f in selected_files: os.symlink('%s/%s' % (indir, f), '%s/%s' % (outdir, f))
cmd = "ffmpeg -y -hide_banner -loglevel panic -framerate %d -pattern_type glob -i '%s/*.jpg' -c:v libx264 -strict -2 -pix_fmt yuv420p -f mp4 %s" % (fps, outdir, vidfile)
print(cmd)
r = os.popen(cmd)

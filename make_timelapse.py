#!/usr/bin/python3
# TODO: Add all-time timelapse with images selected by exposure time!
# TODO: Separate day/night!

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
if not os.path.isdir(outdir): 
	os.mkdir(outdir)
else:
	for f in os.listdir(outdir): os.unlink('%s/%s' % (outdir, f))
selected_files = files[start_index:]
if nb_days > 1:	
	del selected_files[::2] # delete every second element
	del selected_files[::2] # delete every second element
if nb_days > 7:
	del selected_files[::2] # delete every second element
	del selected_files[::2] # delete every second element
print('Using %d of %d images.' % (len(selected_files), len(files)))
for f in selected_files: os.symlink('%s/%s' % (indir, f), '%s/%s' % (outdir, f))
cmd = "ffmpeg -y -hide_banner -loglevel panic -framerate %d -pattern_type glob -i '%s/*.jpg' -c:v libx264 -strict -2 -pix_fmt yuv420p -f mp4 %s" % (fps, outdir, vidfile)
print(cmd)
r = os.popen(cmd)

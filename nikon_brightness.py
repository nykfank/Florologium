#!/usr/bin/python3
import cv2, os
foto_dir = '/mnt/big/katzidien_backup/var/www/florologium/nikon'
outfilename = '/home/nyk/Florologium/brightness.txt'
filed = {}
if os.path.isfile(outfilename):
	for i in open(outfilename).readlines():
		f, et = i.strip().split('\t')
		filed[f] = et
	print('Loaded: %d' % len(filed))
count = 0
for f in os.listdir(foto_dir):
	if f in filed: continue
	if not f.endswith('jpg'): continue
	img = cv2.imread('%s/%s' % (foto_dir, f))
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	m = cv2.mean(gray)[0]
	outrow = '%s\t%f' % (f, m)
	print(outrow)
	open(outfilename, 'a').write(outrow + '\n')
	count += 1
print('New: %d' % count)

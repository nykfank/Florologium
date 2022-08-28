#!/usr/bin/python3
# scale_images.py nikon 348 232
import sys, numpy, shutil, cv2, os, skimage.metrics, scipy.stats
odir = 'anomaly'
if not os.path.isdir(odir): os.mkdir(odir)
indir = sys.argv[1]
#thr = 0.15

def seq_ssimscores(infiles):
	scorelist = []
	num_comparison = len(infiles) - 1
	for i in range(num_comparison):
		fpath1 = '%s/%s' % (indir, infiles[i])
		fpath2 = '%s/%s' % (indir, infiles[i+1])
		img1 = cv2.imread(fpath1)
		img2 = cv2.imread(fpath2)
		score = skimage.metrics.structural_similarity(img1, img2, channel_axis=2)
		scorelist.append(score)
	print(numpy.median(scorelist))
	print(scipy.stats.iqr(scorelist))
	print(scorelist)
	return [ i + 1 for i, x in enumerate(scorelist) if x < numpy.median(scorelist) - scipy.stats.iqr(scorelist) * 1.2 ]

infiles = sorted(filter(lambda x : x.endswith('.jpg'), os.listdir(indir)))
idx = seq_ssimscores(infiles)
print(idx)
interesting_files = [infiles[i] for i in idx]
for fn in interesting_files: shutil.copy('%s/%s' % (indir, fn), '%s/%s' % (odir, fn))
print('Copied %d of %d images' % (len(interesting_files), len(infiles)))

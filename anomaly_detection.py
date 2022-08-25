#!/usr/bin/python3
import sys, numpy, shutil, cv2, os, skimage.metrics
odir = 'anomaly'
if not os.path.isdir(odir): os.mkdir(odir)
indir = sys.argv[1]
thr = 0.1

def seq_ssimscores(infiles):
	scorelist = []
	num_comparison = len(infiles) - 1
	for i in range(num_comparison):
		fpath1 = '%s/%s' % (indir, infiles[i])
		fpath2 = '%s/%s' % (indir, infiles[i+1])
		img1 = cv2.imread(fpath1)
		img2 = cv2.imread(fpath2)
		score = skimage.metrics.structural_similarity(img1, img2, multichannel=True)
		scorelist.append(score)
	return [ i + 1 for i, x in enumerate(scorelist) if x < numpy.median(scorelist) - thr ]

def detect_outliers(vidfiles):
	badfiles = []
	while True:
		outliers = seq_ssimscores(vidfiles)
		if len(outliers) == 0: return badfiles
		badfiles.append(vidfiles[outliers[0]])
		del vidfiles[outliers[0]]

infiles = sorted(filter(lambda x : x.endswith('.jpg'), os.listdir(indir)))
badfiles = detect_outliers(infiles)
for fn in badfiles: shutil.copy('%s/%s' % (indir, fn), '%s/%s' % (odir, fn))
print('Copied %d of %d images' % (len(badfiles), len(infiles)))

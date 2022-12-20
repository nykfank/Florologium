import os, shutil
indir = '/home/nyk/samples'
hidir = '/home/nyk/backup_nikon'
outdir = '/home/nyk/samples_hires'
for f in os.listdir(indir):
	fn1 = '%s/%s' % (hidir, f)
	fn2 = '%s/%s' % (outdir, f)
	shutil.copy(fn1, fn2)
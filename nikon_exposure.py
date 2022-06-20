#!/usr/bin/python3
import subprocess, os
foto_dir = '/home/nyk/nikon'
outfilename = '/home/nyk/exposure_times.txt'
filed = {}
for i in open(outfilename).readlines():
	f, et = i.strip().split('\t')
	filed[f] = et
print('Loaded: %d' % len(filed))
count = 0
for f in os.listdir(foto_dir):
	if f in filed: continue
	cmd = 'exiftool', '%s/%s' % (foto_dir, f)
	r = subprocess.check_output(cmd)
	r = r.decode('ascii')
	rsp = r.split('\n')
	r2 = filter(lambda x : x.startswith('Exposure Time'), rsp)
	exp_time = list(r2)[0].split(':')[1].strip()
	et = eval(exp_time)
	outrow = '%s\t%f' % (f, et)
	print(outrow)
	open(outfilename, 'a').write(outrow + '\n')
	count += 1
print('New: %d' % count)

#!/usr/bin/python3
import os,sys,subprocess
data_dir = os.path.abspath(sys.argv[1]).rstrip('/') # input directory
scaletup = tuple(map(int,sys.argv[2:4]))
assert len(scaletup)==2
convert_path = '/usr/bin/convert'
is_timelapse = lambda x : x.endswith('.jpg')
output_dir='%s_%dx%d' % (data_dir, scaletup[0], scaletup[1])
if not os.path.isdir(output_dir): os.mkdir(output_dir)
files = os.listdir(data_dir)
photos = filter(is_timelapse,files)
for p in photos:
    p1 = '%s/%s' % (data_dir, p)
    p2 = '%s/%s' % (output_dir, p)
    if os.path.isfile(p2): continue
    cmd = convert_path, '-geometry', '%dx%d' % scaletup,p1,p2
    print(' '.join(cmd))
    r = subprocess.call(cmd)
    zeit2 = '%s-%s-%s %s:%s' % (p[0:4], p[4:6], p[6:8], p[9:11], p[11:13])
    cmd = 'Florologium/date_to_image.py', p2, zeit2
    print(' '.join(cmd))
    r = subprocess.call(cmd)


#!/usr/bin/python3
import sys, subprocess, re, os, time
filename = sys.argv[1]
html_path = '/var/www/florologium/content_foto.html'
if not os.path.isfile(filename): 
	print('File does not exist: %s' % filename)
	sys.exit()
cmd = 'exiftool', filename
r = subprocess.check_output(cmd)
r = r.decode('ascii')
rsp = r.split('\n')
r2 = filter(lambda x : x.startswith('Exposure Time'), rsp)
exp_time = list(r2)[0]
exp_time = re.sub(' +', ' ', exp_time)
exp_time = exp_time.replace(' :', ':')
zeit = os.path.splitext(os.path.basename(filename))[0]
zeit2 = '%s-%s-%s %s:%s:%s' % (zeit[0:4], zeit[4:6], zeit[6:8], zeit[9:11], zeit[11:13], zeit[13:15])
html_text = """<p><img alt="Current picture of Florologium" src="https://www.florologium.ch/nikon_current.jpg?%d" style="width: 696px; height: 464px;" />
<br/>%s, %s s</p>""" % (time.time(), zeit2, exp_time)
open(html_path, 'w').write(html_text)

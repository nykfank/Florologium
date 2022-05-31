#!/usr/bin/python3
import sys, subprocess, re, os, time
filename = sys.argv[1]
current_path = '/var/www/florologium/nikon_current.jpg'
html_path = '/var/www/florologium/content_foto.html'
cmd = 'exiftool', current_path
r = subprocess.check_output(cmd)
rsp = r.decode('ascii').split('\n')
r2 = filter(lambda x : x.startswith('Exposure Time'), rsp)
exp_time = list(r2)[0]
exp_time = re.sub(' +', ' ', exp_time)
exp_time = exp_time.replace(' :', ':')
zeit = os.path.splitext(os.path.basename(filename))[0]
zeit2 = '%s-%s-%s %s:%s' % (zeit[0:4], zeit[4:6], zeit[6:8], zeit[9:11], zeit[11:13])
html_text = """<p>
<img alt="Current picture of Florologium" src="https://www.florologium.ch/nikon_current.jpg?%d" style="width: 696px; height: 464px;" />
<br/>%s, %s s</p>
<p>
<img alt="Transformed picture of Florologium" src="https://www.florologium.ch/nikon_current795t.jpg?%d" style="width: 696px; height: 464px;" />
<br/>Image resulting from perspective transformation.</p>
""" % (time.time(), zeit2, exp_time)
open(html_path, 'w').write(html_text)

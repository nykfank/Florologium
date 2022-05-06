#!/usr/bin/python3
import sys, subprocess, re, os, time
filename = sys.argv[1]
if not os.path.isfile(filename): 
	print('File does not exist: %s' % filename)
	sys.exit()
xml_file = '/var/www/florologium/data/pages/index.xml'
xml_data = open(xml_file).read()
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
html_text = """<!--MARKER_START-->
<p><img alt="Current Foto" src="https://www.florologium.ch/nikon_current.jpg?%d" style="width: 696px; height: 464px;" />
<br/>%s, %s s</p>
<!--MARKER_END-->""" % (time.time(), zeit2, exp_time)
html_text = html_text.replace('<', '&lt;')
html_text = html_text.replace('>', '&gt;')
html_text = html_text.replace('"', '&quot;')
xml1 = xml_data.split('&lt;!--MARKER_START--&gt;')[0]
xml2 = xml_data.split('&lt;!--MARKER_END--&gt;')[1]
xml_new = xml1 + html_text + xml2
open(xml_file, 'w').write(xml_new)

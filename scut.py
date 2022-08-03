#!/usr/bin/python3

import urllib.request, cgi, datetime, sys
form = cgi.FieldStorage()
today = datetime.date.today()
year = int(form.getvalue('year', today.year)) 
mon = int(form.getvalue('mon', today.month))
day = int(form.getvalue('day', today.day - 1))
hour, minute = int(form.getvalue('hour', 12)), int(form.getvalue('minute', 0))
sel_species = form.getvalue('species', 'Gazania')
tp = sel_species, mon, day, hour, minute
url = 'http://192.168.1.40/specific_cutout.py?species=%s&mon=%d&day=%d&hour=%d&minute=%d' % tp
contents = urllib.request.urlopen(url).read()

sys.stdout.buffer.write(b"Content-Type: image/png\n\n")
sys.stdout.buffer.write(contents)

#!/usr/bin/python3
import time, sys
nb_days = sys.argv[1]
if nb_days == '1': nb_days = ''
html_path = '/var/www/florologium/content_video%s.html' % nb_days
html_text = """<p>
	<video autoplay="" controls="" height="464" loop="" width="696"><source src="https://www.florologium.ch/video/nikon_timelapse%s.mp4?%d" type="video/mp4" /></video>
	<br/>Update: %s
</p>""" % (nb_days, time.time(), time.strftime("%Y-%m-%d %H:%M"))
open(html_path, 'w').write(html_text)

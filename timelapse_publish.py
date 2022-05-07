#!/usr/bin/python3
import time
html_path = '/var/www/florologium/content_video.html'
html_text = """<p>
	<video autoplay="" controls="" height="464" loop="" width="696"><source src="https://www.florologium.ch/video/nikon_timelapse.mp4?%d" type="video/mp4" /></video>
	<br/>Update: %s
</p>""" % (time.time(), time.ctime())
open(html_path, 'w').write(html_text)

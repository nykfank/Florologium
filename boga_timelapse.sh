#!
ssh flor /home/nyk/bin/scale_images.py /home/nyk/nikon 696 464
ssh flor /home/nyk/bin/make_timelapse.py
rsync flor:/home/nyk/video/nikon_timelapse.mp4 /var/www/florologium/video/nikon_timelapse.mp4


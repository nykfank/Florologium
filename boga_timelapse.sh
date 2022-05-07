#!
ssh flor /home/nyk/bin/scale_images.py /home/nyk/nikon 696 464
ssh flor /home/nyk/bin/make_timelapse.py 1
ssh flor /home/nyk/bin/make_timelapse.py 7
rsync flor:/home/nyk/video/nikon_timelapse.mp4 /var/www/florologium/video/nikon_timelapse.mp4
rsync flor:/home/nyk/video/nikon_timelapse7.mp4 /var/www/florologium/video/nikon_timelapse7.mp4
/home/pi/boga/timelapse_publish.py 1
/home/pi/boga/timelapse_publish.py 7

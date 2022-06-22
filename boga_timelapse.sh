#!
ssh flor Florologium/nikon_exposure.py
ssh flor Florologium/scale_images.py nikon 696 464
ssh flor Florologium/make_timelapse.py 1
ssh flor Florologium/make_timelapse.py 7
ssh flor Florologium/make_timelapse.py 30
rsync flor:video/nikon_timelapse.mp4 /var/www/florologium/video/nikon_timelapse.mp4
rsync flor:video/nikon_timelapse7.mp4 /var/www/florologium/video/nikon_timelapse7.mp4
rsync flor:video/nikon_timelapse30.mp4 /var/www/florologium/video/nikon_timelapse30.mp4
/home/pi/boga/timelapse_publish.py 1
/home/pi/boga/timelapse_publish.py 7
/home/pi/boga/timelapse_publish.py 30

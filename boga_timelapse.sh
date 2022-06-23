#!
ssh flor Florologium/nikon_exposure.py
ssh flor Florologium/scale_images.py nikon 696 464
ssh flor Florologium/make_timelapse.py 1
ssh flor Rscript Florologium/exposure_timelapse.R 7 1
ssh flor Rscript Florologium/exposure_timelapse.R 30 1
ssh flor Rscript Florologium/exposure_timelapse.R 7 0
ssh flor Rscript Florologium/exposure_timelapse.R 30 0
rsync flor:video/nikon_timelapse.mp4 /var/www/florologium/video/nikon_timelapse.mp4
rsync flor:video/nikon_timelapse7.mp4 /var/www/florologium/video/nikon_timelapse7.mp4
rsync flor:video/nikon_timelapse30.mp4 /var/www/florologium/video/nikon_timelapse30.mp4
rsync flor:video/nikon_timelapse7_night.mp4 /var/www/florologium/video/nikon_timelapse7_night.mp4
rsync flor:video/nikon_timelapse30_night.mp4 /var/www/florologium/video/nikon_timelapse30_night.mp4
/home/pi/boga/timelapse_publish.py 1
/home/pi/boga/timelapse_publish.py 7
/home/pi/boga/timelapse_publish.py 30
/home/pi/boga/timelapse_publish.py 7_night
/home/pi/boga/timelapse_publish.py 30_night

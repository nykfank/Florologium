#!
filename="$(date +"%Y%m%d_%H%M%S").jpg"
ssh flortun rm capt0000.jpg
ssh flortun gphoto2 --capture-image-and-download --force-overwrite
rsync flortun:capt0000.jpg /var/www/florologium/nikon/$filename
/usr/bin/convert -geometry 696x464 /var/www/florologium/nikon/$filename /var/www/florologium/nikon_current.jpg
/home/pi/boga/nikon_publish.py /var/www/florologium/nikon/$filename


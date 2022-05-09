#!
filename="$(date +"%Y%m%d_%H%M%S").jpg"
ssh flortun rm capt0000.jpg
ssh flortun gphoto2 --capture-image-and-download --force-overwrite
rsync flortun:capt0000.jpg /var/www/florologium/nikon/$filename
ssh flor convert -geometry 696x464 /home/nyk/nikon/$filename /home/nyk/nikon_current.jpg
rsync flor:/home/nyk/nikon_current.jpg /var/www/florologium/nikon_current.jpg
/home/pi/boga/nikon_publish.py $filename

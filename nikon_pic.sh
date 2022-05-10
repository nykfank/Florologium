#!/bin/bash
filename="$(date +"%Y%m%d_%H%M%S").jpg"
ssh flortun rm capt0000.jpg
ssh flortun gphoto2 --capture-image-and-download --force-overwrite
rsync flortun:capt0000.jpg /var/www/florologium/nikon/$filename
if [[ ! -f /var/www/florologium/nikon/$filename ]] ; then
    echo 'No file downloaded from flortun.'
    exit
fi
ssh flor rm /home/nyk/nikon_current.jpg
ssh flor convert -geometry 696x464 /home/nyk/nikon/$filename /home/nyk/nikon_current.jpg
rsync flor:/home/nyk/nikon_current.jpg /var/www/florologium/nikon_current.jpg
if [[ ! -f /var/www/florologium/nikon/$filename ]] ; then
    echo 'Failed to convert image.'
    exit
fi
/home/pi/boga/nikon_publish.py $filename

#!/bin/bash
filename="$(date +"%Y%m%d_%H%M%S").jpg"
ssh flortun "test -e capt0000.jpg"
if [ $? -eq 0 ]; then
	ssh flortun rm capt0000.jpg
fi
ssh flortun gphoto2 --capture-image-and-download --force-overwrite
ssh flortun "test -e capt0000.jpg"
if [ ! $? -eq 0 ]; then
	echo 'No foto taken.'
	exit
fi
filesize=$(ssh flortun stat -c%s "capt0000.jpg")
if [[ $filesize -lt 10000000 ]]; then
	echo 'Filesize below 10MB, use bulb mode!'
    ssh flortun rm capt0000.jpg
    sleep 5
    ssh flortun gphoto2 --set-config iso=8000 --capture-image-and-download --force-overwrite --bulb 30
fi
rsync flortun:capt0000.jpg /var/www/florologium/nikon/$filename
if [[ ! -f /var/www/florologium/nikon/$filename ]] ; then
	echo 'No file downloaded from flortun.'
	exit
fi
ssh flor "test -e /home/nyk/nikon_current.jpg"
if [ $? -eq 0 ]; then
	ssh flor rm /home/nyk/nikon_current.jpg
fi
ssh flor convert -geometry 696x464 /home/nyk/nikon/$filename /home/nyk/nikon_current.jpg
ssh flor "test -e /home/nyk/nikon_current.jpg"
if [ ! $? -eq 0 ]; then
	echo 'Failed to convert image.'
	exit
fi
rsync flor:/home/nyk/nikon_current.jpg /var/www/florologium/nikon_current.jpg
/home/pi/boga/nikon_publish.py $filename

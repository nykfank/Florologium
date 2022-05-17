#!/bin/bash
filename="$(date +"%Y%m%d_%H%M%S").jpg"
ssh flortun "test -e capt0000.jpg"
if [[ $? -eq 0 ]]; 
then
	ssh flortun rm capt0000.jpg
fi
bulbmode=$(~/boga/bulb_mode.py)
if [[ $bulbmode -eq 0 ]]; 
then
    ssh flortun gphoto2 --capture-image-and-download --force-overwrite
else
    ssh flortun gphoto2 --set-config iso=8000 --capture-image-and-download --force-overwrite --bulb 30
fi
ssh flortun "test -e capt0000.jpg"
if [[ ! $? -eq 0 ]]; 
then
	echo 'No foto.'
	exit
fi
rsync flortun:capt0000.jpg /var/www/florologium/nikon/$filename
if [[ ! -f /var/www/florologium/nikon/$filename ]]; 
then
	echo 'No file downloaded from flortun.'
	exit
fi
ssh flor "test -e nikon_current.jpg"
if [[ $? -eq 0 ]]; 
then
	ssh flor rm nikon_current.jpg
fi
ssh flor convert -geometry 696x464 nikon/$filename nikon_current.jpg
ssh flor "test -e nikon_current.jpg"
if [[ ! $? -eq 0 ]]; 
then
	echo 'Failed to convert image.'
	exit
fi
rsync flor:nikon_current.jpg /var/www/florologium/nikon_current.jpg
~/boga/nikon_publish.py $filename

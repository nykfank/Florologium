#!/bin/bash

current_hour=$(date +%H) # get current hour in 24-hour format

if (( current_hour >= 8 && current_hour < 17 )); then
    exit 0 # Only take pictures when the greenhouse is closed to the public to avoid taking pictures of people.
fi

filename="$(date +"%Y%m%d_%H%M%S").jpg"
ssh flortun "test -e capt0000.jpg"
if [[ $? -eq 0 ]]; 
then
	ssh flortun rm capt0000.jpg
fi
bulbmode=$(~/boga/bulb_mode.py)
if [[ $bulbmode -gt 0 ]]; 
then
    ssh flortun gphoto2 --set-config iso=8000 --capture-image-and-download --force-overwrite --bulb $bulbmode
else
    ssh flortun gphoto2 --capture-image-and-download --force-overwrite
fi
ssh flortun "test -e capt0000.jpg"
if [[ ! $? -eq 0 ]]; 
then
	echo 'No foto.'
	exit
fi
rsync flortun:capt0000.jpg /var/www/box/$filename
if [[ ! -f /var/www/box/$filename ]]; 
then
	echo 'No file downloaded from flortun.'
	exit
fi

convert -geometry 1044x696 /var/www/box/$filename /var/www/current_box.jpg

#ssh flor "test -e nikon_current.jpg"
#if [[ $? -eq 0 ]]; 
#then
#	ssh flor rm nikon_current.jpg
#fi
#ssh flor convert -geometry 696x464 nikon/$filename nikon_current.jpg
#ssh flor "test -e nikon_current.jpg"
#if [[ ! $? -eq 0 ]]; 
#then
#	echo 'Failed to convert image.'
#	exit
#fi

#rsync flor:nikon_current.jpg /var/www/florologium/nikon_current.jpg
#rsync flor:nikon_current795t.jpg /var/www/florologium/nikon_current795t.jpg
#ssh flor convert -geometry 795x530 nikon/$filename nikon_current795.jpg
#ssh flor Florologium/perspective_transformation.py nikon_current795.jpg nikon_current795t.jpg
#~/boga/nikon_publish.py $filename
#ssh flor Florologium/species_cutout.py nikon/$filename
#rsync -r flor:cutout /var/www/florologium/

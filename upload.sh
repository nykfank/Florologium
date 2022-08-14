#!
rsync -p ~/Florologium/nikon_pic.sh katz:boga
rsync -p ~/Florologium/bulb_mode.py katz:boga
rsync -p ~/Florologium/nikon_publish.py katz:boga
rsync -p ~/Florologium/boga_timelapse.sh katz:boga
rsync -p ~/Florologium/exposure_timelapse.R flor:Florologium
rsync -p ~/Florologium/exposure_timelapse_hires.R flor:Florologium
rsync -p ~/Florologium/make_timelapse.py flor:Florologium
rsync -p ~/Florologium/missing.R flor:Florologium
rsync -p ~/Florologium/run_missing.sh katz:boga
rsync -p ~/Florologium/cutout_archive.sh katz:boga
rsync -p ~/Florologium/scale_images.py flor:Florologium
rsync -p ~/Florologium/date_to_image.py flor:Florologium
rsync -p ~/Florologium/crontab_katz.txt katz:.
rsync -p ~/Florologium/perspective_transformation.py flor:Florologium
rsync -p ~/Florologium/species_cutout.py flor:Florologium
rsync -p ~/Florologium/scut.py katz:/var/www/cgi-bin/
rsync -p ~/Florologium/specific_cutout.py flor:/var/www/
rsync -p ~/Florologium/plant_positions.txt flor:Florologium
rsync -p ~/Florologium/plant_positions.txt katz:Florologium
rsync -p ~/Florologium/nikon_exposure.py flor:Florologium

#rsync -vp ~/Florologium/wan_update.sh katz:boga

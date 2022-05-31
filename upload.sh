#!
rsync -p ~/Florologium/nikon_pic.sh katz:boga
rsync -p ~/Florologium/bulb_mode.py katz:boga
rsync -p ~/Florologium/nikon_publish.py katz:boga
rsync -p ~/Florologium/boga_timelapse.sh katz:boga
rsync -p ~/Florologium/exposure_timelapse.R flor:bin
rsync -p ~/Florologium/make_timelapse.py flor:bin
rsync -p ~/Florologium/missing.R flor:bin
rsync -p ~/Florologium/run_missing.sh katz:boga
rsync -p ~/Florologium/crontab_katz.txt katz:.
rsync -p ~/Florologium/perspective_transformation.py flor:bin

#rsync -vp ~/Florologium/wan_update.sh katz:boga

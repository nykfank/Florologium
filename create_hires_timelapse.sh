Rscript Florologium/timepoint_timelapse_hires.R 2 1
Rscript Florologium/timepoint_timelapse_hires.R 7 1
Rscript Florologium/timepoint_timelapse_hires.R 7 0
Florologium/floro_rotazoom.py florologium_hires_7

Rscript Florologium/day_timelapse_hires.R 2022-05-10
Rscript Florologium/day_timelapse_hires.R 2022-06-10
Rscript Florologium/day_timelapse_hires.R 2022-07-10
Rscript Florologium/day_timelapse_hires.R 2022-08-10
Rscript Florologium/day_timelapse_hires.R 2022-09-05

ffmpeg -f concat -safe 0 -i Florologium/vidlist.txt -c copy timelapse2k.mp4
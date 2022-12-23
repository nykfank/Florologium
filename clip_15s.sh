Rscript Florologium/day_timelapse_hires.R 2022-06-24
Rscript Florologium/timepoint_timelapse_hires.R 7
Florologium/median_images.py florologium_hires_7 3
Florologium/median_images.py florologium_hires_2022-06-24 3
Florologium/median_images.py florologium_hires_moving 3
ffmpeg -y -hide_banner -loglevel panic -framerate 25 -pattern_type glob -i 'florologium_hires_7_median3/*.jpg' -s 2048x1080 -c:v libx264 -strict -2 -pix_fmt yuv420p -f mp4 florologium_hires_7_m3.mp4
ffmpeg -y -hide_banner -loglevel panic -framerate 25 -pattern_type glob -i 'florologium_hires_2022-06-24_median3/*.jpg' -s 2048x1080 -c:v libx264 -strict -2 -pix_fmt yuv420p -f mp4 florologium_hires_2022-06-24_m3.mp4


ffmpeg -y -hide_banner -loglevel panic -framerate 25 -pattern_type glob -i 'florologium_hires_moving_median3/*.jpg' -s 2048x1080 -c:v libx264 -strict -2 -pix_fmt yuv420p -f mp4 florologium_hires_moving_m3.mp4

# Video Stabilisation (not looking nice here)
fmpeg -i florologium_hires_moving.mp4 -vf vidstabdetect -f null -
ffmpeg -i florologium_hires_moving.mp4 -vf vidstabtransform florologium_hires_moving_stab.mp4


Rscript Florologium/day_timelapse_hires.R 2022-07-20
Rscript Florologium/day_timelapse_hires.R 2022-07-21
Rscript Florologium/day_timelapse_hires.R 2022-07-22
Rscript Florologium/day_timelapse_hires.R 2022-07-23
Rscript Florologium/day_timelapse_hires.R 2022-07-24
Rscript Florologium/day_timelapse_hires.R 2022-07-25
Rscript Florologium/day_timelapse_hires.R 2022-07-26
Rscript Florologium/day_timelapse_hires.R 2022-07-27
Rscript Florologium/day_timelapse_hires.R 2022-07-28
Rscript Florologium/day_timelapse_hires.R 2022-07-29
Rscript Florologium/day_timelapse_hires.R 2022-07-30
Rscript Florologium/day_timelapse_hires.R 2022-08-01

Rscript Florologium/day_timelapse_hires.R 2022-08-10
Rscript Florologium/day_timelapse_hires.R 2022-08-11
Rscript Florologium/day_timelapse_hires.R 2022-08-12
Rscript Florologium/day_timelapse_hires.R 2022-08-13
Rscript Florologium/day_timelapse_hires.R 2022-08-14
Rscript Florologium/day_timelapse_hires.R 2022-08-15
Rscript Florologium/day_timelapse_hires.R 2022-08-16
Rscript Florologium/day_timelapse_hires.R 2022-08-17
Rscript Florologium/day_timelapse_hires.R 2022-08-18
Rscript Florologium/day_timelapse_hires.R 2022-08-19


Florologium/median_images.py florologium_hires_2022-07-29 3
Florologium/median_images.py florologium_hires_2022-08-19 3
ffmpeg -y -hide_banner -loglevel panic -framerate 25 -pattern_type glob -i 'florologium_hires_2022-07-29_median3/*.jpg' -s 2048x1080 -c:v libx264 -strict -2 -pix_fmt yuv420p -f mp4 florologium_hires_2022-07-29_m3.mp4
ffmpeg -y -hide_banner -loglevel panic -framerate 25 -pattern_type glob -i 'florologium_hires_2022-08-19_median3/*.jpg' -s 2048x1080 -c:v libx264 -strict -2 -pix_fmt yuv420p -f mp4 florologium_hires_2022-08-19_m3.mp4

Rscript Florologium/day_timelapse_hires.R 2022-07-10
Rscript Florologium/day_timelapse_hires.R 2022-07-11
Rscript Florologium/day_timelapse_hires.R 2022-07-12
Rscript Florologium/day_timelapse_hires.R 2022-07-13
Rscript Florologium/day_timelapse_hires.R 2022-07-14
Rscript Florologium/day_timelapse_hires.R 2022-07-15
Rscript Florologium/day_timelapse_hires.R 2022-07-16
Rscript Florologium/day_timelapse_hires.R 2022-07-17
Rscript Florologium/day_timelapse_hires.R 2022-07-18
Rscript Florologium/day_timelapse_hires.R 2022-07-19

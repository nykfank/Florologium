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

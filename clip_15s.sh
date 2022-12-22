#Rscript Florologium/day_timelapse_hires.R 2022-06-19
#Rscript Florologium/day_timelapse_hires.R 2022-06-20
Rscript Florologium/day_timelapse_hires.R 2022-06-21
Rscript Florologium/day_timelapse_hires.R 2022-06-22
Rscript Florologium/day_timelapse_hires.R 2022-06-23
Rscript Florologium/day_timelapse_hires.R 2022-06-24
Rscript Florologium/day_timelapse_hires.R 2022-06-25
Rscript Florologium/day_timelapse_hires.R 2022-06-26
Rscript Florologium/day_timelapse_hires.R 2022-06-27
Rscript Florologium/day_timelapse_hires.R 2022-06-28
Rscript Florologium/day_timelapse_hires.R 2022-06-29
Rscript Florologium/day_timelapse_hires.R 2022-06-30
Rscript Florologium/day_timelapse_hires.R 2022-07-01
Rscript Florologium/day_timelapse_hires.R 2022-07-02
Rscript Florologium/day_timelapse_hires.R 2022-07-03
Rscript Florologium/day_timelapse_hires.R 2022-07-04
Rscript Florologium/day_timelapse_hires.R 2022-07-05
Rscript Florologium/day_timelapse_hires.R 2022-07-06
Rscript Florologium/day_timelapse_hires.R 2022-07-07
Rscript Florologium/day_timelapse_hires.R 2022-07-08

ffmpeg -y -hide_banner -loglevel panic -framerate 25 -pattern_type glob -i 'florologium_hires_7/*.jpg' -s 2048x1080 -c:v libx264 -strict -2 -pix_fmt yuv420p -f mp4 florologium_hires_7.mp4

# todo
ffmpeg -y -hide_banner -loglevel panic -framerate 25 -pattern_type glob -i 'florologium_hires_7_median3/*.jpg' -s 2048x1080 -c:v libx264 -strict -2 -pix_fmt yuv420p -f mp4 florologium_hires_7_m3.mp4
ffmpeg -y -hide_banner -loglevel panic -framerate 25 -pattern_type glob -i 'florologium_hires_2022-06-24_median3/*.jpg' -s 2048x1080 -c:v libx264 -strict -2 -pix_fmt yuv420p -f mp4 florologium_hires_2022-06-24_m3.mp4



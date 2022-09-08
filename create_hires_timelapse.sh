Rscript Florologium/timepoint_timelapse_hires.R 2 1
Florologium/title_generator.py florologium_hires_2 100 "May to September" "Nighttime" ""
ffmpeg -y -hide_banner -loglevel panic -framerate 20 -pattern_type glob -i 'florologium_hires_2/*.jpg' -s 2048x1080 -c:v libx264 -strict -2 -pix_fmt yuv420p -f mp4 timelapse2K/florologium_hires_2.mp4

Rscript Florologium/timepoint_timelapse_hires.R 7 1
Florologium/title_generator.py florologium_hires_7 100 "May to September" "Daytime" ""
ffmpeg -y -hide_banner -loglevel panic -framerate 20 -pattern_type glob -i 'florologium_hires_7/*.jpg' -s 2048x1080 -c:v libx264 -strict -2 -pix_fmt yuv420p -f mp4 timelapse2K/florologium_hires_7.mp4

Rscript Florologium/timepoint_timelapse_hires.R 7 0
Florologium/floro_rotazoom.py florologium_hires_7
Florologium/title_generator.py florologium_hires_7_rota 100 "May to September" "Daytime" "Rotating Zoom"
ffmpeg -y -hide_banner -loglevel panic -framerate 20 -pattern_type glob -i 'florologium_hires_7_rota/*.jpg' -s 2048x1080 -c:v libx264 -strict -2 -pix_fmt yuv420p -f mp4 timelapse2K/florologium_hires_7_rota.mp4

Rscript Florologium/day_timelapse_hires.R 2022-05-10
Florologium/title_generator.py florologium_hires_2022-05-10 25 "Day Timelapse" "May" ""
ffmpeg -y -hide_banner -loglevel panic -framerate 5 -pattern_type glob -i 'florologium_hires_2022-05-10/*.jpg' -s 2048x1080 -c:v libx264 -strict -2 -pix_fmt yuv420p -f mp4 timelapse2K/florologium_hires_2022-05-10.mp4

Rscript Florologium/day_timelapse_hires.R 2022-06-10
Florologium/title_generator.py florologium_hires_2022-06-10 25 "Day Timelapse" "June" ""
ffmpeg -y -hide_banner -loglevel panic -framerate 5 -pattern_type glob -i 'florologium_hires_2022-06-10/*.jpg' -s 2048x1080 -c:v libx264 -strict -2 -pix_fmt yuv420p -f mp4 timelapse2K/florologium_hires_2022-06-10.mp4

Rscript Florologium/day_timelapse_hires.R 2022-07-10
Florologium/title_generator.py florologium_hires_2022-07-10 25 "Day Timelapse" "July" ""
ffmpeg -y -hide_banner -loglevel panic -framerate 5 -pattern_type glob -i 'florologium_hires_2022-07-10/*.jpg' -s 2048x1080 -c:v libx264 -strict -2 -pix_fmt yuv420p -f mp4 timelapse2K/florologium_hires_2022-07-10.mp4

Rscript Florologium/day_timelapse_hires.R 2022-08-10
Florologium/title_generator.py florologium_hires_2022-08-10 25 "Day Timelapse" "August" ""
ffmpeg -y -hide_banner -loglevel panic -framerate 5 -pattern_type glob -i 'florologium_hires_2022-08-10/*.jpg' -s 2048x1080 -c:v libx264 -strict -2 -pix_fmt yuv420p -f mp4 timelapse2K/florologium_hires_2022-08-10.mp4

Rscript Florologium/day_timelapse_hires.R 2022-09-05
Florologium/title_generator.py florologium_hires_2022-09-05 25 "Day Timelapse" "September" ""
ffmpeg -y -hide_banner -loglevel panic -framerate 5 -pattern_type glob -i 'florologium_hires_2022-09-05/*.jpg' -s 2048x1080 -c:v libx264 -strict -2 -pix_fmt yuv420p -f mp4 timelapse2K/florologium_hires_2022-09-05.mp4

ffmpeg -f concat -safe 0 -i Florologium/vidlist.txt -c copy timelapse2k.mp4

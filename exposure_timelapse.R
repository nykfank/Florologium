args <- commandArgs(trailingOnly=TRUE)
nb_days <- as.integer(args[1])
use_daytime <- as.integer(args[2])
movie_seconds <- 30
fps <- 20
nb_imgs <- movie_seconds * fps
indir <- '/home/nyk/nikon_696x464'
outdir <- sprintf('/home/nyk/nikon_696x464_%d_%d', nb_days, use_daytime)
vidfile <- sprintf('/home/nyk/video/nikon_timelapse%d.mp4', nb_days)
if (use_daytime == 0) vidfile <- sprintf('/home/nyk/video/nikon_timelapse%d_night.mp4', nb_days)
if (!dir.exists(outdir)) {
	dir.create(outdir)
} else {
	for (f in list.files(outdir)) unlink(sprintf("%s/%s", outdir, f))
}
et <- read.table("/home/nyk/exposure_times.txt")
colnames(et) <- c("filename", "exp_time")
et$timestamp <- strptime(et$filename, "%Y%m%d_%H%M%S")
et <- et[order(et$timestamp),]
et$date <- as.Date(et$timestamp)
subet <- et[et$timestamp > Sys.time() - nb_days*24*3600,]
subet <- subet[order(subet$exp_time, decreasing=TRUE),]
if (use_daytime == 1) subet <- subet[subet$exp_time < 0.01,] else subet <- subet[subet$exp_time > 1,]
# Take the middle part of the images order by exposure time to avoid the extreme exposures.
if (nrow(subet) < nb_imgs) nb_imgs <- round(nrow(subet) * 0.9)
i1 <- round(nrow(subet)/2 - nb_imgs/2)
i2 <- round(nrow(subet)/2 + nb_imgs/2)
subet <- subet[i1:i2,]
subet <- subet[order(subet$timestamp, decreasing=FALSE),]
for (f in subet$filename) {
	file.copy(sprintf("%s/%s", indir, f), sprintf("%s/%s", outdir, f))
}
cmd <- sprintf("ffmpeg -y -hide_banner -loglevel panic -framerate %d -pattern_type glob -i '%s/*.jpg' -c:v libx264 -strict -2 -pix_fmt yuv420p -f mp4 %s", fps, outdir, vidfile)
writeLines(cmd)
system(cmd)


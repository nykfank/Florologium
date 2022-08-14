args <- commandArgs(trailingOnly=TRUE)
use_daytime <- as.integer(args[2])
movie_seconds <- 30
fps <- 20
nb_imgs <- movie_seconds * fps
indir <- '/home/nyk/backup_nikon'
outdir <- sprintf('/home/nyk/florologium_hires_%d', use_daytime)
vidfile <- '/home/nyk/video/florologium_hires.mp4'
if (use_daytime == 0) vidfile <- '/home/nyk/video/florologium_hires_night.mp4'
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
et <- et[order(et$exp_time, decreasing=TRUE),]
if (use_daytime == 1) et <- et[et$exp_time < 0.01,] else et <- et[et$exp_time > 1,]
# Take the middle part of the images order by exposure time to avoid the extreme exposures.
if (nrow(et) < nb_imgs) nb_imgs <- round(nrow(et) * 0.9)
i1 <- round(nrow(et)/2 - nb_imgs/2)
i2 <- round(nrow(et)/2 + nb_imgs/2)
et <- et[i1:i2,]
et <- et[order(et$timestamp, decreasing=FALSE),]
for (f in et$filename) {
	file.copy(sprintf("%s/%s", indir, f), sprintf("%s/%s", outdir, f))
}

#cmd <- sprintf("ffmpeg -y -hide_banner -loglevel panic -framerate %d -pattern_type glob -i '%s/*.jpg' -c:v libx264 -strict -2 -pix_fmt yuv420p -f mp4 %s", fps, outdir, vidfile)
#writeLines(cmd)
#system(cmd)


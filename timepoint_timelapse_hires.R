args <- commandArgs(trailingOnly=TRUE)
use_daytime <- as.integer(args[2])

start_hour <- 16
movie_seconds <- 30
fps <- 20
nb_imgs <- movie_seconds * fps
indir <- '/home/nyk/backup_nikon'
outdir <- sprintf('/home/nyk/florologium_hires_%d', start_hour)
vidfile <- sprintf('/home/nyk/video/florologium_hires_%d.mp4', start_hour)
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

for (f in subet$filename) {
	file.copy(sprintf("%s/%s", indir, f), sprintf("%s/%s", outdir, f))
}

#cmd <- sprintf("ffmpeg -y -hide_banner -loglevel panic -framerate %d -pattern_type glob -i '%s/*.jpg' -c:v libx264 -strict -2 -pix_fmt yuv420p -f mp4 %s", fps, outdir, vidfile)
#writeLines(cmd)
#system(cmd)


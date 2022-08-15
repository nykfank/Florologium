args <- commandArgs(trailingOnly=TRUE)
sel_hour <- as.integer(args[1]) # 16 was first tested.
movie_seconds <- 30
fps <- 20
photo_interval_seconds <- 5
nb_imgs <- movie_seconds * fps
indir <- '/home/nyk/backup_nikon'
outdir <- sprintf('/home/nyk/florologium_hires_%d', sel_hour)
vidfile <- sprintf('/home/nyk/florologium_hires_%d.mp4', sel_hour)
if (!dir.exists(outdir)) {
	dir.create(outdir)
} else {
	for (f in list.files(outdir)) unlink(sprintf("%s/%s", outdir, f))
}
et <- read.table("/home/nyk/exposure_times.txt")
colnames(et) <- c("filename", "exp_time")
et$timestamp <- strptime(et$filename, "%Y%m%d_%H%M%S")
et$date <- as.Date(et$timestamp)
et$hour <- as.integer(strftime(et$timestamp, "%H"))
et$minute <- as.integer(strftime(et$timestamp, "%M"))
et$hourmin <- et$hour + et$minute/60
et$seldiff <- abs(et$hourmin - sel_hour)
nb_days <- length(unique(et$date))
img_per_day <- nb_imgs / nb_days
diff_limit <- img_per_day * photo_interval_seconds / 60 / 2
subet <- et[et$seldiff <= diff_limit,]
for (f in subet$filename) {
	fn1 <- sprintf("%s/%s", indir, f)
	fn2 <- sprintf("%s/%s", outdir, f)
	if (file.exists(fn1)) file.symlink(fn1, fn2)
}
# Use a resolution of 3840 x 2160 (the 4K norm), not the full 5568x3712 of the camera, otherwise it'll be a huge video file.
# Better use 2048x1080 (2K video), my laptop is too slow to play 4K!
cmd <- sprintf("ffmpeg -y -hide_banner -loglevel panic -framerate %d -pattern_type glob -i '%s/*.jpg' -s 2048x1080 -c:v libx264 -strict -2 -pix_fmt yuv420p -f mp4 %s", fps, outdir, vidfile)
writeLines(cmd)
system(cmd)

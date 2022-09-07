args <- commandArgs(trailingOnly=TRUE)
sel_hour <- as.integer(args[1])
select_only <- as.integer(args[2])
movie_seconds <- 60
fps <- 20
photo_interval_seconds <- 5
nb_imgs <- movie_seconds * fps
indir <- '/home/nyk/backup_nikon'
outdir <- sprintf('florologium_hires_%d', sel_hour)
vidfile <- sprintf('timelapse2K/florologium_hires_%d.mp4', sel_hour)
if (!dir.exists('timelapse2K')) dir.create('timelapse2K') else for (f in list.files(outdir)) unlink(sprintf("%s/%s", outdir, f))
if (!dir.exists(outdir)) dir.create(outdir) else for (f in list.files(outdir)) unlink(sprintf("%s/%s", outdir, f))
# Loading brighness values for photos
br <- read.table("/home/nyk/brightness.txt", stringsAsFactors=FALSE)
colnames(br) <- c("filename", "brightness")
br$timestamp <- strptime(br$filename, "%Y%m%d_%H%M%S")
br$date <- as.Date(br$timestamp)
br$hour <- as.integer(strftime(br$timestamp, "%H"))
br$minute <- as.integer(strftime(br$timestamp, "%M"))
nb_days <- length(unique(br$date))
img_per_day <- nb_imgs / nb_days
subbr <- br[br$hour == sel_hour | br$hour == (sel_hour - 1),]
subbr$brdiff <- abs(subbr$brightness - median(subbr$brightness))
subbr <- subbr[order(subbr$date, subbr$brdiff),]
datetab <- as.data.frame(table(subbr$date))
subbr$idx <- unlist(lapply(datetab$Freq, function(x) seq(x)))
subbr <- subbr[subbr$idx <= 1+ceiling(img_per_day),] # Select images nearest the median each day
subbr2 <- subbr[subbr$brdiff <= quantile(subbr$brdiff, 0.95),] # Outlier removal
writeLines(sprintf("Selected hour: %d, Target images: %d, Selected images: %d, Outliers: %d", 
	sel_hour, nb_imgs, nrow(subbr2), nrow(subbr)-nrow(subbr2)))
# Copy
pb = txtProgressBar(min=0, max=nrow(subbr2), initial=0, style=3) 
for (i in 1:nrow(subbr2)) {
	f <- subbr2[i, "filename"]
	fn1 <- sprintf("%s/%s", indir, f)
	fn2 <- sprintf("%s/%s", outdir, f)
	if (!file.exists(fn1)) next
	setTxtProgressBar(pb, i)
	file.copy(fn1, fn2)
	zeit <- strftime(subbr2[i, "timestamp"], "%Y-%m-%d %H:%M")
	if (select_only == 1) {
		cmd <- sprintf('/home/nyk/Florologium/date_to_image.py %s "%s"', fn2, zeit)
		system(cmd)
	}
}
close(pb)
# Use a resolution of 3840 x 2160 (the 4K norm), not the full 5568x3712 of the camera, otherwise it'll be a huge video file.
# Better use 2048x1080 (2K video), my laptop is too slow to play 4K!
#if (select_only == 1) {
#	cmd <- sprintf("ffmpeg -y -hide_banner -loglevel panic -framerate %d -pattern_type glob -i '%s/*.jpg' -s 2048x1080 -c:v libx264 -strict -2 -pix_fmt yuv420p -f mp4 %s", 
#		fps, outdir, vidfile)
#	writeLines(cmd)
#	system(cmd)
#}
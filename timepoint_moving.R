movie_seconds <- 15
fps <- 25
nb_imgs <- movie_seconds * fps
indir <- '/mnt/big/katzidien_backup/var/www/florologium/nikon'
outdir <- 'florologium_hires_moving'
vidfile <- 'florologium_hires_moving.mp4'
if (!dir.exists(outdir)) dir.create(outdir) else for (f in list.files(outdir)) unlink(sprintf("%s/%s", outdir, f))
# Loading brighness values for photos
br <- read.table("/home/nyk/Florologium/brightness.txt", stringsAsFactors=FALSE)
colnames(br) <- c("filename", "brightness")
br$timestamp <- strptime(br$filename, "%Y%m%d_%H%M%S")
br$date <- as.Date(br$timestamp)
br$hour <- as.integer(strftime(br$timestamp, "%H"))
br$minute <- as.integer(strftime(br$timestamp, "%M"))
br <- br[br$date > as.Date("2022-05-11"),]
br <- br[br$date < as.Date("2022-09-24"),]
br <- br[order(br$timestamp),]
nb_days <- length(unique(br$date))
img_per_day <- nb_imgs / nb_days
hourvec <- rep(0:23, each=nb_days/24)
if (length(hourvec) < nb_days) hourvec <- c(hourvec, rep(23, nb_days - length(hourvec)))
if (length(hourvec) > nb_days) hourvec <- hourvec[1:nb_days]
subbr2 <- list()
for (i in 1:nb_days) {
	bri <- br[br$date == unique(br$date)[i],]
	subbr <- bri[bri$hour == hourvec[i],]
	subbr$brdiff <- abs(subbr$brightness - median(subbr$brightness))	
	subbr <- subbr[order(subbr$date, subbr$brdiff),]
	datetab <- as.data.frame(table(subbr$date))
	subbr$idx <- unlist(lapply(datetab$Freq, function(x) seq(x)))
	subbr <- subbr[subbr$idx <= 1+ceiling(img_per_day),] # Select images nearest the median each day
	subbr <- subbr[subbr$brdiff <= quantile(subbr$brdiff, 0.95),] # Outlier removal
	subbr2 <- rbind(subbr2, subbr)
}

writeLines(sprintf("Target images: %d, Selected images: %d", nb_imgs, nrow(subbr2)))
if (nrow(subbr2) > nb_imgs) subbr2 <- subbr2[1:nb_imgs,]
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
	cmd <- sprintf('/home/nyk/Florologium/date_to_image.py %s "%s"', fn2, zeit)
	#writeLines(cmd)
	system(cmd)
	
}
close(pb)
# Use a resolution of 3840 x 2160 (the 4K norm), not the full 5568x3712 of the camera, otherwise it'll be a huge video file.
# Better use 2048x1080 (2K video), my laptop is too slow to play 4K!
cmd <- sprintf("ffmpeg -y -hide_banner -loglevel panic -framerate %d -pattern_type glob -i '%s/*.jpg' -s 2048x1080 -c:v libx264 -strict -2 -pix_fmt yuv420p -f mp4 %s", 
	fps, outdir, vidfile)
writeLines(cmd)
system(cmd)

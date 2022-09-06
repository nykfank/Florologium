args <- commandArgs(trailingOnly=TRUE)
sel_day <- args[1]
if (interactive()) sel_day <- "2022-08-03"
fps <- 5
indir <- '/home/nyk/backup_nikon'
outdir <- sprintf('/home/nyk/florologium_hires_%s', sel_day)
vidfile <- sprintf('timelapse2K/florologium_hires_%s.mp4', sel_day)
if (!dir.exists('timelapse2K')) dir.create('timelapse2K') else for (f in list.files(outdir)) unlink(sprintf("%s/%s", outdir, f))
if (!dir.exists(outdir)) dir.create(outdir) else for (f in list.files(outdir)) unlink(sprintf("%s/%s", outdir, f))
# Loading brighness values for photos
br <- read.table("/home/nyk/brightness.txt", stringsAsFactors=FALSE)
colnames(br) <- c("filename", "brightness")
br$timestamp <- strptime(br$filename, "%Y%m%d_%H%M%S")
br <- br[order(br$timestamp),]
br$date <- as.Date(br$timestamp)
subr <- br[br$date == as.Date(sel_day),]
# Outlier removal
outl <- EnvStats::rosnerTest(subr$brightness, k=10) # Rosner’s test for outliers 
outl_idx <- outl$all.stats[outl$all.stats$Outlier == TRUE, "Obs.Num"]
print(outl$all.stats)
writeLines(sprintf("Removed %d of %d images.", length(outl_idx), nrow(subr)))
if (length(outl_idx) > 0) {
	writeLines(subr[outl_idx, "filename"])
	subr <- subr[-outl_idx,]
}
# Copy
pb = txtProgressBar(min=0, max=nrow(subr), initial=0, style=3) 
for (i in 1:nrow(subr)) {
	f <- subr[i, "filename"]
	fn1 <- sprintf("%s/%s", indir, f)
	fn2 <- sprintf("%s/%s", outdir, f)
	if (!file.exists(fn1)) next
	setTxtProgressBar(pb, i)
	file.copy(fn1, fn2)
	zeit <- strftime(subr[i, "timestamp"], "%Y-%m-%d %H:%M")
	cmd <- sprintf('/home/nyk/Florologium/date_to_image.py %s "%s"', fn2, zeit)
	system(cmd)
}
close(pb)
# Use a resolution of 3840 x 2160 (the 4K norm), not the full 5568x3712 of the camera, otherwise it'll be a huge video file.
# Better use 2048x1080 (2K video), my laptop is too slow to play 4K!
cmd <- sprintf("ffmpeg -y -hide_banner -loglevel panic -framerate %d -pattern_type glob -i '%s/*.jpg' -s 2048x1080 -c:v libx264 -strict -2 -pix_fmt yuv420p -f mp4 %s", 
	fps, outdir, vidfile)
writeLines(cmd)
system(cmd)

# datab <- as.data.frame(table(br$date))
# datab$date <- gsub("2022-", "", as.character(datab$Var1))
# barplot(datab$Freq, names.arg=datab$date, las=3, cex.names=0.8)
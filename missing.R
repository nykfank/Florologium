fotab <- data.frame(filename=list.files("~/nikon"))
fotab$time <- strptime(fotab$filename, "%Y%m%d_%H%M%S.jpg")
start_time <- min(fotab$time)
start_time_day <- as.POSIXct(strftime(start_time, "%Y-%m-%d 00:00:01"))
end_time_day <- as.POSIXct(strftime(Sys.time(), "%Y-%m-%d 23:55:01"))
optab <- data.frame(time=seq(from=start_time_day, by=5*60, to=end_time_day))
fotab$key <- strftime(fotab$time, "%Y%m%d_%H%M")
optab$key <- strftime(optab$time, "%Y%m%d_%H%M")
misstab <- merge(optab, fotab[,c("key", "filename")], all.x=TRUE, by="key")
misstab <- misstab[order(misstab$time),]
misstab$ok <- 0
misstab[!is.na(misstab$filename), "ok"] <- 1
misstab$date <- strftime(misstab$time, "%Y-%m-%d")
daymat <- matrix(misstab$ok, ncol=24*60/5, byrow=TRUE)
colnames(daymat) <- 1:(24*60/5)
rownames(daymat) <- unique(misstab$date)
#gplots::heatmap.2(daymat, dendrogram='none', Rowv=FALSE, Colv=FALSE, trace='none', key=FALSE, col=c("black", "green"))
melted_daymat <- reshape2::melt(t(daymat))
p <- ggplot2::ggplot(data = melted_daymat, ggplot2::aes(x=Var1, y=Var2, fill=value)) + 
  ggplot2::geom_tile() + ggplot2::theme_minimal() +
  ggplot2::theme(legend.position = "none") +
  ggplot2::xlab(NULL) + ggplot2::ylab(NULL)
png("~/missing_dayplot.png", width=640, height=480)
print(p)
dev.off()
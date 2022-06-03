fotab <- data.frame(filename=list.files("~/nikon"))
interval <- 5
fotab$time <- strptime(fotab$filename, "%Y%m%d_%H%M%S.jpg")
start_time <- as.POSIXct(strftime(min(fotab$time), "%Y-%m-%d 00:00:01"))
end_time <- as.POSIXct(strftime(Sys.time(), "%Y-%m-%d 23:55:01"))
optab <- data.frame(time=seq(from=start_time, by=interval*60, to=end_time))
fotab$key <- strftime(fotab$time, "%Y%m%d_%H%M")
optab$key <- strftime(optab$time, "%Y%m%d_%H%M")
misstab <- merge(optab, fotab[,c("key", "filename")], all.x=TRUE, by="key")
misstab <- misstab[order(misstab$time),]
misstab$ok <- as.numeric(!is.na(misstab$filename))
misstab$date <- strftime(misstab$time, "%Y-%m-%d")
misstab$index <- rep(1:(24*60/interval), length(unique(misstab$date)))
misstab$hour <- 24 * (misstab$index - 1 ) / (24*60/interval)
misstab2 <- misstab[misstab$time > min(fotab$time) & misstab$time < Sys.time() - 60 & misstab$date > Sys.Date() - 14,]
percent_complete <- 100 * sum(misstab2$ok) / nrow(misstab2)
p <- ggplot2::ggplot(data = misstab2, ggplot2::aes(x=hour, y=date, fill=ok)) + 
  ggplot2::geom_tile() + ggplot2::theme_minimal() +
  ggplot2::theme(legend.position = "none") + ggplot2::xlab(NULL) + ggplot2::ylab(NULL) +
  ggplot2::scale_x_continuous(limits = c(0, 24), breaks = 0:23) + 
  ggplot2::ggtitle(sprintf("%2.2f%% complete (last 14 days)", percent_complete))
svg("~/missing_dayplot.svg")
print(p)
dev.off()

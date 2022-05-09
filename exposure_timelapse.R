et <- read.table("/home/nyk/exposure_times.txt")
colnames(et) <- c("filename", "exp_time")
et$timestamp <- strptime(et$filename, "%Y%m%d_%H%M%S")
et <- et[order(et$timestamp),]
et$date <- as.Date(et$timestamp)
et$lexp <- log(et$exp_time)
etday <- et[et$timestamp > Sys.time() - 24*3600,]
etweek <- et[et$timestamp > Sys.time() - 7*24*3600,]

png("/home/nyk/exptime1.png", width=696, height=320)
plot(etday$timestamp, etday$lexp, xlab="Time", ylab="Log of exposure time [s]", main=sprintf("Exposure times at %s", etday$date[nrow(etday)]))
lines(etday$timestamp, etday$lexp)
dev.off()

png("/home/nyk/exptime7.png", width=696, height=320)
plot(etweek$timestamp, etweek$lexp, xlab="Time", ylab="Log of exposure time [s]", main=sprintf("Exposure times %s to %s", etweek$date[1], etweek$date[nrow(etday)]))
lines(etweek$timestamp, etweek$lexp)
dev.off()
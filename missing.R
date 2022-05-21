fotovec <- list.files("../nikon")
timevec <- strptime(fotovec, "%Y%m%d_%H%M%S.jpg")
# min should be on a full 5 divisible minute
optvec <- seq(from=min(timevec), by=5*60, to=Sys.time())

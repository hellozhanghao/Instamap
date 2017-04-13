library(data.table)

combine <- fread("combined_data.csv",header = T, fill = T)
#sort data
combine <- combine[order(id,date_time)]

#find the interval
combine[,interval := c(0, diff(as.POSIXct(date_time))),by = id]
meaninterval <-combine[,list(meaninterval =mean(interval)),by = id]
medianinterval <-combine[,list(medianinterval =median(interval)),by = id]

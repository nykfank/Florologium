#current_time = datetime.datetime(2022, 5, 19, 22, 30, 0).astimezone()
#print("dawn", s["dawn"])
#print("dusk", s["dusk"])

#daymat <- matrix(misstab$ok, ncol=24*60/interval, byrow=TRUE)
#colnames(daymat) <- 1:(24*60/interval)
#rownames(daymat) <- unique(misstab$date)
#gplots::heatmap.2(daymat, dendrogram='none', Rowv=FALSE, Colv=FALSE, trace='none', key=FALSE, col=c("black", "green"))
#melted_daymat <- reshape2::melt(t(daymat))

<<<<<<< HEAD
dawn = s["dawn"] + datetime.relativedelta(minutes=15)
dusk = s["dusk"] - datetime.timedelta(hours=0, minutes=15)
=======
#
x = current_time = datetime.datetime(2022, 5, 19, 22, 30, 0).astimezone()
#print("dawn", s["dawn"])
#print("dusk", s["dusk"])
dusk = s["dusk"] - datetime.timedelta(minutes=15)
dawn = s["dawn"] + datetime.timedelta(minutes=15)
>>>>>>> 237890e1dfa1868a9ae88d3c07ea6f339bb9cc70


#html = '<table><tr><th>Picture</th><th>Species</th><th>Flowering</th></tr>\n'
#for Species_Name, (X_Coordinate, Y_Coordinate, Start_hour, End_hour) in specd.items():
#    html += '<tr><td><img src="%s.jpg" width="%d" height="%d" alt="%s"/></td>' % (Species_Name, xsize, ysize, Species_Name)
#    html += '<td>%s</td><td>%dh - %dh</td></tr>\n' % (Species_Name, Start_hour, End_hour)
#html += '</tr></table>'
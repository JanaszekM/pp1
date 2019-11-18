tab=[21600, 4350 , 3920 ,5590 , 3250 , 4010]
import math
import statistics

srednia=sum(tab)/len(tab)
mediana=statistics.median(tab)
odchyl=statistics.stdev(tab)
print(srednia)
print(mediana)

print(odchyl)


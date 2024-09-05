from datetime import date
import time

startTime = time.perf_counter()

ldates = []

d1=date(2016,8,12)
d2=date(2016,7,12)
d3=date(2018,8,12)
d4=date(2017,8,12)
d5=date(2012,8,12)
d6=date(2011,8,12)

ldates.append(d1)
ldates.append(d2)
ldates.append(d3)
ldates.append(d4)
ldates.append(d5)
ldates.append(d6)

ldates.sort()

time.sleep(1)

for d in ldates:
    print(d)


endTime = time.perf_counter()

print("Execution Time",endTime-startTime)


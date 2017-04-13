from dateutil import parser
import time

dt = parser.parse("Aug 28 1999 12:00AM")
print(dt)
f = open("combined_data.csv","r")


line = f.readline()
line = f.readline()
while line!="":
    info = line[:-1].split(",")
    dt = parser.parse(info[2])
    s= time.mktime(dt.timetuple())


    line = f.readline()

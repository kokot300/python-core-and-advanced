import time
import datetime

startTime=time.perf_counter()
a=time
b=datetime

c=time.time()
d=time.ctime(c)
e=datetime.datetime.today()

print(a)
print(b)
print(c)
print(d)
print(e)
print(e.day,e.month,e.year,e.hour,e.minute,e.second,e.microsecond)
print("current date {}/{}/{}".format(e.day,e.month,e.year))

#print(type(datetime))

f=datetime.date(2019,9,12)
g=datetime.time(17,40)
fg=datetime.datetime.combine(f,g)
print(f)
print(g)
print(fg)

time.sleep(3)

ldates=[]
d1=datetime.date(2019,2,3)
d2=datetime.date(2018,5,3)
d3=datetime.date(2020,2,4)
d4=datetime.date(2019,9,1)
ldates.append(d1)
ldates.append(d2)
ldates.append(d3)
ldates.append(d4)
ldates.sort()

for i in ldates:
    print(i)

stopTime=time.perf_counter()

print("executed in ",stopTime-startTime)
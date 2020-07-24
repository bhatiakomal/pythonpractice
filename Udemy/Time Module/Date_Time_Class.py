'''from datetime import datetime
dt1=datetime(year=2020,month=7,day=30)
dt2=datetime(year=2020,month=7,day=30,hour=14,minute=23,second=20)
#It is not neccessay that u have to write date time month only maintain the order
dt3=datetime(2020,7,30)
dt4=datetime(2020,7,30,14,23,20)
print(dt1)
print(dt2)
print(dt3)
print(dt4)
print(dt1.year)'''

from datetime import datetime
curren_time=datetime.now()
print(curren_time)
print(curren_time.day)
print(curren_time.time())


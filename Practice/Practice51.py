import datetime
datetime_object = datetime.datetime.now()
print(datetime_object)

import datetime
d=datetime.date(2020,5,25)
print(d)

from datetime import date
d=date.today()
print(d)

from datetime import datetime
d=datetime(2020,5,25,11,12,13)
print(d)

from datetime import date
d1=datetime(year=2020,month=8,day=6)
d2=datetime(year=1996,month=8,day=6)
d3=d1-d2
print(d3)

def getdate():
    date1 = input("date and time:")
    print(date1)
getdate()




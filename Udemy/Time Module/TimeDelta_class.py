#It is used to find out difference between two dates
from datetime import timedelta,date
td=timedelta(days=10)
d=date.today()
print(d+td)
print(d-td)
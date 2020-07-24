from datetime import date
dob=date(1996,8,6)
current_date=date.today()
age=current_date.year-dob.year-((current_date.month,date)<(dob.month,date))
print(age)
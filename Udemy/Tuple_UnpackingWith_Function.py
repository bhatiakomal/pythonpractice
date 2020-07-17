"""tuple_lst=[('apple',200),('google',300),('microsoft',500)]
for items in tuple_lst:
    print(items)
for items,price in tuple_lst:
    print(price)"""
work_Hours=[('apple',200),('google',300),('microsoft',500)]
def employee_hours(work_Hours):
    current_max=0
    employee_of_the_month=''
    for employee, hours in  work_Hours:
        if hours>current_max:
            current_max=hours
            employee_of_the_month=employee
        else:
            pass
    return (employee_of_the_month,current_max)
rslt=employee_hours(work_Hours)
print(rslt)



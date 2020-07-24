from datetime import datetime
dt=datetime.today()
print(dt)
print()

new_d1=dt.strftime('%B,%d %Y')
print(new_d1)
print()

new_d2=dt.strftime('%d/%b/%y')
print(new_d2)
print()

new_d3=dt.strftime('%d-%m- %y')
print(new_d3)
print()

new_d4=dt.strftime('%H:%M:%S')
print(new_d4)
print()

new_d5=dt.strftime('%I:%M:%S')
print(new_d5)
days_worked=int(input("Enetr number of days:"))
peny_per_day=0.1
totalNumberPennies=0
for current_day in range(days_worked+1):
    pennies_for_day=2**current_day
    totalNumberPennies+=pennies_for_day
    print(current_day+1,"\t",pennies_for_day)
payTotalmoney=totalNumberPennies*0.1
print(payTotalmoney)
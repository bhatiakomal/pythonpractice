oraginsm=int(input("Enter number of organism:"))
daily_increase=int(input("average daily increase:"))
number_of_days=int(input("Enter number of days:"))
daily_increase=daily_increase/100
population=oraginsm
for current_day in range(1,number_of_days+1):
    print(current_day,"\t",format(population,".2f"))
    population=population+(daily_increase*population)
total_Days=5
total_bugs=0
for current_days in range(1,total_Days+1):
   bugs_collected= int(input("How many bugs collect in day:"+str(current_days)))
   total_bugs+=bugs_collected
print("The total number of bugs collected for all",total_Days,"Days is ",total_bugs)

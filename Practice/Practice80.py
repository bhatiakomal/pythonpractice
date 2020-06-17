totalNumberOfMonths=0
totalInchesOfRainFall=0
userNumberOfYears=int(input("Enter number of years:"))
for currentyears in range(1,userNumberOfYears+1):
    for currentMonths in range(1,13):
        monthlyRainfallInches=float(input("Please enter tpe of inches rainfall in month:"\
                                          +format(currentMonths,"2d")))
        totalInchesOfRainFall+=monthlyRainfallInches
        totalNumberOfMonths+=1
averageRainFall=totalInchesOfRainFall/totalNumberOfMonths
print("Number of months: "+format(totalNumberOfMonths,"d")+\
      "Toatal inches rain fall:"+format(totalInchesOfRainFall,".2f"),\
     "Average Rain Fall:"+format(averageRainFall,".2f"),sep="\n")



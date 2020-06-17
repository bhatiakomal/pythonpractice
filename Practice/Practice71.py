onePenny=0.01
oneNickle=onePenny*5
oneDimse=onePenny*10
oneQuarter=onePenny*25
noOfPannies=int(input("Enter the number of pennies:"))
noOfNickles=int(input("Enter the number of nicles:"))
noOfDimse=int(input("Enter the number of dimise:"))
noOfQuarter=int(input("Enter the number of quarter:"))
peniesValue=noOfPannies*onePenny
nickleValue=noOfNickles*oneNickle
demisevalue=noOfDimse*oneDimse
quarterValue=noOfQuarter*oneQuarter
total_value=peniesValue+nickleValue+demisevalue+quarterValue
if total_value==1.00:
    print("Congrates u win the game bcoz ur money value "+str(total_value)+"is equal to 1 doller")
else:
    if total_value<1.00:
        print("u didn't win the game bcoz ur moeny value of"+str(total_value)+"is less than 1 dollar")
    elif total_value>1.00:
        print("u didn't win the game bcoz ur moeny value of"+str(total_value)+"is more than 1 dollar")




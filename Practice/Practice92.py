def show():
    enterAmount=int(input("Enter your amount:"))
    minimumInsurance=(80/100)*enterAmount
    print("Financial expert advice is you should insure your house for:",format(minimumInsurance,".2f")+\
          "which is 80% of the amount:",enterAmount)
show()
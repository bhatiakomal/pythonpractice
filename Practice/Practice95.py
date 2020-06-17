def show():
    seatsInClassA=int(input("Enter number of seats in class A:"))
    seatsInClassB = int(input("Enter number of seats in class B:"))
    seatsInClassC = int(input("Enter number of seats in class C:"))
    costPerseatInClassA=seatsInClassA*20
    costPerseatInClassB=seatsInClassB*15
    costPerseatInClassC=seatsInClassC*10
    print("cost Per seat In Class A:", str(costPerseatInClassA),"\n" + \
          "cost Per seat In Class B:", str(costPerseatInClassB),"\n" + \
          "cost Per seat In Class C:", str(costPerseatInClassC))
    totalIncome=costPerseatInClassA+costPerseatInClassB+costPerseatInClassC
    print("Total income from one match from class A,B,C is:",totalIncome)

show()

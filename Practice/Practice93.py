def show():
    monthlyLoan=int(input("How much pay you for ur mothly loan"))
    monthlyInsurancePayment = int(input("How much pay you for ur Insurance Payment"))
    monthlyGasPayment = int(input("How much pay you for ur gas payment"))
    monthlyOilPayment = int(input("How much pay you for ur oil payment"))
    monthlyTirePayment = int(input("How much pay you for ur mothly tire payment"))
    monthlyMaintainsCost = int(input("How much pay you for ur mothly maintainse cost"))
    totalMonthlyExpense=monthlyLoan+monthlyInsurancePayment+monthlyGasPayment+monthlyOilPayment+monthlyTirePayment+\
          +monthlyMaintainsCost
    totalAnnuallyExpense=totalMonthlyExpense*12
    print("Your total monthly expense is:",totalMonthlyExpense)
    print("Your total annualy expense is:",totalAnnuallyExpense)

show()
def askAmountOfPurchase():
    useramountOfPurchase=float(input("Enter ur amount of purchase:"))
    return useramountOfPurchase
def calculateStateTax(useramountOfPurchase):
    stateTax=0.05*useramountOfPurchase
    return stateTax
def calculateCountryTax(useramountOfPurchase):
    countryTax=useramountOfPurchase*0.25
    return countryTax
def calculateTotalTax(stateTax,countryTax):
    totalTax=stateTax+countryTax
    return totalTax
def calculateTotalSale(useramountOfPurchase,totalTax):
    totalSale=useramountOfPurchase+totalTax
    return totalSale
def printdetails(useramountOfPurchase,stateTax,countryTax,totalTax,totalSale):
    print("user ammount of purchase="+format(useramountOfPurchase,".2f"),\
          "state tax="+format(stateTax,".2f"),\
          "country tax="+format(countryTax,".2f"),\
          "total tax="+format(totalTax,".2f"),\
          "total sale="+format(totalSale,".2f"),sep="\n")
def main():
    useramountOfPurchase=askAmountOfPurchase()
    stateTax=calculateStateTax(useramountOfPurchase)
    countryTax=calculateCountryTax(useramountOfPurchase)
    totalTax=calculateTotalTax(stateTax,countryTax)
    totalSale=calculateTotalSale(useramountOfPurchase,totalTax)
    printdetails(useramountOfPurchase, stateTax, countryTax, totalTax, totalSale)


numberOfSharePurchased=2000
amountPaidPerShare=40
amountPaidForStock=numberOfSharePurchased*amountPaidPerShare
comissionForBuying=0.03*amountPaidForStock
numberOfShareSold=2000
amountgetForShare=42.75
amountgetForStock=numberOfShareSold*amountgetForShare
comissionForSelling=0.03*amountgetForStock
profit=(amountgetForStock-comissionForSelling)-(amountPaidForStock-comissionForBuying)
print("amountPaidForStock: $"+format(amountgetForStock,".2f"),"\n"
      "Amount paid for buying stcok with commission: $"+format(comissionForBuying,".2f"),"\n"
      "Amount get for sold stock: $"+format(amountgetForStock,".2f"),"\n"
      "The ammount paid when sold the stock as commision: $"+format(comissionForSelling,".2f"),"\n"
      "Profit: $"+format(profit,".2f")) 


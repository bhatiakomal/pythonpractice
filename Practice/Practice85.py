tution_fee=8000
increased_fee=0.03
print("Years \t final amount")
for years in range(1,6):
    final_amount=years*increased_fee*tution_fee+tution_fee
    print(years,"\t  ",final_amount)
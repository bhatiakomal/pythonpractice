x=int(input("Enetr the weight of the  package: "))
if x<=2:
    shippingcharges=1.50
elif x<7:
    shippingcharges=3.00
elif x<11:
    shippingcharges=4.00
elif x>10:
    shippingcharges=4.75
print("For package weighing "+str(x)+",You will pay"+format(shippingcharges,".2f"))
def show():
    x=int(input("Enter number of packages purchased:"))
    package_price=99
    if x<10:
        discount=0.0
    elif x<20:
        discount=0.10
    elif x <50:
        discount = 0.20
    elif x<100:
        discount=0.30
    elif x>100:
        discount=0.40
    subtotal=x*package_price
    discount_amount=discount*subtotal
    total=subtotal-discount_amount
    print("Amount discount:$"+str(discount_amount),"\n"
    "Total amount:$"+str(total))
show()
show()
show()

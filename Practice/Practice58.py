#Find out Sales Tax:
def show():
    amount=int(input("Enter your anount:"))
    state_tax=0.05
    country_tax=0.025
    x=amount*state_tax
    print("State tax:",x)
    y=amount*country_tax
    print("Country tax:",y)
    print("Total amount:"+format(amount+x+y,".2f"))
show()
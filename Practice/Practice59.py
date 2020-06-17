def show():
    x=int(input("Enter your meal amount:"))
    print(x)
    print("Tip amount is:",x*0.18)
    print("Sale Tax is:",x*0.07)
    print("Total taxx is:",x+x*0.18+x*0.07)
show()


def show():
    primarycolour1=input("Please enter first colour:")
    primarycolour2=input("Please enter second colour:")
    if primarycolour1=="red" and primarycolour2=="blue" or \
            primarycolour1=="blue" and primarycolour2=="red":
        print(primarycolour1+" is mixed with "+primarycolour2+" is purple ")
    elif primarycolour1=="red" and primarycolour2=="yellow" or \
            primarycolour1=="yellow" and primarycolour2=="red":
        print(primarycolour1 + " is mixed with " + primarycolour2 + " is orange")
    elif primarycolour1=="blue" and primarycolour2=="yellow" or \
            primarycolour1=="yellow" and primarycolour2=="blue":
        print(primarycolour1 + " is mixed with " + primarycolour2 + " is green")
    else:
        print("Error:Out of the course")
show()



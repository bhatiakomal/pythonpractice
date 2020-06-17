total=0
number=int(input("enter number:"))
while number>-1:
    total=total+number
    number=int(input("Please enter next number or -ve number:"))
print("Total sum:",total)
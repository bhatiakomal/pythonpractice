user_integer=int(input("Enter integer:"))
while user_integer<1:
    user_integer=int(input("Enter +ve number"))
factorial = 1
for current_number in range(1,user_integer+1):
    factorial=factorial*current_number
print("the factorial of",user_integer,"is",factorial)
x=float(input("Enter weight:"))
y=float(input("Enter height:"))
BMI=(x*703)/(y**2)
print("Your BMI is",BMI)
if BMI<18.5:
    print("Your BMI "+format(BMI,".2f")+" You are underweight")
elif BMI<26:
    print("Your BMI "+format(BMI,".2f")+" You are optimal")
else:
    print("Your BMI "+format(BMI,".2f")+" You are overweight")

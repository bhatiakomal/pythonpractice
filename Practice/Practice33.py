import math
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
gcd = (math.gcd(a,b))
lcm = str(a*b/gcd)
print("LCM = "+ lcm)
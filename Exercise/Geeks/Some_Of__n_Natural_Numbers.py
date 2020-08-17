def findSum(n):
    sum = 0
    x = 1
    while x <= n:
        sum = sum + x
        x = x + 1
    return sum
n = int(input("Enter ur number:"))
print(findSum(n))
'''string=input("String: ")
n=int(input("No. of copies :"))
result=""
for i in range(n):
    result=result+string
print(result)

def show():
    name="Welcome"
    print("Komal",name)
show()'''

def show(str,n):
    result=""
    for i in range(n):
        result=result+str
    return result
print(show("a",5))
print(show("b",10))

x = input("enter string : ")
y = int(input("enter num : "))
print(y * x)

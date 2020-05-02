'''a=[]
n=int(input("Enter number of element:"))
for i in range(n):
    a.append(int(input("Enter element:")))

print(type(a))
a=tuple(a)
print(type(a))
print("tuples")
for j in a:
    print(j)

#Repition in Tuple
print("Repition in Tuple")
a=(10,20,30,40,50)
b=a*5
print(b)

#Aliasing in tuple
print("Aliasing in tuple")
a=(10,20,30,40,50)
b=a
print(a)
print(b)
print("A:",id(a))
print("b:",id(b))

a=(10,20,30,40,50)
b=a
a=a[:3]
print(a)
print(id(a))
print(b)
print(id(b))'''

print("copying tuple")
a=(10,20,30,40,50)
b=a[0:5]
print(b)

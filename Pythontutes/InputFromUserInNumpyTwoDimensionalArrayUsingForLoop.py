'''from numpy import *
m=int(input("Enter number of rows :"))
n=int(input("Enter number of column :"))
a=zeros((m,n),dtype=int)
u=len(a)
print(a)
#With index
for r in range(u):
    for c in range(len(a[r])):
        x=int(input("Enter your element"))
        a[r][c]=x

for r in range(u):
    for c in range(len(a[r])):
        print(a[r][c])

print(a)'''

#Without index
from numpy import *
m=int(input("Enter number of rows :"))
n=int(input("Enter number of column :"))
a=zeros((m,n),dtype=int)
u=len(a)
print(a)
for r in range(u):
    for c in range(len(a[r])):
        x=int(input("Enter your element"))
        a[r][c]=x

for r in a:
    for c in r:
        print(c)

print(a)
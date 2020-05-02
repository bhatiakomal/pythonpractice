'''from numpy import *
n=int(input("Enter your number :"))
a=zeros(n,dtype=int)
print(a)#Input from user

from numpy import *
n=int(input("Enter your number :"))
a=zeros(n,dtype=int)
a[0]=20
a[1]=30
a[3]=60
print(a)#we can modified like this .

from numpy import *
n=int(input("Enter your number :"))
a=zeros(n,dtype=int)
for i in range(n):
    x=int(input("enter number :"))
    a[i]=x
print(a)'''

from numpy import *
n=int(input("Enter your number :"))
a=zeros(n,dtype=int)
for i in range(n):
    x=int(input("enter number :"))
    a[i]=x
for i in range(len(a)):
    print(a[i])


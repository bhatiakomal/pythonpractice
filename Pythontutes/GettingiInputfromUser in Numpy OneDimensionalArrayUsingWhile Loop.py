from numpy import *
n=int(input("Enter your Element :"))
a=zeros(n,dtype=int)
u=len(a)
i=0
j=0
while i<u:
    x=int(input("Enter number:"))
    a[i]=x
    i+=1
while j< len(a):
    print(a[j])
    j+=1

'''from numpy import *
a=zeros((3,2),dtype=int)
print(a)

#FOR Loop
from numpy import *
a=zeros((3,2),dtype=int)
n=len(a)
for  r in a:
    for c in r:
        print(c)
    print()

from numpy import *
a=zeros((3,2),dtype=int)
n=len(a)
for  r in range(n):
    for c in range(len(a[r])):
        print(r,c,'=',a[r][c])
    print()'''

#While Loop
from numpy import *
a=zeros((3,2),dtype=int)
n=len(a)
r=0
while r<n:
    c=0
    while c< len(a[r]):
        print(r,c,"=",a[r][c])
        c+=1
    r+=1
    print()
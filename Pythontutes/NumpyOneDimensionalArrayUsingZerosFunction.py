'''from numpy import*
a=zeros(5)
print(a)#by default it is  Float
from numpy import*
a=zeros(5,dtype=int)
for i in a:
    print(i)

from numpy import*
a=zeros(5,dtype=int)
n=len(a)
for i in range(n):
    print(a[i])'''


from numpy import*
a=zeros(5,dtype=int)
n=len(a)
i=0
while i<n:
    print(a[i])
    i+=1

'''from numpy import*
a=linspace(1,8,)
print(a)'''#this divide 1,8 into 50 parts by default

from numpy import*
a=linspace(1,8,5,endpoint=False)
print(a)#here endpoint ie 8 is not included bcoz endpoint is flase.

#FOR Loop
#With index
'''from numpy import*
a=linspace(1,8,5)
print(a)
n=len(a)
print(n)
for i in range(n):
    print(i,'=',a[i])

#Without index
from numpy import *
a = linspace(1, 8, 5)
for  i in a:
    print(i)

#While loop
from numpy import *
a = linspace(1, 8, 5)
n=len(a)
i=0
while i<n:
    print(a[i])
    i+=1'''

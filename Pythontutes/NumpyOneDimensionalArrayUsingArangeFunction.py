'''from numpy import*
a=arange(5)
print(a)

from numpy import*
a=arange(1,10,2)
print(a)

from numpy import*
a=arange(1,10,2)
for i in a:
    print(i)

from numpy import*
a=arange(1,10,2)
n=len(a)
print(n)
for i in range(n):
    print(i,'=',a[i])'''

from numpy import*
a=arange(1,10,2)
n=len(a)
i=0
while i <n:
    print(a[i])
    i+=1
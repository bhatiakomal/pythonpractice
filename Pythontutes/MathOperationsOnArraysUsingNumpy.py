'''from numpy import *
a=array([101,102,103,104,105])
a+=5
print(a)

from numpy import *
a=array([101,102,103,104,105])
a+=5
for i in a:
    print(i)

from numpy import *
a=array([101,102,103,104,105])
b=array([202,205,209,212,222])
c=a+b
n=len(c)
for i in range(n):
    print(c[i])

from numpy import *
a=array([101,102,103,104,105])
b=array([202,205,209,212,222])
c=a+b
n=len(c)
i=0
while i<n:
    print(i,'=',c[i])
    i+=1'''

#Note we can apply all arithematical operations on array like this.

from numpy import *
a=array([101,102,103,104,105])
b=array([202,205,209,0,0])
c=a+b
print(c)
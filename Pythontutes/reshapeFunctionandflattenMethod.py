'''from numpy import*
a=array([1,2,3,4,5,6])
b=reshape(a,(3,2))
print(b)

from numpy import*
a=array([1,2,3,4,5,6,7,8,9,10,11,12])
b=reshape(a,(2,3,2))
print(b)

from numpy import*
a=array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
b=reshape(a,(12))
print(b)'''

#Flatten Array
from numpy import*
a=array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
f=a.flatten()
print(f)
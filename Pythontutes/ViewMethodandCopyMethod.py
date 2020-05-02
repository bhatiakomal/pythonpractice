#View method
'''from numpy import *
a=array([101,500,666,0,897,5,0,96,0])
b=a.view()
print(a)
print(b)
print("a",id(a))
print("b",id(b))
#It gives different memory locations for  same elements in two array

from numpy import *
a=array([101,500,666,0,897,5,0,96,0])
b=a.view()
a[2]=555
print(a)
print(b)
print("a",id(a))
print("b",id(b))#After modification in "a", "b" is also modified

from numpy import *
a=array([101,500,666,0,897,5,0,96,0])
b=a.view()
b[2]=900
print(a)
print(b)
print("a",id(a))
print("b",id(b))#After modification in "b", "a" is also modified

#Copy Method
from numpy import *
a=array([101,500,666,0,897,5,0,96,0])
b=copy(a)
print(a)
print(b)
print("a",id(a))
print("b",id(b))'''

from numpy import *
a=array([101,500,666,0,897,5,0,96,0])
b=copy(a)
a[1]=545
b[0]=545
print(a)
print(b)
print("a",id(a))
print("b",id(b))
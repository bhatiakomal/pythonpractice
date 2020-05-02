'''from numpy import*
a=array([[1,2,3,4],[5,6,7,8]])
print(a)

#Accessing elements
from numpy import*
a=array([[1,2,3,4],[5,6,7,8]])
print(a[0][2]

# Modifying Elements
from numpy import *

a = array([[1, 2, 3, 4], [5, 6, 7, 8]])
a[0][0] = 200
print(a[0][0])

#Accessing Numpy Two Dimensional Array using for Loop
#Without Index
from numpy import*
a=array([[1,2,3,4],[5,6,7,8]])
for r in a:
    for c in r:
        print(c)
    print()

#With Index
from numpy import*
a=array([[1,2,3,4],[5,6,7,8]])
a[1][2]=100
n=len(a)
for i in range(n):
    for j in range(len(a[i])):
        print(a[i][j])
    print()'''

#While loop Without Index
from numpy import*
a=array([[1,2,3,4],[5,6,7,8]])
n=len(a)
i=0
while i<n:
    j=0
    while j<len(a[i]):
        print(a[i][j])
        j+=1
    i+=1
    print()
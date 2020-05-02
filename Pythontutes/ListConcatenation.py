'''a=[1,2,3,4,5]
b=[11,15,12,22,23,]
print(a)
print(b)
x=a+b
print(x)

#Repition *
a=[1,2,3]
print(a)
x=a*3
print(x)

#Aliasing List (nick name)
a=[1,2,3,6,3]
b=a
print("A:",a)
print("B:",b)

print()

a[1]=55
print("A:",a)
print("B:",b)

print()

b[2]=90
print("A:",a)
print("B:",b)'''

#Copying and Cloning List
#copying a lsit to store in another list
a=[1,2,3,6,3]
b=a.copy()
print("A:",a)
print("B:",b)

print("After modified:")
a[1]=33

print("A:",a)
print("B:",b)

print("After modified:")
b[1]=309
print("A:",a)
print("B:",b)
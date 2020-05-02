'''a=(10,20,30,40,50)
b=(1,20,3,4,5)
print(a+b)

#Modifying in Tuple
a=(10,20,30,40,50)
b=(1,20,3,4,5)#we cannot modify or update or delete tuple's elements
print(a)
print(id(a))
print(a+b)#So we can use concatenation in tuple
print(id(a+b))

a=(10,20,30,40,50)
print(a)
c=(101,220)
d=a[0:2]
e=a[2:]
result=d+c+e

print(result)

#deleting a tuple
print("deleting a tuple")
a=(10,20,30,40,50)
print(a)
print(id(a))
x=a[0:3]
print(x)
print(id(x))

a=(10,20,30,40,50)
print(a)
print(id(a))
x1=a[0:2]
x2=a[3:]
y=x1+x2
print(y)
print(id(y))

a=(10,20,30,40,50)
print(a)
print(id(a))
x1=a[0:2]
x2=a[4:]
y=x1+x2
print(y)
print(id(y))

#Pssing a  function to a function
print("Pssing a  function to a function")
def show(m):
    print(m)
    print(type(m))
    for  i in m:
        print(i)
tup=(10,20,30,"komal")
show(tup)'''

print("Pssing and returning  function t")
def show(m):
    print(m)
    print(type(m))
    for  i in m:
        print(i)
    return (m)
tup=(10,20,30,"komal")
new_tup=show(tup)
print(new_tup)
print(type(new_tup))






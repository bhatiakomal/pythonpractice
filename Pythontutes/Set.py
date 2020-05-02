'''a={10,20,34.54,"komal"}
print(a)
print(type(a))

a={10,20,34.54,"komal",10,10,"komal"}
print(a)
print(type(a))'''

#Add elements in set
'''a={10,20,34.54,"komal"}
a.add("Bhatia")
print(a)

a=set()
a.add('komal')
print(a)
print(type(a))

#Add multiple elements in set
a=set()
a.update([101,102,103,"komal",23.43])
print(a)
print(type(a))

a={90,98,"suraj",24.43}
a.update([101,102,103,"komal",23.43])
print(a)
print(type(a))

#Delete elements in Set
a={90,98,"suraj",24.43}
print("original set:",a)
print(id(a))
a.remove(90)
print(a)
print(id(a))

a={90,98,"suraj",24.43}
print("original set:",a)
print(id(a))
a.discard("Arti")
print(a)
print(id(a))

#Use of for loop
a={90,98,"suraj",24.43}
for i in a :
    print(i)

#Getting Set input from user
print("Getting Set input from user")
a=set()
n=int(input("Enter number of elements:"))
for i in range(n):
    p=int(input("Enter elements:"))
    a.add(p)

print(a)

#Copying elements of set
a={90,98,"suraj",24.43}
print(a)
print(id(a))

new_a=a.copy()
print(new_a)
print(id(new_a))'''

#Clearing all elements in set
a={90,98,"suraj",24.43}
a.clear()
print(a)




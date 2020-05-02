'''a=[]
n=int(input("Enter your number:"))
for i in range(n):
    a.append(int(input("Enter ur element")))
print("list")
for i in a:
    print(i)

#Insert add  a element in any postion
a=[101,102,1.23,-33,'komal']
a.insert(2,'Suraj')
for i in a:
    print(i)

#Pop remove last element
a=[101,102,1.23,-33,'komal']
a.pop()
for i in a:
    print(i)

a=[101,102,1.23,-33,'komal']
a.pop(2)
for i in a:
    print(i)


a=[101,102,1.23,-33,'komal']
a.remove(102)
for i in a:
    print(i)

#Index

a=[101,102,1.23,-33,'komal']
n=a.index(-33)
print(n)

#Reverse Method
a=[101,102,1.23,-33,'komal']
a.reverse()
print("Reverse in ",a)
for i in a:
    print(i)

#Extend
a=[101,102,1.23,-33,'komal']
b=[100,234,23.56,45,"harry"]
a.extend(b)
print("extend in ",a)
for i in a:
    print(i)

a=[101,101,1.23,-33,'komal']
n=a.count(101)
print(n)

a=[20,45,60,89,1,25,63,45223,5]
print("befor sort:",a)
a.sort()
print("after short:",a)
for i in a:
    print(i)'''

a=[20,45,60,89,1,25,63,45223,5]
print("befor clear:",a)
a.clear()
print("after clear:",a)
for i in a:
    print(i)
''''stu={101:'komal',102:'suraj',103:'arti',104:'ankit'}
print(stu)

fee={'komal':2000,'suraj':3000,'Ankit':4000}
print(fee)
print("Modification")
stu[103] ='harry'
print(stu)

#insert and add in dictinary
print("insert and add in dictinary")
stu={101:'komal',102:'suraj',103:'arti',104:'ankit'}
print("Before add",stu)
print(id(stu))
print()
print("After add")
stu[104]='priya'
print(stu)
print(id(stu))

#Delete items in dictionary
print("Delete items in dictionary")
stu={101:'komal',102:'suraj',103:'arti',104:'ankit'}
print("Before Deletion",stu)
print(stu)
print(id(stu))
print()

del stu[103]
print("After deletion",stu)
print(id(stu))

#How to Test Dictionary Key exist or not
print("How to Test Dictionary Key exist or not")
stu={101:'komal',102:'suraj',103:'arti',104:'ankit'}
print(102 in stu)
print(105 in stu)
print(109 not in stu)

#Remove all the elements of dictionary
print("Remove all the elements of dictionary")
stu={101:'komal',102:'suraj',103:'arti',104:'ankit'}
print("Befor clear:")
print(stu)
print()

stu.clear()
print("After clear:")
print(stu)

#Copy in dictionary
stu={101:'komal',102:'suraj',103:'arti',104:'ankit'}
print(stu)
print(id(stu))
print()
new_stu=stu.copy()
print(new_stu)
print(id(new_stu))

#Create Dictionary using formkeys Method
key=(101,102,103)
value="komal"
new_stu=dict.fromkeys(key,value)
print(new_stu)

#Get mothod
stu={101:'komal',102:'suraj',103:'arti',104:'ankit'}
print("original dict:",stu)
print()

print(stu.get(102))
print(stu.get(109))

stu={101:'komal',102:'suraj',103:'arti',104:'ankit'}
print("original dict:",stu)
print()
p=stu.items()
print(p)
print(type(p))

lst=list(p)
print(lst)
print(type(lst))
print(lst[0])
print(lst[0][0])

for i in lst:
    for c in i:
        print(c)

stu={101:'komal',102:'suraj',103:'arti',104:'ankit'}
print("original dict:",stu)
print()

new_dict=stu.keys()
print(new_dict)
print()

lst=list(new_dict)
print(lst)
for i in lst:
    print(i)

#Values Methods
stu={101:'komal',102:'suraj',103:'arti',104:'ankit'}
print("original dict:",stu)
print()
new_dict=stu.values()
print(new_dict)
print()

lst=list(new_dict)
print(lst)
print(type(lst))
for i in lst:
    print(i)

#Update Method
stu={101:'komal',102:'suraj',103:'arti',104:'ankit'}
print("original dict:",stu)
print(id(stu))
print()

stu.update({105:'Harry'})
print(stu)
print(id(stu))

#Pop method
stu={101:'komal',102:'suraj',103:'arti',104:'ankit'}
print("original dict:",stu)
print(id(stu))
print()
stu.pop(103)
print(stu)

#Popitem
stu={101:'komal',102:'suraj',103:'arti',104:'ankit'}
print("original dict:",stu)
print(id(stu))
print()
result=stu.popitem()
print(result)

#Setdefault
stu={101:'komal',102:'suraj',103:'arti',104:'ankit'}
print("original dict:",stu)
print(id(stu))
print()
result=stu.setdefault(109,'Anku')
print(result)
print(stu)

#For loop
stu={101:'komal',102:'suraj',103:'arti',104:'ankit'}
print("original dict:",stu)
for i in stu:
    print(i)
for k in stu:
    print(stu[k])'''

a={}
n=int(input("Enter Number of elemets:"))
for i in range(n):
    k=input("Enter keys:")
    v=input("Enter values:")
    a.update({v:k})
print(a)
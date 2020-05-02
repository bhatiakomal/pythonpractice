'''a=[10,20,(30,40)]
print(a)
print(id(a))
print(type(a))

#Appending new tuple
a.append((50,60))
print("After appending",a)
print(id(a))
print(type(a))

print("excess elements:")
a=[10,20,(30,40)]
n=len(a)
for i in range(n):
    if type(a[i]) is tuple:
        if len(a[i])>1:
            m=len(a[i])
            for j in range(m):
                print(i,j,a[i][j])
    else:
        print(i,a[i])

a=[10,20,(30,40)]
a.append((50,60))
print(a)
a.append(234)
print(a)
a.append("komal")
print(a)'''

a=[(10,20),(30,40)]
n=len(a)
for i in range(n):
    for j in range(len(a[i])):
        print(i,j,a[i][j])
    print()
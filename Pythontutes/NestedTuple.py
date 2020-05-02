#For loop
''''a=(10,20,30,(40,50))
print(a)
n=len(a)
for i in range(n):
    if type(a[i]) is tuple:
        if len(a[i])>1:
            m=len(a[i])>1
            for j in range(m):
                print(i,j,a[i][j])
    else:
        print(i,a[i])

a=((10,20,30),(40,50))
for r in a:
    for c in r:
        print(c)
    print()

a=((10,20,30),(40,50))
n=len(a)
for i in range(n):
    for j in range(len(a[i])):
        print(i,j,a[i][j])
    print()

#While loop
a=(10,20,30,(40,50))
n=len(a)
i=0
while i<n:
    if type(a[i]) is tuple:
        if len(a[i])>1:
            j=0
            m=len(a[i])
            while j<m:
                print(i,j,a[i][j])
                j+=1
            i+=1

    else:
        print(i,a[i])
        i+=1

a=((10,20,30),(40,50))
n=len(a)
i=0
while i<n:
    j=0
    while j<len(a[i]):
        print(i,j,a[i][j])
        j+=1
    i+=1'''
#Slicing in nested tuple
a=((10,20,30),(40,50),(12,13,14),(32,43,54))
m=a[2:3]
print(m)
g=a[2:3][0][0]
print(g)

'''a=[10,20,30,40,[50,60]]
print(a)
n=len(a)
for i in range(n):
    print(i,a[i])

a=[10,20,30,40,[50,60]]
print("before modification:",a)
a[2]=44
a[4][1]=90
print("after modification:",a)

b=[50,60]
a=[10,20,30,40,b]
print("a:",a)

a=[[10,20,30,40],[50,60,70,80]]
print(a)
for i in a:
    print(i)

#Accessing Nested List
a=[10,20,30,40,[50,60]]
print(a)
n=len(a)
for i in range(n):
    if type(a[i]) is list:
        if len(a[i])>1:
            m=len(a[i])
            for j in range(m):
                print(i,j,a[i][j])
    else:
        print(i,a[i])

a=[[10,20,30,40],[50,60,70,80]]
n=len(a)
for i in range(n):
    m=len(a[i])
    for j in range(m):
        print(i,j,a[i][j])

#Accessing with while Loop
a=[10,20,30,40,[50,60]]
n=len(a)
i=0
while i<n:
    if type(a[i]) is list:
        if len(a[i])>1:
            j=0
            m=len(a[i])
            while j<m:
                print(i,j,a[i][j])
                j+=1
            i+=1
    else:
        print(i,a[i])
        i+=1'''

'''a=[10,20,30,40,[50,60]]
n=len(a)
i=0
while i<n:
    j=0
    while j < len(a[i]):
        print(i,j,a[i][j])
        j+=1
    i+=1'''

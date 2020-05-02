'''a=(10,20,[30,40])
print(a)
print(type(a))
a[2][0]=90
print(a)
print(id(a ))

print("access:")
n=len(a)
for i in range(n):
    if type(a[i]) is list:
        if len(a[i])>1:
            m=len(a[i])
            for j in range(m):
                print(i,j,a[i][j])
    else:
        print(i,a[i])'''
a=([10,20],[30,40])
n=len(a)
for i in range(n):
    for j in range(len(a[i])):
        print(i,j,a[i][j])
    print()
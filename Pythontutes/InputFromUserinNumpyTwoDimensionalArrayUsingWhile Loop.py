from numpy import*
m=int(input("Enter number of rows :"))
n=int(input("Enter number of column :"))
a=zeros((3,2),dtype=int)
u=len(a)
r=0
while r<u:
    c=0
    while c<(len(a[r])):
        x=int(input("Enter ur number :"))
        a[r][c]=x
        c+=1
    r+=1

r=0
while r<u:
    c=0
    while c<len(a[r]):
        print('index',r,c,"=",a[r][c])
        c+=1
    r+=1

print(a)



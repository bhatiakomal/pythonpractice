#Print upto 2decimal point
a=2154.545653165
print('%.2f'%a)

floatlst=[]
n=int(input("Enter the size of list:"))
for i in range(0,n):
    print("Enter numbers:",i)
    item=float(input())
    floatlst.append(item)
print('Usr list is:',floatlst)
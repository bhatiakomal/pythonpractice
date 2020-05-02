'''a=[101,102,78.98,32.4,104,132]
print("Original List:",a)
n=len(a)
for i in range(n):
    print(i)

print("1st to 4th ")
x=a[1:5]
print(x)
for i in x:
    print(i)

print("0 to last:")
x=a[0:]
print(x)'''

a=[10,11,13,14,15,16,17,18,19,20]
n=len(a)
x=a[::2]
print(x)
for i in x :
    print(i)
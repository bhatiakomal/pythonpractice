a=(10,20,12.34,-45,30,'Komal')
print(a)
print(type(a))

#For loop
print("for loop")
a=(10,20,12.34,-45,30,'Komal')
for i in a:
    print(i)

a=(10,20,12.34,-45,30,'Komal')
n=len(a)
for i in range(n):
    print(i,a[i])


#While loop
print('while loop')
a=(10,20,12.34,-45,30,'Komal')
n=len(a)
i=0
while i<n:
    print(i,a[i])
    i+=1
#Making List And Tuple input from User
'''values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)'''
'''a=[]
for i in range(5):
    num=int(input("Enter list"))
    a.append(num)
print(a)'''

b=[]
n=int(input("Enter number of elements"))
for i in range(n):
   b.append(int(input("Enter numbers")))
for i in b:
    print(i)
a=tuple(b)
print(a)
print(type(a))




""""mystring="hello"
mylist=[]
for letter in mystring:
    mylist.append(letter)
print(mylist)

mylist=[x for x in "Komal Bhatia"]
print(mylist)

mylist=[num for num in range(0,10)]
print(mylist)

mylist=[num**2 for num in range(0,10)]
print(mylist)

mylist=[num for num in range(0,10) if num%2==0]
print(mylist)

celcius=[10,20,45,33,23,12]
fahrenheit=[((9/5)*temp+32) for temp in celcius]
print(fahrenheit)"""



result=[x if x%2==0 else "Odd" for x in range(0,20)]
print(result)


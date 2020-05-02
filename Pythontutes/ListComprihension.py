'''lst=[1,23,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
new_lst=[]
for i in lst:
    new_lst.append(i+1)
print(new_lst)

#With List comprehension
lst=[1,23,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
new_lst=[i+1 for i in lst]
print(new_lst)

lst=[]
new_lst=[]
for i in range(20):
    new_lst.append(i+1)
print(new_lst)

new_lst=[i+1 for i in range(20)]
print(new_lst)

lst=[]
for i in range(20):
    if(i%2==0):
        lst.append(i)
print(lst)

lst=[i for i in range(20) if i%2==0]
print(lst)
lst=[]
for i in range(10):
    if(i%2==0):
        lst.append(i)
    else:
        lst.append("Invalid")
print(lst)'''

lst=[i if i%2==0 else "Invalid" for i in range(10)]
print(lst)
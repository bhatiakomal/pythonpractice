'''a=[10,20,44,56,78,89,87,60,65,81,34,12,45,60]
def high_marks(n):
    if n>=60:
        return True

result=filter(high_marks,a)
print(result)
for i in result:
    print(i)'''

#With lambda function
a=[10,20,44,56,78,89,87,60,65,81,34,12,45,60]

result=list(filter(lambda n:(n>=60),a))
print(result)
for i in result:
    print(i)
'''a=[10,20,30,40,50]
def inc(n):
    return n+2
result=map(inc,a)
print(result)
for i in result:
    print(i)

#with Lambda Function
a=[10,20,30,40,50]

result=list(map(lambda n:n+2,a))
print(result)
for i in result:
    print(i)'''

a=[10,20,30,40,50]
b=[1,2,3,4,5]
result=list(map(lambda m,n:m+n,a,b))
print(result)
for i in result:
    print(i)
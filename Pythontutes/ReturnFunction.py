#Return Statement single value
#Defining a function
def add():
    x=10
    y=20
    return(x+y)
#Calling a ffunction
sum=add()
print(sum)

def add(y):
    x=10
    return(x+y)
#Calling a ffunction
sum=add(20)
print(sum)

#Multiple value return
def add(y):
    x=30
    c=x+y
    d=x-y
    return c,d
#Calling a ffunction
sum,sub=add(10)
print(sum)
print(sub)

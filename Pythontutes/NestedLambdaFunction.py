add=lambda x=10:(lambda y:x+y)
a=add()
print(a(20))

#Passing Lambda Function to another Function
def show(a):
    print(a(8))
show(lambda x:x)

#Returning Lambda Function from a Function
def add():
    y=10
    return (lambda x:x+y)
a=add()
print(a(20))

#Immediately Invoked Function Expression
(lambda x:print(x+1))(5)
(lambda x,y:print(x+y))(5,9)
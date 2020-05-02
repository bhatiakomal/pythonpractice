#Actual Arrguments:-
def ab(x,y):
    z=x**y
    print(z)
ab(5,2)

def ab(x,y):
    z=x**y
    print(z)
ab(2,5)#postion and number of arguments should be matter a lot

#Keyword Arguments
def ab(name,age,hobby):
    print(name,age,hobby)
ab(name="Komal",age=23,hobby="sona")

#Default Argument
def show(name, age=23):
    print(name,age)
show(name="Komal")

def show(name, age=23):
    print(name,age)
show(name="Komal",age=21)#here priority wiill be given to call function

def show(name, age=23):
    print(f"Name:{name} Age:{age}")
show(name="Komal",age=21)

#variable length argument
def add(*num):
    print(num[0]+num[1])
add(2,4)

def add(x,*num):
    print(x+num[0])
add(2,4)

def add(*num):
    print(num[0]+num[1])
add(2,478,2,24,3,3,554,)

def add(**num):
    print(num['a']+num['b']+num['c'])
add(a=2,b=3,c=4)








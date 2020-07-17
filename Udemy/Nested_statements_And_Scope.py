'''x=25
def printer():
    x=50
    return (x)
rslt=printer()
print(rslt)'''

x=50
def func(x):
    print(f'X is {x}')
    #Locally Reassign
    x=200
    print(f'I just locally reassign the value {x}')
func(x)
#out of function
print(x)

'''x=50
def func():
    global x #Avoid Global function for beginner
    print(f'X is {x}')
    #Locally Reassign on global variable
    x='new value'
    print(f'I just locally changed global X to  {x}')

print(x)
#out of function
func()
print(x)'''



''''name='this is global string'
def greet():
    name='komal'
    def hello():
       # name='i am local'
        print('hello '+name)
    hello()
greet()'''
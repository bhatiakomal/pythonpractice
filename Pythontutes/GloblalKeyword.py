'''a=5
def ab():
    a=10
    print(a)

ab()

#Access global variable  outside the function
a=5
def ab():
    a=10
    print(a)

ab()
print(a)

i=5
def ab():
    i=9
    i=i+10
    print("i",i)

ab()
print("i",i)

#Access global variable through global keyword
a=0
def ab():
    global a
    a=a+1
    print(a)

ab()
print(a)'''

a=0
def ab():
    a=0
    while a<5:
        a+=1
        print(a)

ab()

a=50
def ab():
    a=10
    print("local variable:",a)
    x=globals()['a']
    print('X:',x)

ab()
print("global variable A:",a)

a=50
def ab():
    a=10
    print("local variable:",a)

    print(globals()['a'])

ab()
print("global variable A:",a)
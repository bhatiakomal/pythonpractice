'''def my_func(*args):
    return sum((args))

rslt=my_func(15,20,45,90)*0.5
print(rslt)
my_func()

def my_func(*args):# args is arbitrary choice we can change is later
   print(args)
rslt=my_func(15,20,45,90)

def my_func(*spam):
   print(spam)


def my_func(*spam):
    for items in spam:
        print(items)
rslt=my_func(15,20,45,90)

def my_func(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('my fav fruit is:{}'.format(kwargs['fruit']))
    else:
        print('This is not my fav fruit')
my_func(fruit='Mango',veggie='califlower')

def my_func(**komal):#Komal is a arbitrary choice we can change it later
    print(komal)
    if 'fruit' in komal:
        print('my fav fruit is:{}'.format(komal['fruit']))
    else:
        print('This is not my fav fruit')
my_func(fruit='Mango',veggie='califlower')

#Combination
def my_func(*args,**kwargs):
    print(args)
    print(kwargs)
    print('i would like {} {}'.format(args[0],kwargs['food']))
my_func(5,20,30,fruit='orange',food='egg',hobby='sona')'''

def my_func(*args):
    if rslt%2==0:
        print(rslt)
    else:
        print('odd')
rslt=my_func(12,13,34)



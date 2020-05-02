'''def var(x):
    x=15
    print(x,id(x))
x=10
var(x)
print(x,id(x))

def var(x):
    print(x, id(x))
    x=15
    print(x, id(x))
x=10
var(x)
print(x,id(x))

def val(lst):
    print("A:",lst,id(lst))
    lst.append(4)
    print("B:", lst, id(lst))
lst=[1,2,3]
print("c:",lst,id(lst))
val(lst)
print("D:",lst,id(lst))'''

def val(lst):
    print("A:",lst,id(lst))
    lst=(11,22,33)
    print("B:", lst, id(lst))
lst=[1,2,3]
print("c:",lst,id(lst))
val(lst)
print("D:",lst,id(lst))

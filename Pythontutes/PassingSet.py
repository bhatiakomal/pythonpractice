#Passing Set to Function
'''print("Passing Set to Function")
def show(s):
    print(s)
    print(type(s))
    for i in s:
        print(i)
st={20,30,-21,23.45,"komal"}
show(st)'''

print("Returning a function to set")
def show(s):
    print(s)
    print(type(s))
    for i in s:
        print(i)
    return s
st={20,30,-21,23.45,"komal"}
new_set=show(st)
print(new_set)
print(type(new_set))


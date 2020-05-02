'''def dis(a,b):
    yield a
    yield b
result=dis(10,20)
lst=list(result)
print(lst)
print(type(lst))
print(next(result))

def dis(a,b):
    yield a
    yield b
result=dis(10,20)
print(next(result))
print(next(result))'''

def show(a,b):
    while a<=b:
        yield a
        a+=1
result=show(1,5)
print(result)
print(next(result))

for i in result:
    print(i)


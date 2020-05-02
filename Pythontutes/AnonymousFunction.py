show = lambda x:print(x)
show(5)

add=lambda x,y:x+y
print(add(2,4))

add_sub=lambda x,y:(x+y,x-y)
a,s=add_sub(10,4)
print(a)
print(s)
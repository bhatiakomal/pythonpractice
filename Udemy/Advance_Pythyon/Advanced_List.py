a=[1,2,3,4]
a.append(10)
print(a)
print(a.count(8))
x=[1,2,3]
x.append([8,9])
print(x)
x.extend([8,9])
print(x)

y=[1,2,3,4,5,6,7,8,9]
y.insert(2,'inserted')
print(y)
y.remove('inserted')
print(y)
y.reverse()
print(y)
y.sort()
print(y)

y.pop()#Removal of last element of the set
print(y)
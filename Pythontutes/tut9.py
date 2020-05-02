#List slicing and Tuple
grocery=("harpic","toothpaste", "brush", "pista","snackes",34)
print(grocery)

grocery=("harpic","toothpaste", "brush", "pista","snackes",34)
print(grocery[4])#it will print 0,1,2,3 but not print 5 bcoz this integer

num=(1,2,3,4,5)
print(num)

num=(1,2,3,4,5)
print(num[3])#this called list slicing

num=[11,21,13,44,65]
print(num.sort())

num=[11,21,13,44,65]
num.sort()
print(num)

num=[11,21,13,44,65]
num.reverse()
print(num)

num=[11,21,13,44,65]
print(num[3])

num=[11,21,13,44,65]
print(num[1:3])

#Extended Slicing
num=[11,21,13,44,65]
print(num[::])#0:length of list:by default 1

num=[11,21,13,44,65]
print(num[::1])

num=[11,21,13,44,65]
print(num[::2])#it takes one integer and then skip one integer

num=[11,21,13,44,65]
print(num[::3])

num=[11,21,13,44,65]
print(max(num))

num=[11,21,13,44,65]
print(min(num))

num=[11,21,13,44,65]
print(len(num))

num=[11,21,13,44,65]
num.append(22)
print(num)#Append means add something in last

num=[11,21,13,44,65]
num.append(22)
num.append(22)
num.append(22)
num.append(22)
print(num)#when u write .append multiple times then multiple times that number is added

num=[]
num.append(22)
num.append(225)
num.append(228)
num.append(242)
print(num)

num=[11,21,13,44,65]
num.insert(2,56)
print(num)

num=[11,21,13,44,65]
num.remove(13)
print(num)

num=[11,21,13,44,65]
num.pop()#pop is used to remove last
print(num)

num=[11,21,13,44,65]
num[1]=100
print(num)

num=[11,21,13,44,65]
num.remove(13)#this is used for change value
print(num)

num=[11,21,13,44,65]
num.remove(13)
print(num)

#Mutable-can be change eg list-[]
#Immutable-can not be change eg tpple-()

tp=(1,2,3,4)
print(tp)#value of tuple can not be change

tp=(1,)
print(tp)

a=1
b=5
a,b=b,a
print(a,b)










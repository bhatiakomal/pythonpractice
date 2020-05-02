x=((11,12,13),
(14,15,16),
(17,18,19),
(20,21,22),
(23,24,25),
(26,27,28),
(29,30,31))

print("original tuple")
print(x)

print("1st to 4th position")
a=x[1:5]
print(a)

print("from 0 to last")
b=x[0:]
print(b)

print("last 4 tuples")
c=x[-4:]
print(c)

print("0 to 6th stepie 2")
d=x[0:7:2]
print(d)

print("slicing in nested tuples,2nd and 0th position")
e=x[2:3]
print(e)
f=x[2:3][0]
print(f)

print("slicing in nested tuples,2nd and 0th position 1st element")
g=x[2:3]
print(e)
h=x[2:3][0][0]
print(f)

print("extract element of nested tuples")
i=x[2:3][0]
for a in i:
    print(a)

print("last nested 4 tuples then 1st position:")
p=x[-4:][1]
print(p)
l=x[-4:][1]
for s in l:
    print(s)
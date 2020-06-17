#MY Style:
a="1"
print(a*1)
b="2 "
print(b*2)
c="3 "
print(c*3)
d="4 "
print(d*4)
e="5 "
print(e*5)
print(type(a))

#Actual Solution
for i in range(6):
    for k in range(i):
        print(i,end=" ")
    print("\n")

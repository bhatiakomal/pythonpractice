x=[[11,12,13],
   [14,15,16],
   [17,18,19],
   [20,21,22],
   [23,24,25],
   [26,27,28],
   [29,30,31]]
print("original list:",x)

print()
print("1st to 4th position:")
print(x[1:5])
print()

print("0 to last")
print(x[0:])
print()

print("0 to 5th position:")
print(x[:5])
print()

print(x[0:7:2])
print()

m=x[2:3]
print(m)
g=x[2:3][0]
print(g)
print()
#Slicing 2nd list and extract its elemets
print("Slicing 2nd list and extract its elemets")
h=x[2:3][0][0]
print(h)
i=x[2:3][0]
for k in i:
   print(k)



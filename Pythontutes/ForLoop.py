'''a=range(5)
for i in a:
    print(i)

a=range(1,10,2)
for i in a:
    print(i)

#for loop used in string with range
st="Komalbhatia"
a=len(st)
for m in range(10):
    print(m,"=",st[m])

#For loop with Else
st="komal"
for m in st:
    print(m)
else:
    print("print else part")
print("Rest of the code")'''

#Nested for Loop:
for i in range(2):
    print("Outer loop",i)
    for j in range(3):
        print("inner loop",j)
print("Rest of the code")
#While loop
''''a=1
while a<=10:
    print(a)
    a+=1
print("Rest of the code")

a=2
while a<=20:
    print(a)
    a+=2
print("Rest of the code")#Table of 2

#While Loop With Else
a=1
while a<=5:
    print(a)
    a+=1
else:
    print("now execute else part")
print("Rest of the code")

a=6
while a<=5: #here while loop is false first time directly so Else part executed directly
    print(a)
    a+=1
else:
    print("now execute else part")
print("Rest of the code")

#While Infinite True
a=0
while True:
    a+=1
    print(a)
    if(a==5):
        break
print("Rest of the Code")'''

#Nested While
i=1
while i<=3:
    print("outer loop",i)
    i+=1
    j=1
    while j<=5:
        print("inner loop",j)
        j+=1
print("Rest of the code")
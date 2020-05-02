'''dict={}
for n in range(20):
    dict[n]=n*2
print(dict)

dict={n:n*2 for n in range(10)}
print(dict)

dict={}
for i in range(10):
    if  i%2==0:
        dict[i]=i*2

print(dict)'''

'''dict={}
for i in range(10):
    if  i%2==0:
        dict[i]=i
    else:
        dict[i]="invalid"

print(dict)

dict={n:(n if n%2==0 else "Invalid") for n in range(10)}
print(dict)

lst=[(101,"koma"),(102,"Bhatia")]
dict={k:v for k,v in lst}
print(dict)'''

dict={}
for i in range(10):
    if  i%2==0:
        if i%3==0:
                dict[i]=i*2

print(dict)

dict={i:i*2 for i in range(10) if i%2==0 if i%3==0}
print(dict)
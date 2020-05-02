'''a={1:{'name':'komal','age':23,'salary':'berojgar'},
   2:{'hobby':'travel','dream':'big','want':'luxury'}}
print(a)
print(a[1])
print(a[1]['salary'])
print(a[2])
print(a[2]['dream'])

print("Modifying")
a={1:{'name':'komal','age':23,'salary':'berojgar'},
   2:{'hobby':'travel','dream':'big','want':'luxury'}}
print(a)
a[1]['salary']=200000
print(a)
a[2]['dream']='bhot bde hain hahhahhahahha'
print(a)

print('delete')
del a[1]['salary']
print(a)

print('add')
a[2]['watch']='Netflix'
print(a)'''

print('Access Nested Dictionary Ny For loop')
a={1:{'name':'komal','age':23,'salary':'berojgar'},
   2:{'hobby':'travel','dream':'big','want':'luxury'}}
print('ID:')
for id in a:
    print(id)

for id in a:
    for k in a[id]:
        print(k,'=',a[id][k ])
print()

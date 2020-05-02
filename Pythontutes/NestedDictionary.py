'''a={'name':'komal','salary':150000,1:{'job':'coder','address':'Himachal'}}
print(a['name'])
print(a[1])
print(a[1]['address'])

print("After modifying")
a[1]['job']='IAS'
print(a)
print()
print("Delete")
del a[1]['address']
print(a)
print()
a['duration']='two years'
print(a)
print()
a[1]['behaviour']='cool'
print(a)
print()
a[2]={'Hobby':'Travell','Fav food':'Pizza','fav movie':'Iron man'}
print(a)'''

print("Accessing dictionary by for loop ")
a={'name':'komal','salary':150000,1:{'job':'coder','address':'Himachal'}}
for i in a:
    if type(a[i]) is  dict:
        for c in a[i]:
            print(c,'=',a[i][c])

    else:
        print(i,'=',a[i])

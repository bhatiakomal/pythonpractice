''''def show(d):
    print(d)
    for k in d:
        print(k,'=',d[k])
dc={1:{'name':'komal','age':23,'salary':'berojgar'},
   2:{'hobby':'travel','dream':'big','want':'luxury'}}
show(dc)'''

print('Returning')
def show(d):
    print(d)
    print(type(d))
    for k in d:
        print(k,'=',d[k])
    return d
dc={'name':'komal','age':23,'salary':'berojgar'}

new_dict=show(dc)
print(new_dict)
print(type(new_dict))

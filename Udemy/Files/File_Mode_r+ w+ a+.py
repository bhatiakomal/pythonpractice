'''f=open('Childern.txt',mode='r+')
data=f.read()
print(f.tell())
f.write('Welcome on Youtube ')
print(f.tell())
print(data)
print(f.tell())
f.close()'''

#w+ 1st write data and override(exiting data is deleted) the data then read the data
'''f=open('Childern.txt',mode='w+')
print(f.tell())
f.write('Youtube')
print(f.tell())
f.seek(0)
data=f.read()
print(f.tell())
print(data)'''

#a+ is same as w+ but it append the data in the last position
f=open('Childern.txt',mode='a+')
print(f.tell())
f.write("Youtube")
print(f.tell())
print(f.seek(0))
data=f.read()
print(f.tell())
print(data)

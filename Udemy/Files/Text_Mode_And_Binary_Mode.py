f=open('student.txt',mode='w')#W= is write mode
f.write("hello Miss Komal\n")
f.write('How Are you???\n')
f.write('I am very glad to meet you')
f.close()
print('Writing succcess')

f=open('student.txt',mode='r')#r is text mode's read mode(r)
data=f.read()
print(data)
f.close()

f=open('student.txt',mode='rb') #r is read mode of binary
data=f.read()
print(data)
f.close()

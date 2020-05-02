#Slicing in Array
'''from array import *
stu_roll=[101,102,103,104,105,106,107,108,109,110]
n=len(stu_roll)
print(stu_roll[1:5])'''

'''from array import *
stu_roll=array('i',[101,102,103,104,105,106,107,108,109,110])
print("Orignal Array ")
n=len(stu_roll)
for i in range(n):
    print(i,"=",stu_roll[i])
print('*************')

a=stu_roll[:5]
for i in a:
    print(i)'''

'''from array import *
stu_roll=array('i',[101,102,103,104,105,106,107,108,109,110])
print("Orignal Array ")
n=len(stu_roll)
for i in range(n):
    print(i,"=",stu_roll[i])
print('*************')

a=stu_roll[-5:-3]#-5-(-3)=-5+3=-2 take last 5 elements then take 2 elements from last five
for i in a:
    print(i)'''

''''from array import *
stu_roll=array('i',[101,102,103,104,105,106,107,108,109,110])
print("Orignal Array ")
n=len(stu_roll)
for i in range(n):
    print(i,"=",stu_roll[i])
print('*************')

a=stu_roll[0:9:2]
for i in a:
    print(i)'''

from array import *
stu_roll=array('i',[101,102,103,104,105,106,107,108,109,110])
for i in stu_roll[1:5]:
    print(i)


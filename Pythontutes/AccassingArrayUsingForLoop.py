#Without Index
'''from numpy import*
stu_roll=array([101,102,103,104,105])
for i in stu_roll:
    print(i)'''

#with index
'''from numpy import*
stu_roll=array([101,102,103,104,105])
n=len(stu_roll)
print(n)
for i in range(n):
    print(i,'=',stu_roll[i])'''

from numpy import*
stu_roll=array([101,102,103,104,105])
stu_roll[3]=222
n=len(stu_roll)
print(n)
for i in range(n):
    print(i,'=',stu_roll[i])
#POP-This method is used to removed last element from a array.
'''from array import *
stu_roll=array('i',[101,102,103,104,105])
n=len(stu_roll)
i=0
while i<n:
    print(stu_roll[i])
    i+=1
print("Print Array After Pop")
stu_roll.pop()
n=len(stu_roll)
i=0
while i<n:
    print(stu_roll[i])
    i+=1'''

#POP(n)-This method is used to removed any element from a array and also add element.
from array import *
stu_roll=array('i',[101,102,103,104,105])
n=len(stu_roll)
i=0
while i<n:
    print(stu_roll[i])
    i+=1
print("Print Array After Pop")
stu_roll.pop(4)
n=len(stu_roll)
i=0
while i<n:
    print(stu_roll[i])
    i+=1


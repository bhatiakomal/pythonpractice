##Accessing Array Using For loop
#Without index
'''from array import *
stu_roll =array('i',[101,102,103,104,105])
print(stu_roll)

from array import *
stu_roll =array('i',[101,102,103,104,105])
for el in stu_roll:
    print(el)'''

#with index
from array import *
stu_roll =array('i',[101,102,103,104,105])
n=len(stu_roll)
for i in range(n):
    print(i,"=",stu_roll[i])
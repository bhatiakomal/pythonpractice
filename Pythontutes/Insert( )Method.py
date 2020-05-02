from array import *
stu_roll=array('i',[101,102,103,104,105])
n=len(stu_roll)
i=0
while i<n:
    print(stu_roll[i])
    i+=1
print("Print after Array")
stu_roll.insert(0,108)
stu_roll.insert(4,756)
stu_roll.insert(2,568)
n=len(stu_roll)
i=0
while i<n:
    print(stu_roll[i])
    i+=1
from array import *
stu_roll=array('i',[101,102,103,104,105])
arr1=array('i',[110,109,108])
n=len(stu_roll)
i=0
while i<n:
    print(stu_roll[i])
    i+=1
print("Print Array After Extend")
stu_roll.extend(arr1)
n=len(stu_roll)
i=0
while i<n:
    print(stu_roll[i])
    i+=1
from array import *
stu_roll=array('i',[ ])
n=int(input("Enter your Element:"))
i=0
j=0
while i<n:
    stu_roll.append(int(input("Enter Roll Number")))
    i+=1
while j<len(stu_roll):
    print(stu_roll[j])
    j+=1
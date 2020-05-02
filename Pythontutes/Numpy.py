#creating 1-D array using array( )function
'''import numpy
stu_roll=numpy.array([101,102,103,104,105])
print(stu_roll)
print(stu_roll.dtype)
print(stu_roll[3])'''

'''import numpy
stu_roll=numpy.array([101,102,103,104,105],dtype=float)
print(stu_roll)
print(stu_roll.dtype)
print(stu_roll[1])
print(stu_roll[0])
print(stu_roll[2])
print(stu_roll[4])'''

import numpy
stu_roll=numpy.array([101,102,103,104,105])
(stu_roll[1])=111
print(stu_roll)
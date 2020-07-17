'''def func_one(n):
    return [str(num) for num in range(n)]
rslt=(func_one(10))
print(rslt)

def func_two(n):
    return list(map(str , range(n)))
rslt=(func_one(10))
print(rslt)
import time
#Current Time
start_time=time.time()
#Run the code
result=func_one(10)
#Current time after running code
end_time=time.time()
#Elapsed time
elapsed_time=end_time-start_time
print(elapsed_time)

import time
#Current Time
start_time=time.time()
#Run the code
result=func_two(10000)
#Current time after running code
end_time=time.time()
#Elapsed time
elapsed_time=end_time-start_time
print(elapsed_time)'''

import timeit
stmt='''
func_one(1000)
'''
setup='''
def func_one(n):
    return [str(num) for num in range(n)]
'''
print(timeit.timeit(stmt,setup,number=1000))

def func_one(n):
    return [str(num) for num in range(n)]
rslt=(func_one(10))
print(rslt)






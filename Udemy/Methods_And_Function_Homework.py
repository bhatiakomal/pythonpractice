'''def vol(rad):
    return (4/3)*3.14*rad**3
volume=vol(2)
print(volume)

def check_run(num,low,high):
    return num in range(low,high+1)
rslt=check_run(5,2,7)
print(rslt)

def check_run(num,low,high):
    if num in range(low,high+1):
        print(f'num is in range {2} and {7}')
    else:
        print('not in range')
check_run(5,2,7)'''

'''def ups_low(s):
    lowercase=0
    uppercase=0
    for char in s:
        if char.isupper():
            uppercase+=1
        elif char.islower():
            lowercase+=1
        else:
            pass
    print(f'orignal string:{s}')
    print(f'lowercase count:{lowercase}')
    print(f'upper case count;{uppercase}')
ups_low('Hello Komal ...How are you..??? It has been long to Meet.')'''

'''def unique(lst):
    return list(set(lst))
rslt=unique([1,2,3,3,1,2,5,5,4,7,8,8,9,1])
print(rslt)


def unique(lst):
    seen_numbers=[]
    for number in lst:
        if number not in seen_numbers:
            seen_numbers.append(number)
    return seen_numbers
rslt=unique([1,2,3,3,1,2,5,5,4,7,8,8,9,1])
print(rslt)'''

'''def multiply(numbers):
    total=2
    for numb in numbers:
        total=total*numb
    return total
rslt=multiply([1,2,3,4])
print(rslt)'''

'''def pelidrom(s):
    s=s.replace(' ','')
    return s
rslt=pelidrom('komal run')
print(rslt)

#Reverse the  string
print()
def pelidrom(s):
    s=s.replace(' ','')
    return s==s[::-1]
rslt=pelidrom('ko ma l r un')
print(rslt)'''

import string
def inpangram(str1,alphabet=string.ascii_lowercase):
    alphaset=set(alphabet)
    str1=str1.replace(' ','')
    str1=str1.lower()
    str1=set(str1)
    return str1==alphaset
rslt=inpangram('the quick brown fox jumps over the lazy dog')
print(rslt)






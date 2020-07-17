"""eg=[1,2,3,4,5,6,7,8,9]
from random import shuffle
shuffle(eg)
print(eg)
from random import shuffle
eg=[1,2,3,4,5,6,7,8,9]
def shuffle_lst(mylst):
    shuffle(mylst)
    return mylst
rslt=shuffle_lst(eg)
print(rslt)


from random import shuffle
def player_guess():
    guess=''
    while guess  not in['0','1','2']:
        guess=input("pick a number:0,1,or 2")
        return int(guess)
check=player_guess()
print(check)"""

def myfunc(a):
    if a==True:
        return 'Hello'
    else:
        'Goodbye'
b=myfunc('a')
print(b)





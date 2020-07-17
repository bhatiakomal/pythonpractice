"""def even_check(number):
    result= number%2==0
    print(result)
rslt=even_check(20)
rslt1=even_check(45)

def check_even(num_list):
    for num in num_list:
        if num%2==0:
            return (True)
        else:
            pass
    return False
result=check_even([2,3,4,6,7,8,9])
result1=check_even([5,7,9])
print(result)
print(result1)"""

def check_even_lst(num_lst):
    even_num=[]
    for number in num_lst:
        if number % 2 == 0:
            even_num.append(number)
        else:
            pass
    return even_num
numb=check_even_lst([22,34,54,57,68,21,34])
print(numb)






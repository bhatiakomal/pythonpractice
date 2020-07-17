'''def dis(num):
    for i in range(0,len(num)-1):
        if num[i]==3 and num[i+1]==3:
            return True
    return False
rslt1=dis([1,3,3])
rslt2=dis([3,2,3])
rslt3=dis([3,3,5])
print(rslt1)
print(rslt2)
print(rslt3)'''

'''def disp(text):
    result=''
    for char in text:
        result+=char*3
    return result
rslt=disp('hello')
print(rslt)'''

'''def check_sum(a,b,c):
    if sum([a,b,c])<=21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c])<=31:
        return sum([a,b,c])
    else:
        return 'Bust'
rslt=check_sum(10,5,2)
rslt1=check_sum(12,34,32)
print(rslt)
print(rslt1)'''

def summer_69(arr):
    total=0
    add=True
    for num in arr:
        while add:
            if num!=6:
                total+=num
                break
            else:
                add=False
        while not add:
            if num!=9:
                break
            else:
                add=True
    return total
rslt=summer_69([1,3,5])
rslt1=summer_69([4,5,6,7,8,9])
rslt2=summer_69([2,1,6,9,11])
print(rslt)
print(rslt1)
print(rslt2)



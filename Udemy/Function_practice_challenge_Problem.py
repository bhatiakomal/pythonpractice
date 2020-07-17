def spy_game(nums):
    code=[0,0,7,'x']
    for num in nums:
        if num==code[0]:
            code.pop(0)
    return len(code)==1
rslt1=spy_game([1,2,3,4,0,0,7])
rslt2=spy_game([1,0,3,4,1,0,7])
rslt3=spy_game([1,0,0,4,1,3,7])
rslt4=spy_game([1,2,7,4,0,0,9])
print(rslt1)
print(rslt2)
print(rslt3)
print(rslt4)

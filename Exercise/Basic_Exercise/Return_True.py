def Return_True(a):

    if a[0]==a[-1]:
        return True
    else:
        return False
rslt=Return_True(a=[10, 20, 30, 40, 10])
print('The result is:',rslt)

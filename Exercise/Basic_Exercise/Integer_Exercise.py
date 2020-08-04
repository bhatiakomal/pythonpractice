def ifElseStatement(a,b):
    product=a*2
    if product<=1000:
        return product
    else:
        return (a+b)
a=int(input('Enter 1st number:'))
b=int(input('Enter 2st number:'))
result=ifElseStatement(a,b)
print('Your result is:',result)

def mergList(a,b):
    print('frist list:',a)
    print('Second list:',b)
    third_list=[]
    for i in a:
        if (i%2 != 0):
            third_list.append(i)
    for i in b:
        if (i%2==0):
            third_list.append(i)
    return third_list
a=[10, 20, 23, 11, 17]
b=[13, 43, 24, 36, 12]
result=mergList(a,b)
print("Result is:",result)



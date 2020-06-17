def combine_lst(Lst1,lst2):
    print("Lst_one:",Lst1)
    print("Lst_two:",lst2)
    thirdlst=[]
    for num in lst1:
        if (num%2!=0):
            thirdlst.append(num)
    for num in lst2:
        if (num%2==0):
            thirdlst.append(num)
    return thirdlst
lst1=[11,12,13,14,15,16]
lst2=[17,18,19,20,21,22]
print(combine_lst(lst1,lst2))


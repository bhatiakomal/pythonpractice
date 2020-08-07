list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
lst3=[i+j for i,j in zip(list1,list2)]
print(lst3)
print([x+y for x in list1 for y in list2])
def show(numblist):
    print("Given list is:",numblist)
    print("print list divided by 5")
    for i in numblist:
        if i%5==0:
            print(i)

num=[10,15,12,34,45,75,65,80,98,76]
show(num)
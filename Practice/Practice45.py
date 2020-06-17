def show(numberlist):
    print("print orignal list:",numberlist)
    for i in numberlist:
        if i%5==0:
            print(i)
num=[10,32,35,67,84,65,90,70]
show(num)
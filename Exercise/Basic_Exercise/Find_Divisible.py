def findDivisible(numberList):
    print("Given list is ", numberList)
    for i in numberList:
        if (i % 5 == 0):
            print(i)
numList = [10, 20, 33, 46, 55]
findDivisible(numList)
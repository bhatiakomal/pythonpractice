#Print largest number in the list
aList = [4, 6, 8, 24, 12, 2]
print(max(aList))

#Print even number in the given range
print(list( range(4, 30, 2)))

def even():
    l=[]
    for i in range(4,31):
        if i%2 ==0:
            l.append(i)
    return l

print(even())
from collections import Counter
n=int(input("Enetr number of Words:"))
l=list()
for _ in range(n):
    l.append(input())
x=Counter(l)
#print(x)
print(len(x))
print(*x.values())
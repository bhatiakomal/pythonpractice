a={'komal','bhatia','suraj','singh','ankit','nadda'}
b={'shikha','aarti','rishi','suraj','komal'}
print("A:",a)
print("B:",b)
print()
#Intersection
print("intersection")
result=a.intersection(b)
print(result)
print()
#Union
print("Union")
result=a.union(b)
print(result)
print()

##Difference
print("Difference")
result=a.difference(b)
print(result)
print()

#Subset
print("Subset")
result=a.issubset(b)
print(result)
print()

#Superset
print("Superset")
result=a.issuperset(b)
print(result)
print()
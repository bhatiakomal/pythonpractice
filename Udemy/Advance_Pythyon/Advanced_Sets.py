'''s={1,2,3,4,5}
sc=s.copy()
print(sc)
a={1,3,2,4,5,6}
print(s.difference(a))'''

'''s1={1,2,3}
s2={1,4,5}
print(s1.difference_update(s2))
print(s1)'''

'''s={1,2,3,4,5}
(s.discard(2))
print(s)

#Intersaction Method
s1={1,2,3}
s2={1,2,4}
print(s1.intersection(s2))
s1.intersection_update(s2)
print(s1)'''

s1={1,2}
s2={1,2,4}
s3={5}
print(s1.isdisjoint(s2))#this retrun false if something is common in both the sets
print(s1.isdisjoint(s3))
print(s1.issubset(s2))
print(s1.issuperset(s2))
print(s1.symmetric_difference(s2))
s1.update(s2) #Union of itself and others
print(s1)


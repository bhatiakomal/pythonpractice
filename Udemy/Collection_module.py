'''from  collections import Counter
mylist=[1,2,1,2,3,4,3,2,4,5,6,2,3,4]
print(Counter(mylist))
print()
mylist1=('a','a','a','v','v','w','w',10,11,12,11,10)
print(Counter(mylist1))
print()
mylist2=('aabbcc')
print(Counter(mylist2))
print(mylist2.upper())
print()
letters='aabbccjjooekdwdjwjdsddd'
c=Counter(letters)
print(c.most_common())'''

from collections import defaultdict
d={'a':10}
print(d)
print(d['a'])
d=defaultdict(lambda:0)
d['wrong']=100
print(d['wrong'])
print(d['wrong key!'])
print(d)
'''import  math
#print(help(math))
v=4.45
print(math.ceil(v))
print(math.floor(v))
print(round(78.90))
print(math.pi)'''

import random
mylist=list(range(0,21))
print(mylist)
print(random.choice(mylist))
print(random.choices(population=mylist,k=10))
print(random.sample(population=mylist,k=10))
print(random.shuffle(mylist))



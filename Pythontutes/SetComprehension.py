#Set Comprehension
''''set1={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19}
new_set1=set()
for i in set1:
    new_set1.add(i+1)

print(new_set1)

#With Set Comprehension
set1={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19}
new_set1=set(i+1 for i in  set1)
print(new_set1)

new_Set={i+1 for i in range(20)}
print(new_Set)
print()
new_Set={i for i in range(20) if i%2==0}
print(new_Set)

set1=set()
for i in range(20):
    if  i%2==0:
        if i%3==0:
            set1.add(i)
print(set1)

new_Set={i for i in range(20) if i%2==0 if i%3==0}
print(new_Set)

new_Set={i if i%2==0 else i*100 for i in range(20)  }
print(new_Set)'''

print("Nested set Comprehension")
st={(i,j) for j in range(4,7) for i in range(6,8) }
print(st)
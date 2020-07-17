"""lst=[1,2,3,4,5,6,78,9,10]
for num in lst:
    print("Komal")"""

"""lst=[1,2,3,4,5,6,7,8,9,10]
for num in lst:
    if num%2==0:
        print(f"even numbers:{num}")
    else:
        print(f"odd numbers:{num}")

lst=[1,2,3,4,5,6,7,8,9,10]
my_lst=0
for num in lst:
    my_lst=my_lst+num
print(my_lst)

lst=[(1,2),(3,4),(5,6),(7,8),(9,10)]
for (a,b) in lst:
    print(a)
    print()

my_dictionary={"apple":220,"mango":100,"orange":50}
for item in my_dictionary:
    print(item)
for things in my_dictionary.items():
    print(things)

x=0
while x<5:
    print(f"print current value of {x}")
    x+=1
else:print(f"x is not less than {x}")

index_count=0
for letter in "KomalBhatia":
    print("At index {} the letter is {}".format(index_count,letter))
    index_count+=1"""

a=[1,2,3,4]
b=['a','b','c','d']
for itme in zip(a,b):
    print(itme)
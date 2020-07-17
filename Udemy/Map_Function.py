'''def square(num):
    return num**2
my_num=[1,2,3,4,5]
for item in map(square,my_num):
    print(item)
rslt=list(map(square,my_num))
print(rslt)

def splicer(string):
    if len(string)%2==0:
        return "Even"
    else:
        return string[0]
name=(['Anny','Komal','Ankit','priya'])
rslt=list(map(splicer,name))
print(rslt)'''

def check_Even(num):
    return num%2==0
mynum=[1,2,3,4,5,6,7,8,9,10]
rslt=list(filter(check_Even,mynum))
print(rslt)
for i in filter(check_Even,mynum):
    print(i)




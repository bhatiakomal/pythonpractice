a="Hello World"
print(a)
a=a[1:]
b="P"+a
print(b)

print("this is inserted {}".format("string"))
print("the {} {} {}".format("fox","quick","brown"))
print()
print("the {1} {2} {0}".format("fox","quick","brown"))
print()
print("the {2} {2} {2}".format("fox","quick","brown"))
print()
print("the {b} {q} {f}".format(f="fox",q="quick",b="brown"))

a=100/777
print(a)
print("the result is",format(a,".2f"))
print("the result is{}".format(a,".2f"))

name="komal"
print(f"hello, her name is {name}")
print()
name="ocean"
age=3
print(f"{name} is {age} years old" )
print("List")
my_list=["komal",20,256.325,"Aarti"]
another_list=["Suraj",345,67787.325,"Ankit"]
print(my_list+another_list)
my_list[0]="KOMAL"
print(my_list)
a=["komal",23,45.76]
print(a)
print()

my_dictionary={"apple":220,"mango":100,"orange":50}
print(my_dictionary)
print(my_dictionary["apple"])
d={"k1":['a','b','c']}
p=d["k1"][2].upper()
print(p)
d["k3"]=40
print(d)



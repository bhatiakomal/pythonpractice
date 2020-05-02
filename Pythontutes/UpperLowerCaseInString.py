'''name="harry potter"
print(name)
print(name.upper())
print(name.title())

name="harry potter"
p=name.title()
print(p)
print(name)'''

#Isupper and Islower case
name="HARRY POTTER"
print(name.isupper())

name="harry potter"
print(name.isupper())

name="harry potter"
print(name.islower())

name="HARRY POTTER"
print(name.islower())

name=("hARRY POTTER")
print(name.isupper())

name=("hARRY POTTER")
print(name.istitle())

name=("Harry  Potter")
print(name.istitle())

#isdigit isalpha and isalnum String Functions
name="1223343546"
print(name.isdigit())

name="komal"
print(name.isalpha())

name="komal1233"
print(name.isalnum())

name="komal"
print(name.isalpha())

#isspace String Function
name=" "
print(name.isspace())
print(name.isspace())

#lstrip rstrip and strip String
name="   komal"
print(name.lstrip())

name="komal    "
print(name.lstrip())

name="   komal   "
print(name.strip())

print("replace split and join")
name="komal"
old="komal"
new="priya"
print(name.replace(old,new))

k="Hello- komal- bhatia- gg"
print(k.split('-'))

k=('Hello', ' komal', ' bhatia', ' gg')
print(' '.join(k))

print("startswith and endswith String Functions")
k="Hello komal bhatia gg"
print(k.startswith('Hello'))
print(k.endswith("gg"))
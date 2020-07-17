#Part1
'''import re
text="komal likes adventure trips, she wants travels around the world ,trip"
print('world'in text)
pattern='world'
print(re.search(pattern,text))
match=re.search(pattern,text)'''

#Part2
import re
text='My phone number is 821-320-8610 '
phone=re.search(r'\d{3}-\d{3}-\d{4}',text)
print(phone.group())
'''phone_patttern=re.compile(r'(d{3})-(d{3})-(d{4})')
rslt=re.search(phone_patttern,text)
rslt.group()'''#Its not working ....why

#part3
import re
print(re.search(r'cat','the cat is here'))
print(re.findall(r'.at','mat rat hat cat is here'))
print(re.findall(r'^\d','1 is a number'))
print(re.findall(r'^\d','the 3 is a number'))
phrase='there are 2 men and 6 women are holding a 8 pices of cake'
pattern=r'[^\d]'
print(re.findall(pattern,phrase))
pattern=r'[^\d]+'
print(re.findall(pattern,phrase))
phrase='there are 2 men and!  6 women are @holding a 8 pices# of cake'
print(re.findall(r'[^! @ #]+',phrase))

text='She is really-nice person,cake cutting time come-on'
v=r'[\w]+-[\w]+'
print(re.findall(v,text))
from time import time,ctime,localtime
#if want to import whole time module we can import it like this one(from time import*)
epoch=time()
#it represneets whole seconds till now
print(epoch)
et= ctime(epoch)
#It shows us todays date
print(et)

#it give us all atributes
with_atributes=localtime()
print(with_atributes)
#We can also access year date month individually
print(with_atributes.tm_year)
print(with_atributes.tm_mon)

#Well formated use of date
with_atributes=localtime()
print(with_atributes)
print(with_atributes.tm_mday,end='/')
print(with_atributes.tm_mon,end='/')
print(with_atributes.tm_year)

print('Well formated use of date')
with_atributes=localtime()
print(with_atributes)
print(with_atributes.tm_hour,end=':')
print(with_atributes.tm_min,end=':')
print(with_atributes.tm_sec)
